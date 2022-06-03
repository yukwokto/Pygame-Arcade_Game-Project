import pygame, random, pygwidgets
from pygame.locals import *
from Boat import *
from Pirate import *
from Pier import *
from TreasureIsland import *

class GameMgr():
    pygame.mixer.init()
    NO_OF_PIRATE_SHIP = 5
    NO_OF_TREASURE_ISLAND = 1
    getTreasureSound = pygame.mixer.Sound("sounds/coin.wav")
    returnTreasureSound = pygame.mixer.Sound("sounds/back.wav")

    def __init__(self, screen, screenWidth, screenHeight):
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.treasureCount = 0
        self.entity = []
        
    def gameStart(self):
        self.pirateList = []
        self.score = 0
        self.treasureCount = 0

        #create player boat
        global oBoat
        oBoat = Boat(self.screen, self.screenWidth, self.screenHeight)
        self.entity.append(oBoat)

        #spawning pirates, the treasure island, and the pier
        for i in range(0, GameMgr.NO_OF_PIRATE_SHIP):
            oPirate = Pirate(self.screen)
            self.pirateList.append(oPirate)
            self.entity.append(oPirate)
        
        global oTreasureIsland
        oTreasureIsland = TreasureIsland(self.screen)
        self.entity.append(oTreasureIsland)

        global oPier
        oPier = Pier(self.screen)
        self.entity.append(oPier)

    #allow player control on the boat
    def playerControl(self, keyPressedTuple):
        oBoat.handleEvent(keyPressedTuple)

    def gameUpdate(self):

        global oTreasureIsland
        #enable the movement of the pirate 
        for oPirate in self.pirateList:
            oPirate.movement()
        
        global playerRect #get the rect of the player ship
        playerRect = pygame.Rect(oBoat.locationX(), oBoat.locationY(), oBoat.theWidth(), oBoat.theHeight())

        global pierRect #get the rect of the pier
        pierRect = pygame.Rect(oPier.locationX(), oPier.locationY(), oPier.theWidth(), oPier.theHeight())

        global treasureIslandRect #get the rect of the treasure island
        treasureIslandRect = pygame.Rect(oTreasureIsland.locationX(), oTreasureIsland.locationY(), oTreasureIsland.theWidth(), oTreasureIsland.theHeight())

        #detect collision between the boat and the treasure island
        if pygame.Rect.colliderect(playerRect, treasureIslandRect):
            if oTreasureIsland.treasureExist():
                oTreasureIsland.treasureExcavated()
                oBoat.treasureOnLoad()
                GameMgr.getTreasureSound.play()

        #detect collision between the boat and the pier, add one score if the boat is loaded with treasure
        if pygame.Rect.colliderect(playerRect, pierRect):
            if oBoat.ifTreasureLoaded(): #whether the player get the treasure
                self.treasureCount += 1
                oBoat.treasureUnload()
                GameMgr.returnTreasureSound.play()
                self.entity.remove(oTreasureIsland) #remove the old oTreasure Isalnd from the entity list
                del oTreasureIsland
                oTreasureIsland = TreasureIsland(self.screen) #create a new treasure island
                self.entity.append(oTreasureIsland) #to allow the new treasure island to be drawn on the screen

        #detect collision between the boat and the pirate, send player to the original point if collision is occurred
        global pirateRect
        for pirate in self.pirateList:
            pirateRect = pygame.Rect(pirate.locationX(), pirate.locationY(), pirate.theWidth(), pirate.theHeight())
            if pygame.Rect.colliderect(playerRect, pirateRect):
                oBoat.boatLifeDecreaseBy1()
                oBoat.crashingBack()
                Boat.boatCrashSound.play()

    def getTreasureCount(self):
        return "Treasure: " + str(self.treasureCount)

    def getLifeCount(self):
        return "Life: " + str(oBoat.boatLife())

    def restart(self):
        global oTreasureIsland
        global oBoat
        if oBoat.boatLife() <= 0:
            self.entity = []
            return True

    def draw(self):
        for entity in self.entity:
            entity.draw()