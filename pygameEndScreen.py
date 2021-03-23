import pygame
import pygame.freetype
import pygame_gui

def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center = (400, 300))
    return rotated_surface, rotated_rect



# Phrase of Matching
def youMatch(screen, final_time):

    #font needed to render the highscore text
    font = pygame.freetype.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 30)
    #creating the reading/writing object
    

    
#%%

    highscore = open(r'highscores.txt', 'r')
    print(highscore.read())
    highscore.close()
    highscore = open(r'highscores.txt', 'a')
    highscore.write(str(final_time) + '\n')
    highscore.close()
    highscore = open(r'highscores.txt', 'r')
    print(highscore.read())
    highscore.close()

#%%
def youMatch(screen):

    endManager = pygame_gui.UIManager((800, 600))


    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 545), (150, 50)),
                                            text='Back',
                                            manager=endManager)

    clock = pygame.time.Clock()
    running = True
    size = 100
    angle = 0
    phrase = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', size).render("Good Job!", False, (105,105,105))
    while running:
        time_delta = clock.tick(40)

        #clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit()
            
            # Handle the back button
            if event.type == pygame.USEREVENT:
                # If button is pressed
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    # If start button, start
                    if event.ui_element == back_button:
                        return
        phrase_rect = phrase.get_rect(center = (400, 300))

        endManager.process_events(event)

        angle += 1

        screen.fill((0,0,0))
        font.render_to(screen, (300, 500), ("Your Time:" + str(int(final_time))),(105,105,105))
        phrase_rotated, phrase_rotated_rect = rotate(phrase, angle)

        screen.blit(phrase_rotated, phrase_rotated_rect)
        pygame.display.update() 
# %%
        #Update manager (for the buttons)
        endManager.update(time_delta)
        #Display buttons
        endManager.draw_ui(screen)
        pygame.display.update() 
