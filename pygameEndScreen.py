import pygame
import pygame_gui

def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center = (400, 300))
    return rotated_surface, rotated_rect

# Phrase of Matching
def youMatch(screen):
    clock = pygame.time.Clock()
    running = True
    size = 100
    angle = 0
    phrase = pygame.font.SysFont('Cooper Black', size).render("Good Job!", False, (105,105,105))
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit()
        phrase_rect = phrase.get_rect(center = (400, 300))

        angle += 1

        screen.fill((0,0,0))
        phrase_rotated, phrase_rotated_rect = rotate(phrase, angle)

        screen.blit(phrase_rotated, phrase_rotated_rect)
        pygame.display.update() 