import pygame, pygwidgets, random
from pygame.locals import *

class Boat():
    pygame.mixer.init()
    boatImage = pygame.image.load("images/boat.png")
    boatCrashSound = pygame.mixer.Sound("sounds/boatsink.wav")

    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, locX=94, locY=290):
        self.screen = screen
        self.x = locX
        self.y = locY
        self.image = pygwidgets.Image(self.screen, (self.x, self.y), Boat.boatImage)
        boatRect = self.image.getRect()
        self.width = boatRect.width
        self.height = boatRect.height
        self.maxWidth = SCREEN_WIDTH - self.width
        self.maxHeight = SCREEN_HEIGHT - self.height

        self.treasureLoaded = False
        self.life = 3

    def handleEvent(self, keyPressedTuple):
        self.speedX = 10
        self.speedY = 10

        #set player control of the boat
        if keyPressedTuple[pygame.K_w]:
            self.y -= self.speedY
        if keyPressedTuple[pygame.K_s]:
            self.y += self.speedY
        if keyPressedTuple[pygame.K_a]:
            self.x -= self.speedX
        if keyPressedTuple[pygame.K_d]:
            self.x += self.speedX

        #set limit of the boat
        if self.x <= 0:
            self.x = 0
        if self.x >= self.maxWidth:
            self.x = self.maxWidth
        if self.y <= 0:
            self.y = 0
        if self.y >= self.maxHeight:
            self.y = self.maxHeight

        self.image.setLoc((self.x, self.y))

    def crashingBack(self):
        self.x = 94
        self.y = 290

    def treasureOnLoad(self):
        self.treasureLoaded = True
    
    def treasureUnload(self):
        self.treasureLoaded = False

    def ifTreasureLoaded(self):
        return self.treasureLoaded

    def boatLife(self):
        return self.life

    def boatLifeDecreaseBy1(self):
        self.life -= 1

    def locationX(self):
        return self.x
    
    def locationY(self):
        return self.y

    def theWidth(self):
        return self.width

    def theHeight(self):
        return self.height

    def draw(self):
        self.image.draw()