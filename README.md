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

## Patrones

Antes de seguir profundizando en el juego es necesario definir lo que se denominan patrones básicos. Los patrones básicos no son más que configuraciones de vecindades de células que determinan un comportamiento concreto con un número mínimo de células vivas en la estructura. Estos patrones básicos y sus comportamientos han sido determinados o hallado por aficionados al juego en el cual veían un desafío de programación, de hecho se extendió todo un movimiento en torno a este juego, que en ocasiones llegaba a tener connotaciones filosóficas. Llegaron a crearse concursos de búsqueda de patrones interesantes, incluso el propio Conway ofreció un premio de 50 dólares para aquel que encontrara un patrón que creciera de forma indefinida.

Algunos de los patrones que suelen aparecer en el juego de la vida son:

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOAAAADgCAMAAAAt85rTAAAACVBMVEX////AwMAAAADw4bE0AAABoElEQVR4nO3UMa4bMRAFQdn3P/Q3FBpgQo/kbbJe2oBGFSxfvw7f63//gU/vD/C12DvnG2C9AdYbYL0B1htgvQHWG2C9AdYbYL0B1htgvd0APHuA9d0AfM6D4BXdaID1BlhvgPUGWG+A9QZYb4D1BlhvgPUGWG+A9fbOJw+wvhuAn/jofy/2L7+51wD3GuDwvXUD3GuAw/fWDXCvAQ7fWzfAvQY4fG/dAPca4PC9dQPca4DD99YNcK8BDt9bN8C99ijg2QOs7wbgdz/6bz9AgPMNcPQe4HwDHL0HON8AR+8BzjfA0XuA8w1w9B7gfAMcvQc43wBH7wHOt68Dzx5gfTcAP/FY7LaPPDKAgICAgICAgICAgICAgICAgICAgH8Bzx5gfTcA5z/sJzXAegOsN8B6A6w3wHoDrDfAegOsN8B6A6w3wHq7AXj2AOu7AficB8ErutEA6w2w3gDrDbDeAOsNsN4A6w2w3gDrDbDeAOvtnU8eYH03AJ/zIHhFNxpgvQHWG2C9AdYbYL0B1htgvQHWG2C9AdYbYL2988k7HvgDKgBKgW82od0AAAAASUVORK5CYII=">

-Deslizador (Glider): es el patrón astronave más pequeño que se conoce así como el más común. Se desplaza a lo largo del tablero de forma diagonal y tiene una velocidad de “c/4”.

La colmena (Beehive): pueden encontrarse de forma aislada, pero lo mas común esque aparezca de forma apareada o en grupos de cuatro formando el patron pseudo-inmortal llamado “panal de miel” (Honey farm).

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh23pJqSMGDS7McGGwtHtUvh0-U-gmEXbhmw&usqp=CAU">

Nave ligera (Lightweight spaceship): Se desplaza a lo largo del tablero de forma horizontal o vertical.

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTi6WQhc1o0la7O_N1subt5jdJIcGZ7RGrZ0w&usqp=CAU">

# Pseudocódigo

- Crear la base donde se ejecutara todo con pygame
- Crear el patrón
- Iniciar el juego
- Ejecutar las reglas de la vida
- Una célula muerta con exactamente 3 células vecinas vivas "nace"
- Una célula viva con 2 o 3 células vecinas vivas sigue viva, caso contraio muere
- Hacer que cada regla se ejecute haciendo consultas a las diferentes celdas que rodean una "celula" viva
- Repetir las reglas con un bucle
- Crear una funcion donde "q" detenga el juego

#### *Condiciones adicionales*

- Si aprieto una tecla, que esta detenga o reanude el juego
- Para detener el juego declaro que el ciclo se detenga con un False, caso contraio True

# Requisitos

 - Python 3.8.5 ó superior
 - Pygame 2.0.2 ó superior
 - Se creo y ejecuto en Linux, pero tambien puede ser ejecutado en Windows.
