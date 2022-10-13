# importing
import random
import sys
import pygame
from pygame.locals import *
from time import sleep
from turtle import *
from lets_test import Hello
from IntroScreen import instructionText

#global variables
windowWidth = 600
windowHeight = 499

#set window heigth and width
window = pygame.display.set_mode((windowWidth, windowHeight))
elevation = windowHeight * 0.8
gameImages = {}
framesPerSecond = 32 
pipeImage = "Images/pipe.png"
backgroundImage = "Images/background.jpg"
birdPlayerImage = "Images/bird.png"
seaLevelImage = "Images/base.jfif"

pygame.display.update()

def flappyGame():
    yourScore = 0
    horizontal = int(windowWidth/5)
    vertical = int(windowWidth/2)
    ground = 0
    myTempHeight = 100

    #generating hte 2 pipes
    firstPipe = createPipe()
    secondPipe = createPipe()

    #list containing the lower pipes
    downPipes = [
        {"x": windowWidth + 300 - myTempHeight, "y": firstPipe[1]["y"]},
        {"x": windowWidth + 300 - myTempHeight + (windowWidth/2), "y": secondPipe[1]["y"]},
    ]

    #list containing upper pipes
    upPipes = [
        {"x": windowWidth + 300 - myTempHeight, "y": firstPipe[0]["y"]},
        {"x": windowWidth + 300- myTempHeight + (windowWidth/2), "y": secondPipe[0]["y"]},
    ]
    
    pipeVelX = -4 #pipe velocity

    birdVelocityY = -9 # says in hte variable
    birdMaxVelY = 10
    birdMinVelY = -8
    birdAccY = 1

    # Velocity while flapping
    birdFlapVelocity = -8
    birdFlapped = False
    while True:

        #handeling the key pressing event
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if vertical > 0:
                    birdVelocityY = birdFlapVelocity
                    birdFlapped = True

        #this function will reset the game if crashed
        gameOver = isGameOver(horizontal, vertical, upPipes, downPipes)
        if gameOver:
            return
        

        #check your score
        playerMidPos = horizontal + gameImages["flappyBird"].get_width()/2
        for pipe in upPipes:
            pipeMidPos = pipe["x"] + gameImages["pipeImage"][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                #printing score
                yourScore += 1
                print(f"Your Score is {yourScore}")
        
        if birdVelocityY < birdMaxVelY and not birdFlapped:
            birdVelocityY += birdAccY
        
        if birdFlapped:
            birdFlapped = False
        playerHeight = gameImages["flappyBird"].get_height()
        vertical = vertical + min(birdVelocityY, elevation - vertical - playerHeight)

        #move pipes to the left aka make it seem as if teh bird is moving
        for upperPipe, lowerPipe in zip(upPipes, downPipes):
            upperPipe["x"] += pipeVelX
            lowerPipe["x"] += pipeVelX
        
        # add another pipe when the first one is about to exit teh screens view thingy
        if 0 < upPipes[0]["x"] < 5:
            newPipe = createPipe()
            upPipes.append(newPipe[0])
            downPipes.append(newPipe[1])
        
        # removes pipe if it is out of hte screens view thing 
        if upPipes[0]["x"] < - gameImages["pipeImage"][0].get_width():
            upPipes.pop(0)
            downPipes.pop(0)
        
        #make the images blit? (dont know what it means)
        window.blit(gameImages["background"], (0, 0))
        for upperPipe, lowerPipe in zip(upPipes, downPipes):
            window.blit(gameImages["pipeImage"][0],
                        (upperPipe["x"], upperPipe["y"]))
            window.blit(gameImages["pipeImage"][1],
						(lowerPipe["x"], lowerPipe["y"]))
        
        window.blit(gameImages["seaLevel"], (ground, elevation))
        window.blit(gameImages["flappyBird"], (horizontal, vertical))

        #getting the digits of score
        numbers = [int(x) for x in list(str(yourScore))]
        width = 0

        #finding the width of score images from number.
        for num in numbers:
            width += gameImages["scoreImages"][num].get_width()
        Xoffset = (windowWidth - width)/1.1

        #biiting? the images in the window
        for num in numbers:
            window.blit(gameImages["scoreImages"][num], (Xoffset, windowWidth*0.02))
            Xoffset += gameImages["scoreImages"][num].get_width()

        #refreshing hte games window and getting score
        pygame.display.update()

        #setting the fps
        framesPerSecondClock.tick(framesPerSecond)

#checking if bird is above sea level
def isGameOver(horizontal, vertical, upPipes, downPipes):
    if vertical > elevation - 25 or vertical < 0:
        return True
    
    #checking if bird hits any pipe or not
    for pipe in upPipes:
        pipeHeight = gameImages["pipeImage"][0].get_height()
        if(vertical < pipeHeight + pipe["y"] and abs(horizontal - pipe["x"]) < gameImages["pipeImage"][0].get_width()):
            return True
    
    for pipe in downPipes:
        if (vertical + gameImages["flappyBird"].get_height() > pipe["y"]) and abs(horizontal - pipe["x"]) < gameImages["pipeImage"][0].get_width():
            return True
        return False

def createPipe():
    offset = windowHeight/3
    pipeHeight = gameImages["pipeImage"][0].get_height()

    #generating random pipe heigths i hope
    y2 = offset + random.randrange(0, int(windowHeight - gameImages["seaLevel"].get_height() - 1.2 * offset))
    pipeX = windowWidth + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        #upper pipe
        {"x": pipeX, "y": -y1},
        #lower pipe
        {"x": pipeX, "y": y2}
    ]
    return pipe

#program starts running
if __name__ == "__main__":
    # pygame moduels intiiation
    pygame.init()
    framesPerSecondClock = pygame.time.Clock()

    # Screens title
    pygame.display.set_caption("Cesar's project for a veteran.")

    #loading all images for te score thing
    gameImages["scoreImages"] = (
        pygame.image.load("Images/0.png").convert_alpha(),
        pygame.image.load("Images/1.png").convert_alpha(),
        pygame.image.load("Images/2.png").convert_alpha(),
        pygame.image.load("Images/3.png").convert_alpha(),
        pygame.image.load("Images/4.png").convert_alpha(),
        pygame.image.load("Images/5.png").convert_alpha(),
        pygame.image.load("Images/6.png").convert_alpha(),
        pygame.image.load("Images/7.png").convert_alpha(),
        pygame.image.load("Images/8.png").convert_alpha(),
        pygame.image.load("Images/9.png").convert_alpha()
    )
    gameImages["flappyBird"] = pygame.image.load(birdPlayerImage).convert_alpha()
    gameImages["seaLevel"] = pygame.image.load(seaLevelImage).convert_alpha()
    gameImages["background"] = pygame.image.load(backgroundImage).convert_alpha()
    gameImages["pipeImage"] = (pygame.transform.rotate(pygame.image.load(
        pipeImage).convert_alpha(), 180), pygame.image.load(
            pipeImage).convert_alpha())

    print("Welcome to Flappy Bird (remake)")
    print("press Up Arrow or space to start the game")

while True:
    #set the coordinates of hte bird
    horizontal = int(windowWidth/5)
    vertical = int((windowHeight - gameImages["flappyBird"].get_height())/2)

    #for level
    ground = 0
    while True:
        for event in pygame.event.get():
            # close game when user click buttonnn
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()

                #exit program
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                flappyGame()
            
            else:
                window.blit(gameImages["background"], (0,0))
                window.blit(gameImages["flappyBird"], (horizontal, vertical))
                window.blit(gameImages["seaLevel"], (ground, elevation))

                #refresh the screen
                pygame.display.update()

                # set hte fps of hte scfeen
                framesPerSecondClock.tick(framesPerSecond)





