# -*- coding: utf-8 -*-
import pandas as pd
import webbrowser as wb

algoritmo = open("arbol.html","w")
mensaje = """<!DOCTYPE html>
    <html lang='es'>
    <head>
    <meta http-equiv="Content-Type" content="text/htmset=UTF-8">
    <link rel="icon" href="img/Logotipo.png" type="image/jpg" />
    <title>Módulo Python | Árbol De Decisión</title>
    
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script> 
        <link rel="stylesheet" type="text/css" href="node_modules/chartjs/dist/Chart.min.css">
        <link href="css/slider.css" rel="stylesheet">
    
        <script src="node_modules/chart.js/dist/Chart.js"></script>
    </head>
    <body style="background-color:  #F8F9FA">
        <nav class="navbar navbar-expand-md navbar-info bg-info navbar-hover fixed-top" style="color: rgba(0,0,0,.9); font-family:'Open Sans', sans-serif; font-size: 11px;">
            <a class="navbar-brand" href="index.html"><img src="img/Logotipo.png" class="hover" style="height: 40px; width: 40px; border-radius:50%"></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHover" aria-controls="navbarDD" aria-expanded="false" aria-label="Navigation" style="background: #24A5BA">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarHover">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="index.html">HOME<span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="algoritmo.html">ALGORITMO</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="estadisticas.html">ESTADÍSTICAS</a>
                    </li>
                    <li class="nav-item-2 active">
                        <a class="nav-link" href="arbol.html">ÁRBOL DE DECISIÓN</a>
                    </li>
                </ul>
            </div>
        </nav>
        <div id="slides" class="carousel slide" data-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="img/1.jpg">
                    <div class="carousel-caption">
                        <h1 class="display-2" style="margin-top: 5vw; font-family: 'Muli', sans-serif; color: #F8F9FA">Detalles del Algoritmo</h1>
                    </div>
                </div>
            </div>
        </div>
        <div class="d">
            <article>
                
            </article>
        </div>
        <script src="js/JQuery.js" type="text/javascript"></script>
        <link href="css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <link href="css/estilos.css" rel="stylesheet" type="text/css"/>
    </body>
    </html>
"""
algoritmo.write(mensaje)
algoritmo.close()
wb.open_new_tab("arbol.html")