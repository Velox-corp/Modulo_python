# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
import webbrowser as wb
#Pues un algoritmo, que cosas no;
excel_trabajar = pd.read_excel("archivos/Copia-de-estres.xlsx")
y= excel_trabajar["quieresPaginaestres"]
X = excel_trabajar[["Edad","esunproblema","sintoma","combateestres","dominiointernet"]]
nombres_y = ["Si","No","Tal vez"]
nombres_X=X.columns.tolist()
x_train,x_test,y_train,y_test = train_test_split(X,y, test_size=0.15,  random_state=42)
arbolExperimental = tree.DecisionTreeClassifier(criterion='entropy',max_depth=5) #posiblemente con el criterion entropy salga mejor
arbolExperimental.fit(x_train, y_train)
arbolScoreTest = arbolExperimental.score(x_test, y_test)
arbolScoreTrain = arbolExperimental.score(x_train, y_train)
efectividadTest = round((arbolScoreTest*100),2)
efectividadTrain = round((arbolScoreTrain*100),2)
importancia = arbolExperimental.feature_importances_
#Documento para que amarre
with open('arbol/arbol_estres.dot', 'w') as dot:
    dot = tree.export_graphviz(arbolExperimental,
                               max_depth = 5,
                               out_file=dot,
                               class_names=nombres_y,
                               feature_names=nombres_X,
                               impurity=True,
                               rounded=True,
                               filled=True)
algoritmo = open("algoritmo.html","w")
mensaje = """<!DOCTYPE html>
    <html lang='es'>
    <head>
    <meta http-equiv="Content-Type" content="text/htmset=UTF-8">
    <link rel="icon" href="img/Logotipo.png" type="image/jpg" />
    <title>Módulo Python | Estadísticas Módulos</title>
    
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
                    <li class="nav-item-2 active">
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
                De acuerdo a los datos de nuestro proyecto del estrés, el algoritmo que más se acopla es el arból de desición, el cual se basa en 5 variables para determinar si a las personas les interesa o no la existencia de álguna página web referente al combate del estrés, ya que implica si nuestra página sería usada o no y por quiénes.
                    El algoritmo es un árbol de desición debido a que con este se pueden ejecutar diversas comparativas de condicionales, y a partir de estas determinar lo buscado. Las variables a considerar son:
                <br><br>
                <h5 class="sub">Edad</h5>
                <ul>
                    <li>La edad tiene un impacto en la desición, principalmente por que el algoritmo está orientado a los jóvenes, por lo que estos grupos son los de interés para el algoritmo y la aplicación de la que se deriva como tal</li>
                    <li>Esta variable tiene una relevancia en la desición de: <input class="form-control" type=text  size='4' value='"""+str(round(importancia[0]*100,2))+"""%' readonly='readonly'></li>
                </ul>
                <h5 class="sub">Si consideran que el estrés es un problema para la sociedad</h5>
                <ul>
                    <li>La percepción del problema es un factor muy importante, si no considera que es un problema o duda de su respuesta, este posiblemente no tenga interés</li>
                    <li>Esta variable tiene una relevancia en la desición de: <input class="form-control" type=text  size='4' value='"""+str(round(importancia[1]*100,2))+"""%' readonly='readonly'></li>
                </ul> 
                <h5 class="sub">El sintoma más asociado con el estrés</h5>
                <ul>
                  <li>Dependiendo de este el usuario podría ver de diferente manera el como debería manejar el estrés </li>
                  <li>Esta variable tiene una relevancia en la desición de: <input class="form-control" type=text  size='4' value='"""+str(round(importancia[2]*100,2))+"""%' readonly='readonly'></li>
                </ul>
                <h5 class="sub">Si consideran que es importante el combatir contra el estrés</h5>
                <ul>
                  <li>Ahora, si ellos son capaces de identificar la importancia del combate contra el estrés, y considerando el poco conocimiento, posiblemente tenga un mejor impacto la idea de la página web</li>
                  <li>Esta tiene una relevancia en la desición de: <input type=text class="form-control" size='4' value='"""+str(round(importancia[3]*100,2))+"""%' readonly='readonly'></li>
                </ul>
                <h5 class="sub">Manejo del internet</h5>
                <ul>
                  <li>El cómo maneja el internet una persona puede afectar en si ve viable una página del estrés, debido a como este se envuelve en el campo</li>
                  <li>Esta tiene una relevancia en la desición de: <input type=text class="form-control" size='4' value='"""+str(round(importancia[4]*100,2))+"""%' readonly='readonly'></li>
                </ul>
                <hr>
                <strong><h5 class="subi">Lo que se va mostrar de momento es una versión experimental del algoritmo</h5></strong><br>
                En teoría este dataframe tiene una certeza en los datos de prueba de: <input type='text' class="form-control" readonly='readonly' value='"""+str(efectividadTest)+"""%' size='5'> <br>
                En teoría este dataframe tiene una certeza en los datos de entrenamiento de: <input type='text' class="form-control" readonly='readonly' value='"""+str(efectividadTrain)+"""%' size='5'>
                <hr>
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
wb.open_new_tab("algoritmo.html")
