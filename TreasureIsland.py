import pygame, pygwidgets, random
from pygame.locals import *

class TreasureIsland():
    islandImage = pygame.image.load("images/island.png")

    def __init__(self, screen):
        self.screen = screen
        self.x = random.randrange(250, 850)
        self.y = random.randrange(0, 500)
        self.image = pygwidgets.Image(self.screen, (self.x, self.y), TreasureIsland.islandImage)

        islandRect = TreasureIsland.islandImage.get_rect()
        self.width = islandRect.width
        self.height = islandRect.height

        self.treasure = True

    def treasureExist(self): #to tell whether the treasure is on the island
        return self.treasure

    def treasureExcavated(self):
        self.treasure = None

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