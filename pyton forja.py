import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definindo as dimensões da tela
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo Simples")

# Definindo cores
background_color = (200, 255, 200)
red = (255, 0, 0)

# Definindo a posição inicial do retângulo
rect_x = screen_width // 2
rect_y = screen_height // 2
rect_width = 50
rect_height = 50
speed = 5

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed

    # Preenche a tela de preto
    screen.fill(background_color)

    # Desenha o retângulo
    pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

    # Atualiza a tela
    pygame.display.flip()
    pygame.time.Clock().tick(60)