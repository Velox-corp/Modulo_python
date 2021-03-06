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
        <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>
        <script src='http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js'></script>
        <script src='http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js'></script> 
        <script src="js/OrgChart.js"></script>
        <script src='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js' integrity='sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM' crossorigin='anonymous'></script>	
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
                        <h1 class="display-2" style="margin-top: 5vw; font-family: 'Muli', sans-serif; color: #F8F9FA">Árbol De Decisión</h1>
                    </div>
                </div>
            </div>
        </div>
        <div class="d">
            <div id="tree"></div>
        <script src='css/estilo.css'></script>
        <style type="text/css"> 
            
          [link-id] path {
               stroke: #0396A6;
          }
              
          [node-id='1'] rect {
                fill: #05CFE6;
          }
        
          [node-id='2'] rect {
                fill: #05CFE6;
          }
        
          [node-id='3'] rect {
                fill: #04BF8A;
          }
        
          [node-id='4'] rect {
                fill: #04C4D9;
          }
        
          [node-id='5'] rect {
                fill: #04BF8A;
          }
        
          [node-id='6'] rect {
                fill: #04BF8A;
          }
        
          [node-id='7'] rect {
                fill: #025159;
          }
        
          [node-id='8'] rect {
                fill: #04C4D9;
          }
        
          [node-id='9'] rect {
                fill: #025159;
          }
        
          [node-id='10'] rect {
                fill: #04BF8A;
          }
        
          [node-id='11'] rect {
                fill: #0D0D0D;
          }
        
          [node-id='12'] rect {
                fill: #03996F;
          }
        
          [node-id='13'] rect {
                fill: #04BF8A;
          }
        
          [node-id='14'] rect {
                fill: #04C4D9;
          }
          [node-id='15'] rect {
                fill: #04ADBF;
          }
        
          [node-id='16'] rect {
                fill: #0D0D0D;
          }
        
          [node-id='17'] rect {
                fill: #025940;
          }
        
          [node-id='18'] rect {
                fill: #025940;
          }
        
          [node-id='19'] rect {
                fill: #025159;
          }
        
          [node-id='20'] rect {
                fill: #025940;
          }
        
          [node-id='21'] rect {
                fill: #03996F;
          }
        
          [node-id='22'] rect {
                fill: #0D0D0D;
          }
        
          [node-id='23'] rect {
                fill: #04BF8A;
          }
        
          [node-id='24'] rect {
                fill: #04ADBF;
          }
        
          [node-id='25'] rect {
                fill: #04C4D9;
          }
              
          [node-id='26'] rect {
                fill: #04ADBF;
          }
        
          [node-id='27'] rect {
                fill: #0D0D0D;
          }
        
          [node-id='28'] rect {
                fill: #05F240;
          }
        
          [node-id='29'] rect {
                fill: #04D99D;
          }
        
          [node-id='30'] rect {
                fill: #025940;
          }
        
          [node-id='31'] rect {
                fill: #04D99D;
          }
        
          [node-id='32'] rect {
                fill: #025940;
          }
        
          [node-id='33'] rect {
                fill: #05F240;
          }
        
          [node-id='34'] rect {
                fill: #04D99D;
          }
        
          [node-id='35'] rect {
                fill: #025940;
          }
        
          [control-expcoll-id] circle {
            fill: #0396A6;
          }
        
          .bg-search-table {
              background-color: #0396A6 !important;
          }
        
          .bg-search-table input {
            background-color: #0396A6 !important;
          }
        
          .bg-ripple-container {
            background-color: #0396A6;
          }
        
          div.edit-fields {
            background-color: #0396A6;
          }
              
          input {
            margin: 0;
            font-family: inherit;
            font-size: inherit;
            line-height: inherit;
            pointer-events: none;
            background-color: #04D99D;
            color: black;
            border-radius: 10px;
        }
        </style>
        <script>
         
         OrgChart.templates.derek.field_0 = '<text class="field_0"  style="font-size: 14px;" fill="#ffffff" x="120" y="20" text-anchor="middle">{val}</text>';
         OrgChart.templates.derek.field_1 = '<text class="field_1"  style="font-size: 14px;" fill="#ffffff" x="120" y="40" text-anchor="middle">{val}</text>';
         OrgChart.templates.derek.field_2 = '<text class="field_2"  style="font-size: 14px;" fill="#ffffff" x="120" y="60" text-anchor="middle">{val}</text>';
         OrgChart.templates.derek.field_3 = '<text class="field_3"  style="font-size: 14px;" fill="#ffffff" x="120" y="80" text-anchor="middle">{val}</text>'; 
         OrgChart.templates.derek.field_4 = '<text class="field_4"  style="font-size: 14px;" fill="#ffffff" x="120" y="100" text-anchor="middle">{val}</text>';
         OrgChart.templates.derek.field_5 = '<text class="field_5"  style="font-size: 22px; font-family: Impact;" fill="#0396A6" x="120" y="-20" text-anchor="middle">{val}</text>';
        
         var chart = new OrgChart(document.getElementById("tree"), {
                mouseScrool: OrgChart.action.none,
            template: "derek",
            enableSearch: true,
            nodeBinding: {
              field_0: "caracteristica",
              field_1: "entropy",
              field_2: "samples",
              field_3: "value",
              field_4: "class",
              field_5: "tf"
            },
            nodes: [
                { id: 1, caracteristica: "combateestres <= 2.0", entropy: "entropy = 1.174", samples: "samples = 100", value: "value = [66, 7, 27]", class: "class = Si"},
                { id: 2, pid: 1, tf: "TRUE", caracteristica: "Edad <= 17.5", entropy: "entropy = 1.059", samples: "samples = 86", value: "value = [63, 6, 17]", class: "class = Si"},
                { id: 3, pid: 1, tf: "FALSE", caracteristica: "dominiointernet <= 2.5", entropy: "entropy = 1.095", samples: "samples = 14", value: "value = [3, 1, 10]", class: "class = Tal vez"},
                { id: 4, pid: 2, caracteristica: "sintoma <= 2.5", entropy: "entropy = 0.874", samples: "samples = 77", value: "value = [62, 4, 11]", class: "class = Si"},
                { id: 5, pid: 2, caracteristica: "Edad <= 19.5", entropy: "entropy = 1.224", samples: "samples = 9", value: "value = [1, 2, 6]", class: "class = Tal vez"},
                { id: 6, pid: 3, caracteristica: "esunproblema <= 1.5", entropy: "entropy = 0.991", samples: "samples = 13", value: "value = [2, 1, 10]", class: "class = Tal vez"},
                { id: 7, pid: 3, entropy: "entropy = 0.0", samples: "samples = 1", value: "value = [1, 0, 0]", class: "class = Si"},
                { id: 8, pid: 4, caracteristica: "Edad <= 16.5", entropy: "entropy = 0.929", samples: "samples = 70", value: "value = [55, 4, 11]", class: "class = Si"},
                { id: 9, pid: 4, entropy: "entropy = 0.0", samples: "samples = 7", value: "value = [7, 0, 0]", class: "class = Si"},
                { id: 10, pid: 5, caracteristica: "esunproblema <= 1.5", entropy: "entropy = 0.863", samples: "samples = 7", value: "value = [0, 2, 5]", class: "class = Tal vez"},
                { id: 11, pid: 5, caracteristica: "esunproblema <= 2.0", entropy: "entropy = 1.0", samples: "samples = 2", value: "value = [1, 0, 1]", class: "class = Si"},
                { id: 12, pid: 6, caracteristica: "Edad <= 15.5", entropy: "entropy = 0.592", samples: "samples = 7", value: "value = [1, 0, 6]", class: "class = Tal vez"},
                { id: 13, pid: 6, caracteristica: "esunproblema <= 2.5", entropy: "entropy = 1.252", samples: "samples = 6", value: "value = [1, 1, 4]", class: "class = Tal vez"},
                { id: 14, pid: 8, caracteristica: "Edad <= 15.5",entropy: "entropy = 0.919", samples: "samples = 53", value: "value = [41, 2, 10]", class: "class = Si"},
                { id: 15, pid: 8, caracteristica: "esunproblema <= 2.5", entropy: "entropy = 0.834", samples: "samples = 17", value: "value = [14, 2, 1]", class: "class = Si"},
                { id: 16, pid: 10, caracteristica: "sintoma <= 1.5", entropy: "entropy = 1.0", samples: "samples = 4", value: "value = [0, 2, 2]", class: "class = No"},
                { id: 17, pid: 10, entropy: "entropy = 0.0", samples: "samples = 3", value: "value = [0, 0, 3]", class: "class = Tal vez"},
                { id: 18, pid: 11, entropy: "entropy = 0.0", samples: "samples = 1", value: "value = [0, 0, 1]", class: "class = Tal vez"},
                { id: 19, pid: 11, entropy: "entropy = 0.0", samples: "samples = 1", value: "value = [1, 0, 0]", class: "class = Si"},
                { id: 20, pid: 12, entropy: "entropy = 0.0", samples: "samples = 2", value: "value = [0, 0, 2]", class: "class = Tal vez"},
                { id: 21, pid: 12, caracteristica: "sintoma <= 1.5", entropy: "entropy = 0.722", samples: "samples = 5", value: "value = [1, 0, 4]", class: "class = Tal vez"},
                { id: 22, pid: 13, caracteristica: "Edad <= 16.5", entropy: "entropy = 1.0", samples: "samples = 2", value: "value = [0, 1, 1]", class: "class = No"},
                { id: 23, pid: 13, caracteristica: "sintoma <= 1.5", entropy: "entropy = 0.811", samples: "samples = 4", value: "value = [1, 0, 3]", class: "class = Tal vez"},
                { id: 24, pid: 14, entropy: "entropy = 0.65", samples: "samples = 6", value: "value = [5, 1, 0]", class: "class =Si"},
                { id: 25, pid: 14, entropy: "entropy = 0.888", samples: "samples = 47", value: "value = [36, 1, 10]", class: "class = Si"},
                { id: 26, pid: 15, entropy: "entropy = 0.567", samples: "samples = 15", value: "value = [13, 2, 0]", class: "class = Si"},
                { id: 27, pid: 15, entropy: "entropy = 1.0", samples: "samples = 2", value: "value = [1, 0, 1]", class: "class = Si"},
                { id: 28, pid: 16, entropy: "entropy = 0.0", samples: "samples = 1", value: "value = [0, 1, 0]", class: "class = No"},
                { id: 29, pid: 16, entropy: "entropy = 0.918", samples: "samples = 3", value: "value = [0, 1, 2]", class: "class = Tal vez"},
                { id: 30, pid: 21, entropy: "entropy = 0.0", samples: "samples = 2", value: "value = [0, 0, 2]", class: "class = Tal vez"},
                { id: 31, pid: 21, entropy: "entropy = 0.918", samples: "samples = 3", value: "value = [1, 0, 2]", class: "class = Tal vez"},
                { id: 32, pid: 22, entropy: "entropy = 0.0", samples: "samples = 1", value: "value = [0, 0, 1]", class: "class = Tal vez"},
                { id: 33, pid: 22, entropy: "entropy = 0.0", samples: "samples = 1", value: "value = [0, 1, 0]", class: "class = No"},
                { id: 34, pid: 23, entropy: "entropy = 0.918", samples: "samples = 3", value: "value = [1, 0, 2]", class: "class = Tal vez"},
                { id: 35, pid: 23, entropy: "entropy = 0.0", samples: "samples = 1", value: "value = [0, 0, 1]", class: "class = Tal vez"}
              ]
            });  
        </script>
        
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
        <script src="js/JQuery.js" type="text/javascript"></script>
        <link href="css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <link href="css/estilos.css" rel="stylesheet" type="text/css"/>
    </body>
    </html>
"""
algoritmo.write(mensaje)
algoritmo.close()
wb.open_new_tab("arbol.html")
