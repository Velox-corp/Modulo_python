# -*- coding: utf-8 -*-
# sitmonas, esunproblema, combateestres, dominiointernet, sexo, edad, quieresPaginaestres
import pandas as pd
import webbrowser as wb
preguntas = pd.read_excel("archivos/estres.xlsx")
#Parte de el entrenamiento
valores_finales = preguntas["quieresPaginaestres"]
y = valores_finales.value_counts()
x = y.index
x = list(x)
x
scriptTablaValoresFinalesX = ""
scriptTablaValoresFinalesYab = ""
scriptTablaValoresFinalesYrel = ""
i = 0
while(i <len(x)):
    if(i + 1 == len(x)):
        scriptTablaValoresFinalesX += "'"+str(x[i])+"'"
        scriptTablaValoresFinalesYab += str(y[i])
        scriptTablaValoresFinalesYrel += str(round(y[i]/len(valores_finales)*100,2))
    else:
        scriptTablaValoresFinalesX += "'"+str(x[i])+"',"
        scriptTablaValoresFinalesYab += str(y[i]) + ","
        scriptTablaValoresFinalesYrel += str(round(y[i]/len(valores_finales)*100,2)) +","
    i+= 1
#Pregunta dominio del internet
valores_dominio = preguntas["dominiointernet"]
y = valores_dominio.value_counts()
x = list(y.index)
scriptValoresDominioX = ""
scriptValoresDominioYab = ""
scriptValoresDominioYrel = ""
i = 0
while(i <len(x)):
    if(i + 1 == len(x)):
        scriptValoresDominioX += "'"+str(x[i])+"'"
        scriptValoresDominioYab += str(y[i])
        scriptValoresDominioYrel += str(round(y[i]/len(valores_dominio)*100,2))
    else:
        scriptValoresDominioX += "'"+str(x[i])+"',"
        scriptValoresDominioYab += str(y[i]) +","
        scriptValoresDominioYrel += str(round(y[i]/len(valores_dominio)*100,2)) + ","
    i+=1
    
#Edad
valores_edad = preguntas["Edad"]
y = valores_edad.value_counts()
x = y.index
x = list(x)
scriptValoresEdadX = ""
scriptValoresEdadYab = ""
scriptValoresEdadYrel = ""
i = 0
while(i <len(x)):
    if(i + 1 == len(x)):
        scriptValoresEdadX += "'"+str(x[i])+"'"
        scriptValoresEdadYab += str(y.iloc[i])
        scriptValoresEdadYrel += str(round(y.iloc[i]/len(valores_edad)*100,2))
    else:
        scriptValoresEdadX += "'"+str(x[i])+"',"
        scriptValoresEdadYab += str(y.iloc[i]) +","
        scriptValoresEdadYrel += str(round(y.iloc[i]/len(valores_edad)*100,2)) + ","
    i+=1
      
#De momento y ultimo combate
valores_Combate = preguntas["combateestres"]
y = valores_Combate.value_counts()
x = y.index
x = list(x)
scriptValoresCombateX = ""
scriptValoresCombateYab = ""
scriptValoresCombateYrel = ""
i = 0
while(i <len(x)):
    if(i + 1 == len(x)):
        scriptValoresCombateX += "'"+str(x[i])+"'"
        scriptValoresCombateYab += str(y.iloc[i])
        scriptValoresCombateYrel += str(round(y.iloc[i]/len(valores_edad)*100,2))
    else:
        scriptValoresCombateX += "'"+str(x[i])+"',"
        scriptValoresCombateYab += str(y.iloc[i]) +","
        scriptValoresCombateYrel += str(round(y.iloc[i]/len(valores_edad)*100,2)) + ","
    i+=1

estadisticas = open("estadisticas.html","w")
cuerpo = """ <!DOCTYPE html>
    <html lang='es'>
    <head>
    <meta http-equiv="Content-Type" content="text/htmset=UTF-8">
    <link rel="icon" href="img/Logotipo.png" type="image/jpg" />
    <title>Módulo Python | Estadisticas Módulos</title>
    
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script> 
        <link rel="stylesheet" type="text/css" href="node_modules/chartjs/dist/Chart.min.css">
        <script src="node_modules/chart.js/dist/Chart.js"></script><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
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
                    <li class="nav-item">
                        <a class="nav-link" href="index.html">HOME<span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="algoritmo.html">ALGORITMO</a>
                    </li>
                    <li class="nav-item-2 active">
                        <a class="nav-link" href="estadisticas.html">ESTADÍSTICAS</a>
                    </li>
                    <li class="nav-item">
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
                        <h1 class="display-2" style="margin-top: 3vw; font-family: 'Muli', sans-serif; color: #F8F9FA">Estadísticas de las variables</h1>
                    </div>
                </div>
            </div>
        </div>
        <div class="d">
            <article>
                Aquí se pretende mostrar las frecuencias de los elementos a considerar del entrenamiento del test para poder entender mejor que caracteristicas tienen mayor impacto en el algoritmo. 
            </article>
            <br>
            <div class='card container'>
                <div class='card-header'>
                    <h2 class='card-title'>Frecuencias del campo de prueba del objetivo: Si desean que exista la página para combatir el estrés<h2>
                    <h3 class='card-subtitle'>Cosa que es lo que nuestro algoritmo busca predecir</h3>
                </div>
                <div class='card-body'>
                    <canvas id='frecuencia_absoluta_objetivo'></canvas>
                    <br>
                    <canvas id='frecuencia_relativa_objetivo'></canvas>
                </div>
            </div>
            <hr>
            <div class='card container'>
                <div class='card-header'><h2 class='card-title'>Frecuencias del campo de prueba del objetivo: Analizar si el dominio del usuario en el internet afecta en la decisión<h2></div>
                <div class='card-body'>
                    <canvas id='frecuencia_absoluta_dominio'></canvas>
                    <br>
                    <canvas id='frecuencia_relativa_dominio'></canvas>
                </div>
            </div>
            <hr>
            <div class='card container'>
                <div class='card-header'><h2 class='card-title' style="color:#04D99D">Frecuencias del campo de prueba de entranemaineto: Ver el impacto de la edad<h2></div>
                <div class='card-body'>
                    <canvas id='frecuencia_absoluta_Edad'></canvas>
                    <br>
                    <canvas id='frecuencia_relativa_Edad'></canvas>
                </div>
            </div>
            <hr>
            <div class='card container'>
                <div class='card-header'><h2 class='card-title'>Frecuencias del campo de prueba del entrenamiento: Si creen que es importante combatir el estrés<h2></div>
                <div class='card-body'>
                    <canvas id='frecuencia_absoluta_Combate'></canvas>
                    <br>
                    <canvas id='frecuencia_relativa_Combate'></canvas>
                </div>
            </div>
            <hr>
            <div class='card container'>
                <div class='card-header'><h2 class='card-title'>Frecuencias del campo de prueba del entrenamiento: Síntoma más asociado al estrés<h2></div>
                <div class='card-body'>
                    <canvas id='frecuencia_absoluta_Sintoma'></canvas>
                    <br>
                    <canvas id='frecuencia_relativa_Sintoma'></canvas>
                </div>
            </div>
            <hr>
            <div class='card container'>
                <div class='card-header'><h2 class='card-title' style="color:#04D99D">Frecuencias del campo de prueba del entrenamiento: Si ven que el estrés es un problema para la sociedad<h2></div>
                <div class='card-body'>
                    <canvas id='frecuencia_absoluta_Sociedad'></canvas>
                    <br>
                    <canvas id='frecuencia_relativa_Sociedad'></canvas>
                </div>
            </div>
        <main>
        <script>
        var frecuencia_absoluta_objetivo =document.getElementById('frecuencia_absoluta_objetivo');
        var ab_objetivo= new Chart(frecuencia_absoluta_objetivo,{
        type:'bar',
        data:{
            labels:["""+scriptTablaValoresFinalesX+"""],
            datasets:[{
                    label:'Frecuencias Valores',
                    data: ["""+scriptTablaValoresFinalesYab+"""],
                    backgroundColor: ["rgb(4, 196, 217)","rgb(4, 217, 157)","#04D976"],
                    borderColor: ["rgb(4, 196, 217)","rgb(4, 217, 157)","#04D976"]
                    }
                    
            ]
        }, options: {
                        scales:{
                                xAxes:[{
                                        gridLines: {
                                            offsetGridLines: true
                                        }
                                }],
                                 yAxes: [{
                                        ticks: {
                                            beginAtZero: true
                                        }
                                    }]
                        }
                }
        });
        var frecuencia_relativa_objetivo =document.getElementById('frecuencia_relativa_objetivo');
            var rel_obj = new Chart(frecuencia_relativa_objetivo,{
            type:'pie',
            data:{
                labels:["""+scriptTablaValoresFinalesX+"""],
                datasets:[{
                        label:'Frecuencias Valores',
                        data: ["""+scriptTablaValoresFinalesYrel+"""],
                        backgroundColor: ["rgb(4, 196, 217)","rgb(4, 217, 157)","#04D976"],
                        borderColor: ["rgb(4, 196, 217)","rgb(4, 217, 157)","#04D976"]
                        }
                        
                ]
            }
            });
    
        var frecuencia_absoluta_dominio =document.getElementById('frecuencia_absoluta_dominio');
            var ab_dominio= new Chart(frecuencia_absoluta_dominio,{
            type:'bar',
            data:{
                labels:["""+scriptValoresDominioX+"""],
                datasets:[{
                        label:'Frecuencias Valores',
                        data: ["""+scriptValoresDominioYab+"""],
                        backgroundColor: ["#025159","#04ADBF","#04C4D9"],
                    borderColor: ["#025159","#04ADBF","#04C4D9"]
                        }
                        
                ]
            }, options: {
                            scales:{
                                    xAxes:[{
                                            gridLines: {
                                                offsetGridLines: true
                                            }
                                    }],
                                     yAxes: [{
                                            ticks: {
                                                beginAtZero: true
                                            }
                                        }]
                            }
                    }
            });
        var frecuencia_relativa_dominio =document.getElementById('frecuencia_relativa_dominio');
        var rel_dominio = new Chart(frecuencia_relativa_dominio,{
                type:'pie',
                data:{
                        labels:["""+scriptValoresDominioX+"""],
                        datasets:[{
                                label:'Frecuencias Valores',
                                data: ["""+scriptValoresDominioYrel+"""],
                    backgroundColor: ["#025159","#04ADBF","#04C4D9"],
                    borderColor: ["#025159","#04ADBF","#04C4D9"]
                                }
                        ]
                }
        });
    
        var frecuencia_absoluta_Edad =document.getElementById('frecuencia_absoluta_Edad');
        var ab_Edad= new Chart(frecuencia_absoluta_Edad,{
        type:'bar',
        data:{
            labels:["""+scriptValoresEdadX+"""],
            datasets:[{
                    label:'Frecuencias Valores',
                    data: ["""+scriptValoresEdadYab+"""],
                    backgroundColor: ["#1D5948","#025940","#03996F","#03A678","#04BF8A","#04D99D","#05E6A6","#05F2AF"],
                        borderColor: ["#1D5948","#025940","#03996F","#03A678","#04BF8A","#04D99D","#05E6A6","#05F2AF"]
                    }
                    
            ]
        }, options: {
                        scales:{
                                xAxes:[{
                                        gridLines: {
                                            offsetGridLines: true
                                        }
                                }],
                                 yAxes: [{
                                        ticks: {
                                            beginAtZero: true
                                        }
                                    }]
                        }
                }
        });
        var frecuencia_relativa_Edad =document.getElementById('frecuencia_relativa_Edad');
            var rel_Edad = new Chart(frecuencia_relativa_Edad,{
            type:'pie',
            data:{
                labels:["""+scriptValoresEdadX+"""],
                datasets:[{
                        label:'Frecuencias Valores',
                        data: ["""+scriptValoresEdadYrel+"""],
                        backgroundColor: ["#1D5948","#025940","#03996F","#03A678","#04BF8A","#04D99D","#05E6A6","#05F2AF"],
                        borderColor: ["#1D5948","#025940","#03996F","#03A678","#04BF8A","#04D99D","#05E6A6","#05F2AF"]
                        }
                        
                ]
            }
            });
    
        var frecuencia_absoluta_Combate =document.getElementById('frecuencia_absoluta_Combate');
            var ab_Combate= new Chart(frecuencia_absoluta_Combate,{
            type:'bar',
            data:{
                labels:["""+scriptValoresCombateX+"""],
                datasets:[{
                        label:'Frecuencias Valores',
                        data: ["""+scriptValoresCombateYab+"""],
                        backgroundColor: ["rgb(4, 196, 217)","rgb(4, 217, 157)"],
                    borderColor: ["rgb(4, 196, 217)","rgb(4, 217, 157)"]
                        }
                        
                ]
            }, options: {
                            scales:{
                                    xAxes:[{
                                            gridLines: {
                                                offsetGridLines: true
                                            }
                                    }],
                                     yAxes: [{
                                            ticks: {
                                                beginAtZero: true
                                            }
                                        }]
                            }
                    }
            });
        var frecuencia_relativa_Combate =document.getElementById('frecuencia_relativa_Combate');
        var rel_Combate = new Chart(frecuencia_relativa_Combate,{
                type:'pie',
                data:{
                        labels:["""+scriptValoresCombateX+"""],
                        datasets:[{
                                label:'Frecuencias Valores',
                                data: ["""+scriptValoresCombateYrel+"""],
                    backgroundColor: ["rgb(4, 196, 217)","rgb(4, 217, 157)"],
                    borderColor: ["rgb(4, 196, 217)","rgb(4, 217, 157)"]
                                }
                        ]
                }
        });
        var frecuencia_absoluta_Sintoma =document.getElementById('frecuencia_absoluta_Sintoma');
            var ab_dominio= new Chart(frecuencia_absoluta_Sintoma,{
            type:'bar',
            data:{
                labels:["Ansiedad","Dolor de cabeza","Depresión", "Neurosis"],
                datasets:[{
                        label:'Frecuencias Valores',
                        data: [{x:'Ansiedad', y:73, z:1},
                            {x:'Dolor de cabeza', y:37, z:2},
                            {x:'Depresion', y:5, z:3},
                            {x:'Neurosis', y:3, z:4},
                            
                                      ],
                        backgroundColor: ["#025159","#04ADBF","#04C4D9","#05CFE6"],
                    borderColor: ["#025159","#04ADBF","#04C4D9","#05CFE6"]
                        }
                        
                ]
            }, options: {
                            scales:{
                                    xAxes:[{
                                            gridLines: {
                                                offsetGridLines: true
                                            }
                                    }],
                                     yAxes: [{
                                            ticks: {
                                                beginAtZero: true
                                            }
                                        }]
                            }
                    }
            });
        var frecuencia_relativa_Sintoma =document.getElementById('frecuencia_relativa_Sintoma');
        var rel_dominio = new Chart(frecuencia_relativa_Sintoma,{
                type:'pie',
                data:{
                        labels:["Ansiedad","Dolor de cabeza","Depresión", "Neurosis"],
                        datasets:[{
                                label:'Frecuencias Valores',
                                data: ["61.86440678","31.355932199999998","4.237288136","2.542372881"],
                    backgroundColor: ["#025159","#04ADBF","#04C4D9","#05CFE6"],
                    borderColor: ["#025159","#04ADBF","#04C4D9","#05CFE6"]
                                }
                        ]
                }
        });
        var frecuencia_absoluta_Sociedad =document.getElementById('frecuencia_absoluta_Sociedad');
            var ab_dominio= new Chart(frecuencia_absoluta_Sociedad,{
            type:'bar',
            data:{
                labels:["Si","Tal vez","No"],
                datasets:[{
                        label:'Frecuencias Valores',
                        data: [{x:'Si', y:82, z:1},
                            {x:'Tal vez', y:30, z:2},
                            {x:'No', y:6, z:3},
                            
                                      ],
                        backgroundColor: ["#1D5948","#025940","#03996F"],
                    borderColor: ["#1D5948","#025940","#03996F"]
                        }
                        
                ]
            }, options: {
                            scales:{
                                    xAxes:[{
                                            gridLines: {
                                                offsetGridLines: true
                                            }
                                    }],
                                     yAxes: [{
                                            ticks: {
                                                beginAtZero: true
                                            }
                                        }]
                            }
                    }
            });
        var frecuencia_relativa_Sociedad =document.getElementById('frecuencia_relativa_Sociedad');
        var rel_dominio = new Chart(frecuencia_relativa_Sociedad,{
                type:'pie',
                data:{
                        labels:["Si","Tal vez","No"],
                        datasets:[{
                                label:'Frecuencias Valores',
                                data: ["69.49152542","25.42372881","5.084745763"],
                    backgroundColor: ["#1D5948","#025940","#03996F"],
                    borderColor: ["#1D5948","#025940","#03996F"]
                                }
                        ]
                }
        });
        </script>
        </div>
        <script src="js/JQuery.js" type="text/javascript"></script>
        <link href="css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <link href="css/estilos.css" rel="stylesheet" type="text/css"/>
    </body>
    </html>
"""
estadisticas.write(cuerpo)
estadisticas.close()
wb.open_new_tab("estadisticas.html")
