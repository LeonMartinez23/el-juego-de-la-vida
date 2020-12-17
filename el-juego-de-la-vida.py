#Librerias que usaremos
import pygame, time, numpy as np

#Ancho y alto de la ventana
width, height = 800, 800

#Creación de la ventana
screen = pygame.display.set_mode((height, width))

#Declaro los colores que usare
negro = 0, 0, 0
blanco = 255,255,255
gris = 125,125,125
otro_gris = 211,211,211

#Pinto el fondo (negro) 
screen.fill(negro)

#Cantidad de celdas en cada eje
Cx, Cy = 100, 100

#Ancho y alto de cada celda
dimCW = width / Cx
dimCH = height / Cy

#Inicializo en ceros las celdas
estado = np.zeros((Cx, Cy))

#Autómata (Inicializo la posición de cada "célula")
posInitX = int((Cx / 2) - 3)
posInitY = int((Cy / 2) - 5)

estado[posInitX, posInitY] = 1
estado[posInitX + 1, posInitY] = 1
estado[posInitX + 2, posInitY] = 1

estado[posInitX, posInitY + 2] = 1
estado[posInitX + 1, posInitY + 2] = 1
estado[posInitX + 1, posInitY + 2] = 1

estado[posInitX, posInitY + 3] = 1
estado[posInitX + 3, posInitY + 3] = 1

estado[posInitX, posInitY + 4] = 1
estado[posInitX + 1, posInitY + 4] = 1
estado[posInitX + 2, posInitY + 4] = 1
estado[posInitX + 3, posInitY + 4] = 1

#Reanuda o pausa el juego
pausa = True
quitar = False

while not quitar:
    
    #Título de la ventana
    title = ("El juego de la vida - León")
    pygame.display.set_caption(title)

    NewEstado = np.copy(estado)

    #Color del fondo
    screen.fill(negro)

    #Deley entre cada NewEstado
    time.sleep(0.1)

    #Registra eventos del teclado
    ev = pygame.event.get()

    for event in ev:

        #Si cierran la ventana finaliza el juego
        if event.type == pygame.QUIT:
            quitar = True
            break

        if event.type == pygame.KEYDOWN:

            #Si oprimen "q" finaliza el juego
            if event.key == pygame.K_q:
                quitar = True
                break

            else:
                #Si toco cualquier otra tecla pauso el juego o reanudo
                pausa = not pausa

    #Recorro cada una de las celdas generadas
    for y in range(0, Cx):
        for x in range(0, Cy):

            if not pausa:

                #Lógica usada para hacer los calculos de cada casilla (celula), aplicando tambien algo conocido en la creación de videojuegos como "la técnica del pacman"
                celdas = (
                    estado[(x - 1) % Cx, (y - 1) % Cy]
                    + estado[x % Cx, (y - 1) % Cy]
                    + estado[(x + 1) % Cx, (y - 1) % Cy]
                    + estado[(x - 1) % Cx, y % Cy]
                    + estado[(x + 1) % Cx, y % Cy]
                    + estado[(x - 1) % Cx, (y + 1) % Cy]
                    + estado[x % Cx, (y + 1) % Cy]
                    + estado[(x + 1) % Cx, (y + 1) % Cy]
                )

                #-----------------------Las reglas de la vida----------------

                #Una célula muerta con exactamente 3 células vecinas vivas "nace"
                if estado[x, y] == 0 and celdas == 3:
                    NewEstado[x, y] = 1

                #Una célula viva con 2 o 3 células vecinas vivas sigue viva, caso contraio muere
                elif estado[x, y] == 1 and (celdas < 2 or celdas > 3):
                    NewEstado[x, y] = 0

            #Dibuja cada cécula en la pantalla
            poly = [
                (int(x * dimCW), int(y * dimCH)),
                (int((x + 1) * dimCW), int(y * dimCH)),
                (int((x + 1) * dimCW), int((y + 1) * dimCH)),
                (int(x * dimCW), int((y + 1) * dimCH)),
            ]

            if NewEstado[x, y] == 0:
                #Dibuja las líneas de cada fila y columna
                pygame.draw.polygon(screen,gris,poly,1)
            else:
                if pausa:
                    #Con el juego pausado pinto de gris las celdas
                    pygame.draw.polygon(screen,otro_gris, poly)
                else:
                    #Con el juego ejecutándose pinto de blanco las celdas
                    pygame.draw.polygon(screen, blanco, poly)

    #Actualizo el estado
    estado = np.copy(NewEstado)

    #Actualizo la pantalla
    pygame.display.flip()