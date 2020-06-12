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
                        <h1 class="display-2" style="margin-top: 5vw; font-family: 'Muli', sans-serif; color: #F8F9FA">DETALLES</h1>
                        <a href="estadisticas.html"><button type="button" class="btn btn-primary btn-lg" style="margin-right: 8vw">VER</button></a>
                    </div>
                </div>
                <div class="carousel-item">
                    <img src="img/3.jpg" alt="">
                    <div class="carousel-caption">
                        <h1 class="display-2" style="margin-top: 5vw; font-family: 'Muli', sans-serif; color: #F8F9FA">NUESTRO ALGORITMO</h1>
                        <a href="arbol.html"><button type="button" class="btn btn-primary btn-lg" style="margin-right: 8vw">VER</button></a>
                    </div>
                </div>
            </div>
        </div>
        <div class="d">
            <article>
                <h5 class="sub">Misión</h5>
                <h9>
                    Desarrollar servicios web para la persona u organización que lo requiera,
                    mediante la aplicación de insumos de alta calidad con la finalidad de
                    satisfacer diferentes funcionalidades tanto establecidas como nuevas que
                    se van presentando a través del internet.
                </h9><br><br>
                <h5 class="sub">Visión</h5>
                <h9>
                    Ser una empresa capaz de satisfacer las necesidades y peticiones de
                    nuestros clientes, siendo innovadores y responsables a la hora y termino
                    del desarrollo de nuestros proyectos para convertirnos en una empresa
                    reconocida por su potencial y competitividad dentro del mercado, pero sin
                    perder la calidad de nuestros proyectos.
                </h9><br><br>
                <h5 class="sub">Razón Social</h5>
                <h9>
                    Velox S. en C. por A.
                </h9><br><br>
                <h5 class="sub">Eslogan</h5>
                <h9>
                    “Adaptados para cualquier carrera”
                </h9><br><br>
                <h5 class="sub">Filosofía</h5>
                <h9>
                    “No hay problema que no podamos solucionar a pesar de entrar en crisis,
                     pues siempre concentramos nuestras ideas para aprovechar y tomar las
                     riendas de la situación”
                </h9><br><br>
                <h5 class="sub">Logotipo</h5>
                <br><br>
                <img src="img/Logotipo.png" class="hover" style="height: 200px; width: 200px"><br><br>
                <h9>
                            Nuestro logotipo está representado por la especie endémica de México Geococcyx
                            velox, el cual representa que somos una empresa mexicana competitiva, con una
                            gran velocidad en los servicios y con una gran facilidad en que podemos realizar
                            una tarea.
                            Los números binarios que se encuentran en la cola del Geococcyx velox y en las
                            iniciales del nombre de la empresa representan el sistema que usan las
                            computadoras, el cual va a estar relacionado con la programación.
                            El nombre de la empresa es “Velox” debido a la especie, por lo tanto, se encuentra
                            debajo de la imagen de esta misma. El color del logotipo es azul debido a que
                            psicológicamente su vinculación más conocida es con la idea de serenidad y
                            calma, que es con lo que exactamente queremos transmitir a los clientes.
                </h9><br><br>
            </article>
        </div>
        <footer style="background-color: #04C4D9; text-align: center; color:#F8F9FA">
            <h2>INTEGRANTES</h2><br>
        </footer>
        <div class="container_3">
		<article class="col">
                    <img src="img/Alicia.jpg" width="70" height="70">
                    <h3>Cortés Gamboa Alicia</h3>
                    <br><button onclick="return mostrarOcultar('ocultable')" type="button" class="oculta">Mostrar</button>
                    <div id="ocultable" style="display: none">
                        <p>
                            Soy actualmente una estudiante en la carrera de programación en CECyT 9 "Juan De Dios Bátiz",teniendo la edad de 16 años 
                            me considero aplicada a en mis estudios y responsable, además de ser alguien bastante sociable, teniendo un interés en area de tecnología y todo lo relacionado a esta,
                            siendo en el futuro dedicarme a alguna carrera de esta.<br>
                            Me gusta ver series, jugar videojuegos, hacer ejercicio y escuchar música.<br>
                            Siempre estoy dispuesta a aprender cosas nuevas y cumplir todos los retos que me proponga.
                        </p> 
                    </div>
		</article>
                
		<article class="col">
                    <img src="img/Damian.jpg" width="70" height="70">
                    <h3>Jarillo Hernández Armando Damián</h3>
                    <br><button onclick="return mostrarOcultar('ocultable_1')" type="button" class="oculta">Mostrar</button>
                    <div id="ocultable_1" style="display: none">
                        <p>
                            Soy un estudiante del CECyT 9 JDB, me considero alguien que debido a circunstancias de mi niñez me hice muy dedicado a los
                            estudios y con gran afición a la tecnología y videojuegos, aunque gracias a eso se me dificultan las situaciones sociales, 
                            pero hago todo lo que puedo para mejorar en todos los aspectos.
                        </p>
                    </div>
		</article>
                
		<article class="col">
                    <img src="img/Uzias.jpg" width="70" height="70">
                    <h3>García Lucero Uzias</h3>
                    <br><button onclick="return mostrarOcultar('ocultable_2')" type="button" class="oculta">Mostrar</button>
                    <div id="ocultable_2" style="display: none">
                        <p>
                            Actualmente estudio programación en el nivel medio superior, tengo 16 años y planeo dedicarme a algo
                            relacionado con la computación en un futuro, ya sea como ingeniero en sistemas computacionales o en algo relacionado al
                            software. En estos momentos tengo conocimientos en java, css3, html5, js, python y algunas nociones en c++, hablo español
                            y un poco de inglés. En mis tiempos libres me gusta leer o ver la televisión.<br>
                            He desarrollado proyectos relacionados con la computación desde que tenia 12 años y siempre me ha gustado, por eso, una de
                            las cosas que más disfruto hacer es usar una computadora o un celular, creo que se pueden usar para muchas cosas, tanto 
                            buenas, como malas, desafortunadamente.
                        </p>
                    </div>
		</article>
                
		<article class="col">
                    <img src="img/Roberto.jpg" width="70" height="70">
                    <h3>Quintana Romero Roberto</h3>
                    <br><button onclick="return mostrarOcultar('ocultable_3')" type="button" class="oculta">Mostrar</button>
                    <div id="ocultable_3" style="display: none">
                        <p>
                            Nací el 12 de mayo de 2003 en la Ciudad de México, hijo de Jesús Roberto Quintana y Graciela
                            Romero. <br>En 2006 ingrese al Colegio Simón Bolívar donde llevaría a cabo mis estudios básicos de primaria y secundaria 
                            donde realice deportes como natación y basquetbol participando así en partidos y competencias, pero mi gusto por las 
                            ciencias exactas como matemáticas me llevaría a ingresar en 2018 al Instituto Politécnico Nacional donde estudio 
                            actualmente la carrera Técnica en Programación. <br>Planeo ingresar a la universidad y estudiar alguna especialidad 
                            relacionada con matemáticas o alguna rama de la programación.
                        </p>
                    </div>
		</article>
		
                <article class="col">
                    <img src="img/Ivan.jpg" width="70" height="70">
                    <h3>Sánchez Gonzáles Daniel Ivan</h3>
                    <br><button onclick="return mostrarOcultar('ocultable_4')" type="button" class="oculta">Mostrar</button>
                    <div id="ocultable_4" style="display: none">
                        <p>
                            Me apasiona programar, creo que es una gran forma de expresarse tanto de forma intelectual como artistica, mi objetivo
                            es lograr llevar a cabo los proyectos que mi mente propone, y cuando algo realmente util o divertido emerja llevarlo 
                            al siguiente nivel -Navy.
                        </p>
                    </div>
		</article>
                
		<article class="col">
                    <img src="img/Luis.jpg" width="70" height="70">
                    <h3>Tenorio Aspiros Luis Fernando</h3>
                    <br><button onclick="return mostrarOcultar('ocultable_5')" type="button" class="oculta">Mostrar</button>
                    <div id="ocultable_5" style="display: none">
                        <p>
                           Soy un apasionado a la programación y a los videojuegos, mis pasatiempos favoritos
                           son jugar videojuegos, ver anime y leer cuentos de ciencia ficción. <br>
                           Tengo la intención de estudiar ciencia de los datos 
                           cuando vaya a la universidad. 
                        </p>
                    </div>
		</article>
            </div>
        <script src="js/JQuery.js" type="text/javascript"></script>
        <link href="css/bootstrap.css" rel="stylesheet" type="text/css"/>
        <link href="css/estilos.css" rel="stylesheet" type="text/css"/>
    </body>
    </html>
"""
acheteemeele.write(cuerpo)
acheteemeele.close()
wb.open_new_tab("index.html")
