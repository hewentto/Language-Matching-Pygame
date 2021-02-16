import pygame

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((500, 500))

font = pygame.font.SysFont(None, 20)
# background = pygame.Surface((800, 600))
# background.fill(pygame.Color('#000000'))

is_running = True

def draw_text(text, font, color, surface, x , y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)
while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    button_1 = pygame.Rect(50, 100, 200, 50)
    button_2 = pygame.Rect(50, 200, 200, 50)
    pygame.draw.rect(window_surface, (255,69,48), button_1)
    pygame.draw.rect(window_surface, (255,126,0), button_2)
    draw_text('Main Menu', font, (255, 255, 255), window_surface, 20, 20)
    # window_surface.blit(background, (0, 0))

    pygame.display.update()