import webbrowser as wb
acheteemeele = open("index.html","w")
cuerpo = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/htmset=UTF-8">
    <title>Módelo Python | Home</title>
    <link rel="icon" href="img/Logotipo.png" type="image/jpg" />
    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script> 
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
	<script src="https://use.fontawesome.com/releases/v5.0.8/js/all.js"></script>
	<link href="css/slider.css" rel="stylesheet">
       
    </head>
    <body style="background-color:  #F8F9FA">
        <nav class="navbar navbar-expand-md navbar-info bg-info navbar-hover fixed-top" style="color: rgba(0,0,0,.9); font-family:'Open Sans', sans-serif; font-size: 11px;">
            <a class="navbar-brand" href="index.html"><img src="img/Logotipo.png" class="hover" style="height: 40px; width: 40px; border-radius:50%"></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHover" aria-controls="navbarDD" aria-expanded="false" aria-label="Navigation" style="background: #24A5BA">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarHover">
                <ul class="navbar-nav">
                    <li class="nav-item-2 active">
                        <a class="nav-link" href="index.html">HOME<span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="algoritmo.html">ALGORITMO</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="estadisticas.html">ESTADÍSTICAS</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="arbol.html">ÁRBOL DE DECISIÓN</a>
                    </li>
                </ul>
            </div>
        </nav>
        <div id="slides" class="carousel slide" data-ride="carousel">
            <ul class="carousel-indicators">
                <li data-target="#slides" data-slide-to="0" class="active"></li>
                <li data-target="#slides" data-slide-to="1"></li>
                <li data-target="#slides" data-slide-to="2"></li>
            </ul>
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="img/2.jpg">
                    <div class="carousel-caption">
                        <h1 class="display-2" style="margin-top: 5vw; font-family: 'Muli', sans-serif; color: #F8F9FA">VELOX</h1>
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="img/4.jpg" alt="">
                    <div class="carousel-caption">
                        <h1 class="display-2"  style="margin-top: 20vw"></h1>
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="img/3.jpg" alt="">
                    <div class="carousel-caption">
                        <h1 class="display-2" style="margin-top: 20vw"></h1>
                    </div>
                </div>
            </div>
        </div>
        <div class="d">
            
        </div> 
        <footer style="background-color: #04C4D9">
        </footer>
        <script src="js/JQuery.js" type="text/javascript"></script>
        <link href="css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <link href="css/estilos.css" rel="stylesheet" type="text/css"/>
    </body>
    </html>
"""
acheteemeele.write(cuerpo)
acheteemeele.close()
wb.open_new_tab("index.html")
