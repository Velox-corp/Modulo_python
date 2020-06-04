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
                <p>Y de manera básica, nosotros usando python pretendemos crear un algoritmo con el cual se puede predecir <strong>TAL COSA QUE NO SE AÚN</strong>, a partir de:
                    <ul>
                        <li>Creo que usaremos edad</li>
                        <li>Creo que usaremos  el sexo</li>
                        <li>No se que más usaremos</li>
                    </ul>    
                </p>
                <p>
                    Nosotros usaremos un Algóritmo del tipo <strong>Inserte tipo algoritmo</strong> debido a que este no permite <strong>{}</strong>.
                </p>
            </article>
            <div class='btn-group'>
            <a class='btn btn-primary' href='estadisticas.html'>Ver información de los datos de entrenamiento</a> <br>
            <a class='btn btn-primary' href='algoritmo.html'>Ver el algoritmo</a>
            </div>
        <main>
        <footer>
        </footer>
    </body>
    <html>
"""
acheteemeele.write(cuerpo)
acheteemeele.close()

