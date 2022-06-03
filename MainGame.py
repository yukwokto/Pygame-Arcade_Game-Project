import pygame
from pygame.locals import *
import sys
import pygwidgets
import random
from GameMgr import *

#Define game parameters
GREY = (169,169,169)
OCEAN_BLUE = (0, 110, 230)
WHITE = (255,255,255)
BLACK = (0,0,0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
PANEL_WIDTH = SCREEN_WIDTH
PANEL_HEIGHT = 100
FPS = 60

#Initalise the game
pygame.init()
pygame.mixer.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Treasure Island")
GAMEICON = pygame.image.load('images/icon.png')
pygame.display.set_icon(GAMEICON)
clock = pygame.time.Clock()
pygame.mixer.music.load("sounds/backgroundmusic.mp3")
pygame.mixer.music.set_volume(0.5)

#Loading Game Assets
oStartButton = pygwidgets.TextButton(SCREEN, (780, 625), "START", textColor=BLACK, width=120, fontSize=30, height=50)
oLifeDisplay = pygwidgets.DisplayText(SCREEN, (90, 638), "Life: 3", textColor=BLACK, fontSize=40)
oTreasureDisplay = pygwidgets.DisplayText(SCREEN, (410, 638), "Treasure: 0", textColor=BLACK, fontSize=40)
oGameMgr = GameMgr(SCREEN, 1000, 600)

#Game loop
inGame = False
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if inGame == True:
            if oGameMgr.restart():
                inGame = False
                oStartButton.enable()
                oLifeDisplay.setValue("Life: 3")
                oTreasureDisplay.setValue("Treasure: 0")
                pygame.mixer.music.stop()

        elif oStartButton.handleEvent(event):
            inGame = True
            oStartButton.handleEvent(event)
            oGameMgr.gameStart()
            oStartButton.disable()
            pygame.mixer.music.play()

    if inGame == True: 
        keyPressedTuple = pygame.key.get_pressed()
        oGameMgr.playerControl(keyPressedTuple)
        oGameMgr.gameUpdate()
        playerTreasure = oGameMgr.getTreasureCount()
        oTreasureDisplay.setValue(playerTreasure)
        playerLife = oGameMgr.getLifeCount()
        oLifeDisplay.setValue(playerLife)

    SCREEN.fill(OCEAN_BLUE)
    pygame.draw.rect(SCREEN, GREY, pygame.Rect(0, 600, PANEL_WIDTH, PANEL_HEIGHT))
    oStartButton.draw()
    oLifeDisplay.draw()
    oTreasureDisplay.draw()
    oGameMgr.draw()
    pygame.display.update()
    clock.tick(FPS)