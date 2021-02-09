import pygame
import time
from tools.button import Button

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 40)

window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#ffffff'))

text_surface = myfont.render("Language Matching", True, pygame.Color('#000000'))

is_running = True

# All usable buttons
starting_pos = 100
buttons = [Button.standard(325, starting_pos), Button.standard(325, starting_pos + 100*1), Button.standard(325, starting_pos + 100*2), Button.standard(325, starting_pos + 100*3)]

start_time = None
end_time = 0.0

def handleTime():
    global start_time

    if start_time == None:
        start_time = time.time()

# Add text to the buttons
buttons[0].addText("Start")
buttons[1].addText("View words")
buttons[2].addText("Start timer")
buttons[3].addText("Quit")

buttons[2].setCallback(handleTime)
buttons[3].setCallback(quit)


while is_running:

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONUP:
            for b in buttons:
                b.checkPressed(event)
    
    window_surface.blit(background, (0, 0))

    # Timer
    if start_time != None:
        end_time = time.time()
        timer = myfont.render(str(int(end_time - start_time)), True, pygame.Color('#000000'))
        window_surface.blit(timer, (500, 300))

    # Display title
    window_surface.blit(text_surface, (210, 25))

    # Draw all buttons
    for b in buttons:
        b.draw(window_surface)

    pygame.event.clear()

    pygame.display.update()
