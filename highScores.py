import os
import pygame
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#Keep the global empty
displayTopScore=''

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
    return [float(doc.id) for doc in docs]


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

        #Despite nothing being placed inside, this is necessary to initalize the document.
        doc_ref.set({})

        #Sort the list to know which index the new score falls under
        listOfScores.sort()
        print(listOfScores)

        #Update the variable (the index it falls under +1)


        displayTopScore = 'Congratulations! Top {}!'.format(listOfScores.index(float(score))+1)

        #Delete the max score if there are more than 10 scores
        if len(listOfScores) > 10:
            db.collection(u'highscores').document(u'{}'.format(str(max(listOfScores)))).delete()
