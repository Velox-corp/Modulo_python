# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:43:27 2020

@author: maste
"""
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
import webbrowser as wb
#Pues un algoritmo, que cosas no;
excel_trabajar = pd.read_excel("Copia-de-estres.xlsx")
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
with open('arbol_estres.dot', 'w') as dot:
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
    <meta charset='utf-8'>
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
            <h1 class='text-center  bg-primary container-fluid'>Detalles del Algortimo</h1><hr>
            <article>
                Nuestro algoritmo, es un arból de desición vasado en 5 variables para determinar si a las personas les interesaría o no la existencia de álguna página web referente al combate del estrés, ya que implica si nuestra página sería usada o no y por quienes. Las variables a considerar son:
                    El algoritmo es un árbol de desición debido a que con este se pueden ejecutar diversas comparativas de condicionales, y a partir de estas determinar lo buscado.
                <br>
                <ul>
                    <li>Edad: 
                        <ul>
                            <li>La edad tiene un impacto en la desición, principalmente por que el algoritmo está orientado a los jovenes, por lo que estos grupos son los de interés para el algoritmo y la palicación de la que se deriva como tal</li>
                            <li>Esta variable tiene una relevancia en la desición de: <input type=text  size='4' value='"""+str(round(importancia[0]*100,2))+"""%' readonly='readonly'></li>
                        </ul>
                    </li>
                    <li>Si consideran que el estés es un problema para la sociedad: 
                        <ul>
                            <li>La percepción del problema es un factor muy importante, si no considera que es un problema o duda de su respuesta, este posiblemente no tenga interes</li>
                            <li>Esta variable tiene una relevancia en la desición de: <input type=text  size='4' value='"""+str(round(importancia[1]*100,2))+"""%' readonly='readonly'></li>
                        </ul>    
                    </li>
                    <li>El sintoma más asociado con el estrés: 
                        <ul>
                            <li>dependiendo de este el usuario podría ver de diferente manera el como debería manejar el estrés </li>
                            <li>Esta variable tiene una relevancia en la desición de: <input type=text  size='4' value='"""+str(round(importancia[2]*100,2))+"""%' readonly='readonly'></li>
                        </ul>
                    </li>
                    <li>Si consideran que es importante el cambate contra el estrés:
                        <ul>
                            <li>Ahora, si ellos son capaces de identificar la importancia del combate contrá el estrés, y considerando el poco conocimiento, posiblemente tenga un mejor impacto la idea de la página web</li>
                            <li>Esta tiene una relevancia en la desición de: <input type=text  size='4' value='"""+str(round(importancia[3]*100,2))+"""%' readonly='readonly'></li>
                        </ul>
                    </li>
                    <li>Manejo del internet:
                        <ul>
                            <li>El como maneja el internet una persona puede afectar en si ve viable una página del estrés, debido a como este se envuelve en el campo</li>
                            <li>Esta tiene una relevancia en la desición de: <input type=text  size='4' value='"""+str(round(importancia[4]*100,2))+"""%' readonly='readonly'></li>
                        </ul>
                    </li>
                </ul>
                <hr>
                <strong>Lo que se va mostrar de momento es una versión experimental del algoritmo</strong><br>
                En teoría este dataframe tiene una certeza en los datos de prueba de: <input type='text' readonly='readonly' value='"""+str(efectividadTest)+"""%' size='5'> <br>
                En teoría este dataframe tiene una certeza en los datos de entrenamiento de: <input type='text' readonly='readonly' value='"""+str(efectividadTrain)+"""%' size='5'>
                <hr>
                <a href='index.html' class='btn btn-primary'>Regresar al index.</a>
            </article>
        <main>
    </body>
    </html>
"""
algoritmo.write(mensaje)
algoritmo.close()
wb.open_new_tab("algoritmo.html")