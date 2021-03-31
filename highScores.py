import os
import pygame
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

pygame.init()
COLOR_INACTIVE = (0,0,0)
COLOR_ACTIVE = pygame.Color('lightskyblue3')
HIGHSCORE_FONT = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 60)
INITIALS_FONT = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 30)

#Keep the globals empty/False
displayTopScore=''
done = False

def fireBase():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "spanglish-matching-high-scores-firebase-adminsdk-yzong-17cc906b50.json"

    # Use the application default credentials
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
    'projectId': 'spanglish-matching-high-scores'
    })

    db = firestore.client()


def getListOfScores():
    
    #Get the connection to the firebase cloud
    db = firestore.client()

    #Get all the elements inside the highscores collection
    users_ref = db.collection(u'highscores')
    docs = users_ref.stream()

    #Store results in a list
    return sorted([float(doc.id) for doc in docs])

def getListOfNames():
    #Get the connection to the firebase cloud
    db = firestore.client()

    #Get all the elements inside the highscores collection
    users_ref = db.collection(u'highscores')
    docs = users_ref.stream()

    #Store results in a list
    return [doc.to_dict()['name'] for doc in docs]



def addScore(score, screen):

    #Refresh the global back to empty, in case it is still active from a previous top score
    global displayTopScore
    displayTopScore=''

    font = pygame.font.SysFont('microsoftjhengheimicrosoftjhengheiuibold', 30)

    #Get the connection to the firebase cloud
    db = firestore.client()

    #Get all the elements inside the highscores collection
    users_ref = db.collection(u'highscores')
    docs = users_ref.stream()

    #Store results in a list
    listOfScores = getListOfScores()

    #Check if score cracks top 10
    if score < max(listOfScores):
        listOfScores.append(score)

        
        doc_ref = db.collection(u'highscores').document(u'{}'.format(score))

        #Place a variable inside the doc, and assign it to the name provided in the text box
        doc_ref.set({
            u'name' : u'{}'.format(getInputBox(screen, score))
        })

        #Sort the list to know which index the new score falls under
        listOfScores.sort()
        print(listOfScores)

        #Update the variable (the index it falls under +1)
        displayTopScore = 'Congratulations! Top {}!'.format(listOfScores.index(float(score))+1)

        #Delete the max score if there are more than 10 scores
        if len(listOfScores) > 10:
            db.collection(u'highscores').document(u'{}'.format(str(max(listOfScores)))).delete()



class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_ACTIVE
        self.text = text
        self.txt_surface = INITIALS_FONT.render(text, True, (0,0,0))
        self.active = False

    def handle_event(self, event):
        global done
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    #Stop the loop in getInputBox
                    done = True
                    #Return the value for assignment in FireBase
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    #Truncate the string if backspace is pressed
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = INITIALS_FONT.render(self.text, True, (0,0,0))

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


#This function is actually it's own screen
def getInputBox(screen, final_time):
    clock = pygame.time.Clock()

    #Create input box
    box = InputBox(300, 300, 140, 50)

    #Text to display on screen
    highScoreText = HIGHSCORE_FONT.render('High Score!', False, (0, 0, 0))
    enterInitialsText = INITIALS_FONT.render('Enter Initials:', False, (0, 0, 0))

    #Background image
    bg_img = pygame.image.load('worldmap1024.jpg')
    bg = pygame.transform.scale(bg_img, (800, 600))

    #Referance to the global variables
    global done

    #Always false when initializing the function
    done = False

    while not done:

        #Check if top right 'X' is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            #Check for input updates in box
            name = box.handle_event(event)

        #Draw the text
        screen.blit(bg, (0,0))
        screen.blit(highScoreText,(210, 10))
        screen.blit(enterInitialsText,(300, 230))
        screen.blit(INITIALS_FONT.render("Your Time: {:0.3f}".format(final_time), False, (0,0,0)), (270, 500))

        #Keep the text inside the box updated
        box.update()

        #Display the box
        box.draw(screen)

        pygame.display.flip()
        clock.tick(30)
    #Return the name for assignment in FireBase
    return name