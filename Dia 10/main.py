import pygame
import random
import math
from pygame import mixer

# Inicializar a pygame
pygame.init()

# Definimos el color del fondo y el color de las estrellas
fondo = (13, 0, 40)
color_estrella = (255, 255, 255)

# Número de estrellas
cantidad_estrellas = 150

# Generar posiciones iniciales de estrellas
estrellas = [(random.randint(0, 800), random.randint(0, 600), random.uniform(0.5, 1.0)) for _ in range(cantidad_estrellas)]

# Crea la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho,alto))

# Titulo e Icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

# Musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)

# Variables del jugador
img_jugador = pygame.image.load('cohete.png')
jugador_x = (ancho / 2) - 32
jugador_y = alto - 100
jugador_x_cambio = 0

# Variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []

for e in range(8):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0, ancho))
    enemigo_y.append(random.randint(36, 150))
    enemigo_x_cambio.append(0.15)
    enemigo_y_cambio.append(50)

# Variables de la bala
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 536
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# Puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 22)
texto_x = 10
texto_y = 10

# Texto Final
fuente_final = pygame.font.Font('freesansbold.ttf', 46)

def game_over():
    mi_fuente_final = fuente_final.render('Game Over!', True, (255, 0, 0))
    pantalla.blit(mi_fuente_final, (250, 280))

def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

def disparar_bala(x, y):
    global bala_visible
    bala_visible = True

    pantalla.blit(img_bala, (x + 16, y + 10))

def detectar_colision(x1, x2, y1, y2):
    distancia = math.dist([x1, y1], [x2, y2])
    return distancia <= 32

def eliminar_enemigos():
    for e in range(8):
        enemigo_y[e] = 1000

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill(fondo)

    # Dibujar estrellas con parpadeo
    for x, y, brightness in estrellas:
        # Simular parpadeo ajustando el brillo
        brightness += random.uniform(-0.05, 0.05)
        brightness = max(0.5, min(1.0, brightness))  # Limitar brillo entre 0.5 y 1.0

        # Dibujar estrella
        color = (int(color_estrella[0] * brightness), int(color_estrella[1] * brightness), int(color_estrella[2] * brightness))
        pygame.draw.circle(pantalla, color, (x, y), 2)  # Estrellas pequeñas de radio 2

    # Escuchar eventos
    for event in pygame.event.get():
        # Evento cerrar
        if event.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar flechas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_x_cambio = -0.7

            if event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.7

            if event.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                if not bala_visible:
                    sonido_bala.play()
                    bala_x = jugador_x
                    disparar_bala(jugador_x, jugador_y)

        # Evento soltar flechas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicacion del jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0

    if jugador_x >= ancho - 64:
        jugador_x = ancho - 64

    # Modificar ubicacion del enemigo
    for e in range(8):
        if enemigo_y[e] > 500:
            eliminar_enemigos()
            game_over()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # Mantener dentro de bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.15
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= ancho - 64:
            enemigo_x_cambio[e] = -0.15
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colision
        colision = detectar_colision(
            enemigo_x[e] + 32,
            bala_x + 16,
            enemigo_y[e] + 32,
            bala_y + 16
        )

        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_visible = False
            bala_y = 536
            puntaje += 1
            enemigo_x[e] = random.randint(0, ancho)
            enemigo_y[e] = random.randint(0, 100)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento bala
    if bala_y <= -64:
        bala_y = 536
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    # Actualizar pantalla
    pygame.display.update()