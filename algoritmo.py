# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:43:27 2020

@author: maste
"""
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import webbrowser as wb
#Pues un algoritmo, que cosas no;
excel_trabajar = pd.read_excel("Copia-de-estres.xlsx")
y= excel_trabajar["quieresPaginaestres"]
X = excel_trabajar[["Edad", "Sexo","combateestres","dominiointernet"]]
x_train,x_test,y_train,y_test = train_test_split(X,y, test_size=0.19,  random_state=4)
arbolExperimental = DecisionTreeClassifier(max_depth=3)
arbolExperimental.fit(x_train, y_train)
arbolScoreTest = arbolExperimental.score(x_test, y_test)
arbolScoreTrain = arbolExperimental.score(x_train, y_train)
print(arbolScoreTest)
print(arbolScoreTrain)
efectividadTest = round((arbolScoreTest*100),2)
efectividadTrain = round((arbolScoreTrain*100),2)
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
            <h1 class='text-center container-fluid'>Detalles del Algortimo</h1>
            <article>
                Nuestro algoritmo, es un arból de desición vasado en 4 variables para determinar si a las personas les interesaría o no la existencia de álguna página web referente al combate del estrés, ya que implica si nuestra página sería usada o no y por quienes. Las variables a considerar son:
                <ul>
                    <li>Edad</li>
                    <li>Manejo del internet</li>
                    <li>Si consideran que es importante el cambate contra el estrés</li>
                    <li>Sexo</li>
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