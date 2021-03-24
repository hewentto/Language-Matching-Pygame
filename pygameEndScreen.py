import pygame
import pygame_gui

def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center = (400, 300))
    return rotated_surface, rotated_rect        



def youMatch(screen, final_time):

    highscore = open(r'highscores.txt', 'r')
    print(highscore.read())
    highscore.close()
    highscore = open(r'highscores.txt', 'a')
    highscore.write(str(final_time) + '\n')
    highscore.close()
    highscore = open(r'highscores.txt', 'r')
    print(highscore.read())
    highscore.close()

    #Background code (might be temporary)
    bg_img = pygame.image.load('worldmap1024.jpg')
    bg = pygame.transform.scale(bg_img, (800, 600))
    
    # font needed to render the highscore text
    font = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 30)

    endManager = pygame_gui.UIManager((800, 600))


    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 545), (150, 50)),
                                            text='Back',
                                            manager=endManager)

    clock = pygame.time.Clock()

    #Win message dimensions
    size = 100
    angle = 0

    #Win message
    phrase = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', size).render("Good Job!", False, (105,105,105))
   
    while True:
        time_delta = clock.tick(40)

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

            endManager.process_events(event)
   
        #Create rect for win message
        phrase_rect = phrase.get_rect(center = (400, 300))

        #Show background        
        screen.blit(bg, (0,0))

        #Show user's time (rounded to 3 places)
        screen.blit(font.render("Your Time: {:0.3f}".format(final_time), False, (105,105,105)), (300, 500))
        
        #Rotate win message
        angle += 1
        phrase_rotated, phrase_rotated_rect = rotate(phrase, angle)

        #Show the spinning win message
        screen.blit(phrase_rotated, phrase_rotated_rect)

        #Update manager (for the buttons)
        endManager.update(time_delta)
        #Display buttons
        endManager.draw_ui(screen)
        pygame.display.update() 
