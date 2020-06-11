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
    <title>Estadisticas modulos</title>
    
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
        
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script> 
        
        <link rel="stylesheet" type="text/css" href="node_modules/chartjs/dist/Chart.min.css">
    
        <script src="node_modules/chart.js/dist/Chart.js"></script>
    </head>
    <body class='container-fluid'>
        <main>
            <h1 class='text-center bg-primary'>Estadisticas de las variables </h1>
            <hr>
            <article>
                Aquí se pretende mostrar las frecuencias de los elementos a considerar del entrenamiento del test para poder entender mejor que caracteristicas tienen mayor impacto en el algoritmo. 
            </article>
            <br>
            <div class='card container'>
                <div class='card-header'>
                    <h2 class='card-title'>Frecuencias del campo de prueba del objetivo: si desean que exista la página para combatir el estrés<h2>
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
                <div class='card-header'><h2 class='card-title'>Frecuencias del campo de prueba de entranemaineto: ver el impacto de la edad<h2></div>
                <div class='card-body'>
                    <canvas id='frecuencia_absoluta_Edad'></canvas>
                    <br>
                    <canvas id='frecuencia_relativa_Edad'></canvas>
                </div>
            </div>
            <hr>
            <div class='card container'>
                <div class='card-header'><h2 class='card-title'>Frecuencias del campo de prueba del entrenamiento: si creen que es importante combatir el estrés<h2></div>
                <div class='card-body'>
                    <canvas id='frecuencia_absoluta_Combate'></canvas>
                    <br>
                    <canvas id='frecuencia_relativa_Combate'></canvas>
                </div>
            </div>
            <hr>
            <a href='index.html' class=' btn btn-primary'>Regresar al index</a>
        <main>
        <script>
        var frecuencia_absoluta_objetivo =document.getElementById('frecuencia_absoluta_objetivo');
        var ab_objetivo= new Chart(frecuencia_absoluta_objetivo,{
        type:'bar',
        data:{
            labels:["""+scriptTablaValoresFinalesX+"""],
            datasets:[{
                    label:'Frecuencias valores',
                    data: ["""+scriptTablaValoresFinalesYab+"""],
                    backgroundColor: ["rgb(255,60,30)","rgb(30,255,60)","rgb(60,20,255)"],
                    borderColor: ["rgb(255,60,30)","rgb(30,255,60)","rgb(60,20,255)"]
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
                        label:'Frecuencias valores',
                        data: ["""+scriptTablaValoresFinalesYrel+"""],
                        backgroundColor: ["rgb(255,60,30)","rgb(30,255,60)","rgb(60,20,255)"],
                        borderColor: ["rgb(255,60,30)","rgb(30,255,60)","rgb(60,20,255)"]
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
                        label:'Frecuencias valores',
                        data: ["""+scriptValoresDominioYab+"""],
                        backgroundColor: ["rgb(255,255,60)","rgb(255,60,30)","rgb(60,255,30)"],
                        borderColor: ["rgb(255,255,60)","rgb(255,60,30)","rgb(60,255,30)"]
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
                                label:'Frecuencias valores',
                                data: ["""+scriptValoresDominioYrel+"""],
                    backgroundColor: ["rgb(255,255,60)","rgb(255,60,30)","rgb(60,255,30)"],
                    borderColor: ["rgb(255,255,60)","rgb(255,60,30)","rgb(60,255,30)"]
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
                    label:'Frecuencias valores',
                    data: ["""+scriptValoresEdadYab+"""],
                    backgroundColor: ["rgb(200,60,30)","rgb(200,60,60)","rgb(200,90,60)","rgb(200,90,90)","rgb(200,120,90)","rgb(200,120,120)","rgb(200,150,120)","rgb(200,150,150)"],
                    borderColor: ["rgb(200,60,30)","rgb(200,60,60)","rgb(200,90,60)","rgb(200,90,90)","rgb(200,120,90)","rgb(200,120,120)","rgb(200,150,120)","rgb(200,150,150)"]
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
                        label:'Frecuencias valores',
                        data: ["""+scriptValoresEdadYrel+"""],
                        backgroundColor: ["rgb(200,60,30)","rgb(200,60,60)","rgb(200,90,60)","rgb(200,90,90)","rgb(200,120,90)","rgb(200,120,120)","rgb(200,150,120)","rgb(200,150,150)"],
                        borderColor: ["rgb(200,60,30)","rgb(200,60,60)","rgb(200,90,60)","rgb(200,90,90)","rgb(200,120,90)","rgb(200,120,120)","rgb(200,150,120)","rgb(200,150,150)"]
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
                        label:'Frecuencias valores',
                        data: ["""+scriptValoresCombateYab+"""],
                        backgroundColor: ["rgb(30,255,200)","rgb(60,255,130)","rgb(255,130,130)"],
                    borderColor: ["rgb(30,255,200)","rgb(60,255,130)","rgb(255,130,130)"]
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
                                label:'Frecuencias valores',
                                data: ["""+scriptValoresCombateYrel+"""],
                    backgroundColor: ["rgb(30,255,200)","rgb(60,255,130)","rgb(255,130,130)"],
                    borderColor: ["rgb(30,255,200)","rgb(60,255,130)","rgb(255,130,130)"]
                                }
                        ]
                }
        });
        </script>
    </body>
    </html>
"""
estadisticas.write(cuerpo)
estadisticas.close()
wb.open_new_tab("estadisticas.html")
