import pygame, pygwidgets, random
from pygame.locals import *

class Pier():
    pierImage = pygame.image.load("images/dock.png")

    def __init__(self, screen, locX=4, locY=300):
        self.screen = screen
        self.x = locX
        self.y = locY
        self.image = pygwidgets.Image(screen, (self.x, self.y), Pier.pierImage)

        pierRect = Pier.pierImage.get_rect()
        self.width = pierRect.width
        self.height = pierRect.height
    
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