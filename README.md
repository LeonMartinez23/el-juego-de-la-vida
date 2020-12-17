# El juego de la vida

Uno de los mas grandes misterios de la humanidad son ¿como inicio la vida?, ¿cúales fueron los factores clave para que se desarollara la vida?, si el ser humando llegara un día a responder a estas preguntas trascendentales, al conocer cúales serian ese leyes básicas fundamentales que expliquen la existencia misma de la vida o incluso del universo, ¿seriamos capaces de simular en un ordenador la realidad misma?. John Horton Conway fue un matemático británico conocido por ser el creador del "juego de la vida". Conway estaba interesado en resolver un problema presentado en los años cuarenta por el matemático John Von Newman quien intento crear una máquina hipotética que fuera capaz de construir copias de si misma, cosa que consiguió basándose en un modelo matemático que se desarrollaba en un tablero cuadriculado con una gran cantidad de normas complejas, creando lo que pasaría a denominarse desde entonces un autómata celular.

En 1970 Conway creo "el juego de la vida", el cúal fue mostrado al público por primera vez en octubre de ese mismo año través de un artículo publicado en la revista Scientific American, en la columna Mathematical Games de Martin Gadner siendo de gran interes por su gran sencillez con la cúal a partir de unas simples reglas podria mediante la evolución de unos patrones emular él como evolucina la vida.

La popularidad del juego se debia a la similitud con algunos de los procesos evolutivos que determinan el surgimiento, decadencia y alteraciones que experimentan las sociedades de seres vivos, tanto a nuestro nivel como a nivel celular, y no sólo eso ya que físicos,
matemáticos, biólogos e incluso economistas y filósofos pudieron apreciar su potencial para asemejar de algún modo procesos en sus correspondientes campos.

## Reglas del juego

Este juego está basado en la evolución de estados sucesivos, en los cuales las condiciones del estado futuro dependen solamente de las condiciones del estado anterior. Por tanto la participación en el mismo únicamente consiste en determinar las condiciones iniciales 

1- Supervivencia: Cada individuo o célula
que cumpla el requisito de tener 2 ó 3 vecinos
vivos sobrevive a la siguiente generación (por
tanto su estado se mantiene inalterado en el
siguiente turno.

2- Fallecimiento: Una célula viva que tenga
menos de 2 vecinos fallece por aislamiento o
soledad en el siguiente estado o turno. Una
célula viva que tenga más de trés vecinos vivos
muere por superpoblación en el siguiente estado
o turno.

3- Nacimiento: Si una celda vacía pasa a
tener en su vecindad exactamente 3 células
vivas su estado futuro en el siguiente turno será
el de célula viva (nacimiento de nuevo
individuo)

# Requisitos

 - Python 3.7.7 o superior (esencial para pygame)
 - Pygame 2.0.0 o superior
 - Numpy 1.17.4 o superior
 - Se creo y ejecuto en Linux, pero tambien puede ser ejecutado en Windows.

### Para instalar pygame ejecutar

`$ pip3 install pygame`
