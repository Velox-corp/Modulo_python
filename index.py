# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
acheteemeele = open("index.html","w")
cuerpo = """
    <!DOCTYPE html>
    <html lang='es'>
    <head>
    <meta charset='utf-8'>
    <title>Modulo de python osiosi</title>
    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script> 
       
    </head>
    <body class='container-fluid'>
        <header class='bg-primary text-center'>
            <h1>Proyecto del estrés</h1>
        </header>
        <main>
            <article class='' id='descripcion'>
                <h2>Descripcion</h2>
                <p>
                Nuesto modulo se crea a partir del estrés del que los alumnos sufren, donde nostros en nuestro PA buscamos dar un metodo de comunicaión entre alumnos y psicologos para que puedan cambatir el estrés.
                </p>
                <p>Y de manera básica, nosotros usando python pretendemos crear un algoritmo con el cual se puede predecir <strong>SI a un alumno le interesa la existencía de una página web que le sirva como una herraienta para combatir el estrés con ayuda de un psicologo</strong>.</p>
                <p>{Insertar información sobre shiee}</p>
                <p>
                    Nosotros usaremos un Algóritmo del tipo <strong>árbol de desición</strong> debido a que este nos permite determinar el estado final d eun objeto a partir de condicionales, cosa que resulta muy util en variables que no son númericas como tal, pese a que se manejan así. 
                </p>
            </article>
            <div class='btn-group text-center flex'>
            <a class='btn btn-primary' href='estadisticas.html'>Ver información de los datos de entrenamiento</a> |--| <a class='btn btn-primary' href='algoritmo.html'>Ver el algoritmo</a>
            </div>
        <main>
        <footer>
        </footer>
    </body>
    <html>
"""
acheteemeele.write(cuerpo)
acheteemeele.close()

