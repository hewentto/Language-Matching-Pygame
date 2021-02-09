import pygame
from tools import button

pygame.init()

pygame.display.set_caption('Jesse Test')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

is_running = True

test = button.Button(400, 300, 60, 50)

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.blit(background, (0, 0))

    test.draw(background)

    pygame.display.update()