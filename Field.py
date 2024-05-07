import numpy.random
import pygame
import math


class Field():
    def __init__(self, myDB, screen):
        self.myDB = myDB
        self.screen = screen
        self.RATIO = 397/271
        self.deck = []
        self.width = 0
        self.height = 0

        self.phase = ['Draw Phace', 'Standby Phase', 'Main Phase1', 'Battale Phase', 'Main Phase2', 'End Phase']
        self.id = {}
        self.hand = []
        self.monsterzone = []
        self.spelltrapzone = []
        self.graveYeard = []
        self.outOfPlay = []
        self.mainDeck = []
        self.extraDeck = []

    def SetPosToCard(self, key, value):
        self.id[key] = value

    def GetPosToCard(self, key):
        return self.id[key]

    def SetCards(self):
        getDeck = self.myDB.cursor()
        getDeck.execute("SELECT cardId FROM decks WHERE userID = 'yugi' ORDER BY name")
        cards = getDeck.fetchall()
        for i in cards:
            self.deck.append(i[0])
            self.mainDeck.append(i[0])

        numpy.random.shuffle(self.mainDeck)

    def GetHand(self):
        hand = 0
        for i in reversed(self.mainDeck):
            if hand == 5:
                break
            self.mainDeck.remove(i)
            self.hand.append(i)
            hand = hand + 1
        return self.hand

    def GetDeckString(self):
        fieldInfo = ''
        n = 0
        for i in self.deck:
            if n > 0:
                fieldInfo = fieldInfo + ':' + i
            else:
                fieldInfo = fieldInfo + i
                n = n + 1
        return fieldInfo

    def DrawBox(self, x, y):
        pygame.draw.line(self.screen, 'yellow', (x, y), (x + self.GetWidth(), y), 3)
        pygame.draw.line(self.screen, 'yellow', (x + self.GetWidth(), y), (x + self.GetWidth(), y + self.GetHeight()), 3)
        pygame.draw.line(self.screen, 'yellow', (x, y), (x, y + self.GetHeight()), 3)
        pygame.draw.line(self.screen, 'yellow', (x, y + self.GetHeight()), (x + self.GetWidth(), y + self.GetHeight()), 3)

    def SetWidth(self, length):
        self.width = length

    def GetWidth(self):
        return self.width

    def GetHeight(self):
        return math.floor(self.width * self.RATIO)
