""" Elo and Markov Stationary Live Rankings (Demo Script)

07-01-2017
"""

import time

import numpy as np
from scipy.linalg import eig

from pylab import *
import seaborn as sns

import pandas as pd

###############################################################################
# Ranking functions

def total_update(scores, winner, loser):
    """ Update the naive point-based ranking

    Parameters
    ----------
    scores : ndarray
        current Elo scores
    winner : int
        index of winning team
    loser : int
        index of loosing team
        
    """
    scores[winner] += 1
    scores[loser] -= 1

def elo_update(scores, winner, loser, xi=400, k=100):
    """ Update a given Elo-Ranking

    Parameters
    ----------
    scores : ndarray
        current Elo scores
    winner : int
        index of winning team
    loser : int
        index of loosing team
    xi : float, optional
        Scaling factor applied in sigmoid function
    k : float, optional
        Update factor
    """

    def get_mu(team1, team2):
        dij = scores[team1] - scores[team2]
        return 1/(1 + 10**(-dij/xi))
    
    mu_winner = get_mu(winner, loser)
    mu_loser  = get_mu(loser, winner)
    
    scores[winner] += k * (1 - mu_winner)
    scores[loser]  += k * (0 - mu_loser)

def markov_stationary(matrix, alpha=0.85, nb_iterations=100):
    """ Compute the stationary vector for a markov process

    Paramters
    ---------
    matrix : ndarray
        MxM matrix with scores between all teams
    alpha : float, optional
        Fixed addition to matrix to guarantee primitivity
        (needed for convergence)
    nb_iterations : int, optional
        Number of maximum iterations

    Returns
    -------
    ndarray
        Vector with stationary probabilities of the given
        markov process
    """

    i = 0

    nb_teams = matrix.shape[0]
    I = np.ones(shape=(nb_teams))
    I_ = np.zeros(shape=(nb_teams))
    I__ = np.zeros(shape=(nb_teams))

    I /= I.sum()

    def update_G(m, I):
        matrix = m.copy()
        print(matrix)
        idc_zeros = ( matrix.sum(axis=1) == 0 )
        fill_vals = I + 0.5
        fill_vals /= fill_vals.sum()
        matrix[idc_zeros,:] = fill_vals #np.array([0.2] + [0.8/5]*5)
        matrix = matrix / matrix.sum(axis=1,keepdims=True)
        print(idc_zeros)
        G = alpha * matrix + (1-alpha)/len(matrix)
        return G

    j = 0 
    m = matrix.copy()
    while j < nb_iterations  and not np.all(np.isclose(I, I__)):
        G = update_G(matrix, I)
        I__ = I

        # Variant 1: Direct calculation of Eigenvectors
        vals,vecs = eig(G.T)
        Ie = np.real(vecs[:,0])
        Ie /= Ie.sum()

        # Variant 2: Iterative calculation of Eigenvectors 
        i = 0
        while i < nb_iterations and not np.all(np.isclose(I, I_)):
            I_ = I
            I = np.dot(G.T,I)
            i += 1
        j += 1

        #assert(np.allclose(Ie, I)), (Ie, I)

    print("Markov converged after {} iterations".format(j))

    assert np.isclose(I.sum(), 1.)

    return I

###############################################################################
# I/O, HTML Output, Plotting

def write_html(table, elo_scores, total_scores, markov_scores):
    
    with open("index.html.tpl", "r") as fp:
        template = fp.read()

    def print_html(scores):
        idc = np.argsort(-scores)
        s = '<ul class="list-group">\n'
        place = 1
        score = 1000000
        for n,i in enumerate(idc):
            if scores[i] < score:
                place = n+1
                score = scores[i]
            s+='<li class="list-group-item">'
            s+='<span class="badge">{:d}</span>'.format(int(scores[i]))
            s+="{}. Team {}</li>\n".format(place,id2team[i],scores[i])
        s += "</ul>"

        return s

    def print_ticker(table):
        
        s = '<ul class="list-group">\n'
        for t, i in enumerate(table.index[-10:]):
            game = table.iloc[i]
            teams = [team2id[game["Team 1"]], team2id[game["Team 2"]]]
            result = game["Result"]
            winner, loser = teams[result], teams[1-result]
            s+='<li class="list-group-item">'
            s+='<span class="badge">{}</span>'.format(game["Spiel"])
            s+='Team {} gewinnt gegen {} </p></li>\n'.format(id2team[winner],id2team[loser])
        s += "</ul>"

        return s

    ticker = print_ticker(table)
    elo = print_html(elo_scores)
    points = print_html(total_scores)
    markov = print_html(markov_scores*100)
    
    with open("index.html", "w") as fp:
        fp.write(template.format(time.strftime("%d-%m-%Y %H:%M:%S"), ticker, elo, markov, points))

def plot_history(fname, history):
    figure(figsize=(16,10))
    sns.despine()
    for i in range(history.shape[1]):
        plot(history[:,i],label=id2team[i])
    legend()
    savefig(fname, bbox_inches="tight")

def compute_ranking():
    elo_scores = np.zeros(shape=(nb_teams,)) + 1200
    total_scores = np.zeros(shape=(nb_teams,))
    matrix = np.zeros(shape=(nb_teams, nb_teams))
    elo_history = np.zeros(shape=(len(table),nb_teams))
    markov_history = np.zeros(shape=(len(table),nb_teams))

    for t, i in enumerate(table.index):
        game = table.iloc[i]
        teams = [team2id[game["Team 1"]], team2id[game["Team 2"]]]
        result = game["Result"]
        winner, loser = teams[result], teams[1-result]

        matrix[winner, loser] += 1
        markov_scores = markov_stationary(matrix.copy().T,alpha=0.99)

        elo_update(elo_scores, winner, loser)
        total_update(total_scores, winner, loser)

        elo_history[t,:] = elo_scores
        markov_history[t,:] = markov_scores

    write_html(table, elo_scores, total_scores, markov_scores)
    plot_history("elohistory.svg",    elo_history)
    plot_history("markovhistory.svg", markov_history)

def get_teams(table):
    teams = set()
    for t in table["Team 1"]:
        teams.add(t)
    for t in table["Team 2"]:
        teams.add(t)
    teams = sort(list(teams))
    return teams

if __name__ == '__main__':
    sns.set_style("white")
    sns.set_context("poster", font_scale=1.5, rc={"lines.linewidth": 2.5})
    
    # Read data
    table = pd.read_csv("results.csv")
    print("Read {} entries".format(len(table)))

    teams = get_teams(table)
    nb_teams = len(teams)
    team2id = {k : i for i,k in enumerate(teams)}
    id2team = {i : k for i,k in enumerate(teams)}

    compute_ranking()
