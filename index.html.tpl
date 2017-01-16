<!DOCTYPE html>

<html lang="en">

<head>
    <title>Ranking</title>
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

</head>
 
<body>
 
    <div class="container-fluid">
        <div class="header">
            <h3 class="text-muted">Live Ranking: Abschlusspräsentation Rating und Ranking</h3>
            <p>Letzte Aktualisierung: {}</p>
        </div>
 
        <div class="row-fluid"> 
            <div class="col-md-3">
                <h4><span class="glyphicon glyphicon-refresh" aria-hidden="true"></span> Live Ticker</h4>
                {}
            </div>
            

            <div class="col-md-7">
                <div class="row-fluid">
                    <div class="col-md-12">
                        <h4><span class="glyphicon glyphicon-tasks" aria-hidden="true"></span> Elo Verlauf</h4>
 
                        <div class="row-fluid">
                            <div class="col-md-8">
                                <img src="elohistory.svg" height="300px">
                            </div>

                            <div class="col-md-4">
                                {}
                                <p class="text-muted"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span> Elo-Scores. Start bei 1200</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row-fluid">
                    <div class="col-md-12">
                        <h4><span class="glyphicon glyphicon-sort-by-order" aria-hidden="true"></span> Markov Verlauf</h4>
                        <div class="row-fluid">
                            <div class="col-md-8">
                                <img src="markovhistory.svg" height="300px">
                            </div>
                            <div class="col-md-4">
                                {}
                                <p class="text-muted"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span> Gewinnwahrscheinlichkeiten für jedes Team (in Prozent)</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-md-2">
                <h4><span class="glyphicon glyphicon-sort-by-order" aria-hidden="true"></span> Gesamtpunkte</h4>
                {}
                <p class="text-muted"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span> Sieg: +1 Punkt, Niederlage: -1 Punkt</p>
            </div>
        </div>
    </div>
    <footer class="footer">
        <div class="container-fluid">
            <p class="text-muted">Studienstifung Winterakademie Davos 2017</p>
        </div>
    </footer>
</body>
 
</html>
