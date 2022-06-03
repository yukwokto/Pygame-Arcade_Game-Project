import pygame, pygwidgets, random
from pygame.locals import *

class Pirate():
    pirateImage = pygame.image.load("images/pirate.png")

    def __init__(self, screen):
        self.screen = screen
        pirateRect = Pirate.pirateImage.get_rect()
        self.width = pirateRect.width
        self.height = pirateRect.height
       
        self.maxWidth = 850
        self.maxHeight = 500
        self.minWidth = 250
        self.minHeight = 0
        self.x = random.randrange(self.minWidth, self.maxWidth)
        self.y = random.randrange(self.minHeight, self.maxHeight)
        self.image = pygwidgets.Image(self.screen, (self.x, self.y), Pirate.pirateImage)

        self.speedX = 5
        self.speedY = 5

    def movement(self):

        self.x += self.speedX
        self.y += self.speedY

        if self.x >= self.maxWidth or self.x <= self.minWidth:
            self.speedX = -self.speedX
            self.x += self.speedX

        if self.y >= self.maxHeight or self.y <= self.minHeight:
            self.speedY = -self.speedY
            self.y += self.speedY

        self.image.setLoc((self.x, self.y))

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












