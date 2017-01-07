<!DOCTYPE html>

<html lang="en">

<head>
    <title>Ranking</title>
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="bootstrap.min.css" rel="stylesheet">
    <link href="design.css" rel="stylesheet">

</head>
 
<body>
 
    <div class="container-fluid">
        <div class="header">
            <h3 class="text-muted">Live Ranking</h3>
            <p>Letzte Aktualisierung: {}</p>
        </div>
 
        <div class="row marketing">
            <div class="col-md-3">
                <h4><span class="glyphicon glyphicon-refresh" aria-hidden="true"></span> Live Ticker</h4>
                {}
            </div>

            <div class="col-md-7">
                <div class="container">
                    <h4><span class="glyphicon glyphicon-tasks" aria-hidden="true"></span> Elo Verlauf</h4>
                    <div class="col-md-5">
                        <img src="elohistory.svg" height="300px">
                    </div>

                    <div class="col-md-2">
                        {}
                    </div>
                </div>

                <div class="container">
                    <h4><span class="glyphicon glyphicon-sort-by-order" aria-hidden="true"></span> Markov Verlauf</h4>
                    <div class="col-md-5">
                        <img src="markovhistory.svg" height="300px">
                    </div>

                    <div class="col-md-2">
                        {}
                    </div>
                </div>
            </div>

            <div class="col-md-2">
                <h4><span class="glyphicon glyphicon-sort-by-order" aria-hidden="true"></span> Gesamtpunkte</h4>
                {}
            </div>

        </div>

        <footer class="footer">
            <p>Studienstifung Winterakademie 2017</p>
        </footer>
 
    </div>
</body>
 
</html>
