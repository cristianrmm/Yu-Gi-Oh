import numpy.random
import pygame
import math


class Field():
    def __init__(self, myDB, screen):
        self.myDB = myDB
        self.screen = screen
        self.RATIO = 397/271
        self.width = 0
        self.height = 0

        self.phase = ['Draw Phace', 'Standby Phase', 'Main Phase1', 'Battale Phase', 'Main Phase2', 'End Phase']

        self.id = {}
        self.deck = []
        self.hand = []
        self.monsterzone = []
        self.spelltrapzone = []
        self.graveYeard = []
        self.outOfPlay = []
        self.mainDeck = []
        self.extraDeck = []
        self.lifePoints = 8000

        self.opId = {}
        self.opDeck = []
        self.opHand = []
        self.opMonsterzone = []
        self.opSpelltrapzone = []
        self.opGraveYeard = []
        self.opOutOfPlay = []
        self.opMainDeck = []
        self.opExtraDeck = []
        self.opLifePoints = 8000

    def Field(self, x, y, w, h):
        # self.DrawBox(400 + (self.GetHeight() + 30) * n, 20 + (self.GetHeight() + 10) * m)
        self.DrawBox(x + (self.GetHeight() + w) * -1, y + (self.GetHeight() + h) * 0)
        self.DrawBox(x + (self.GetHeight() + w) * 0, y + (self.GetHeight() + h) * 0)
        self.DrawBox(x + (self.GetHeight() + w) * 1, y + (self.GetHeight() + h) * 0)
        self.DrawBox(x + (self.GetHeight() + w) * 2, y + (self.GetHeight() + h) * 0)
        self.DrawBox(x + (self.GetHeight() + w) * 3, y + (self.GetHeight() + h) * 0)
        self.DrawBox(x + (self.GetHeight() + w) * 4, y + (self.GetHeight() + h) * 0)
        self.DrawBox(x + (self.GetHeight() + w) * 5, y + (self.GetHeight() + h) * 0)

        self.DrawBox(x + (self.GetHeight() + w) * -2, y + (self.GetHeight() + h) * 1)
        self.DrawBox(x + (self.GetHeight() + w) * -1, y + (self.GetHeight() + h) * 1)
        self.DrawBox(x + (self.GetHeight() + w) * 0, y + (self.GetHeight() + h) * 1)
        self.DrawBox(x + (self.GetHeight() + w) * 1, y + (self.GetHeight() + h) * 1)
        self.DrawBox(x + (self.GetHeight() + w) * 2, y + (self.GetHeight() + h) * 1)
        self.DrawBox(x + (self.GetHeight() + w) * 3, y + (self.GetHeight() + h) * 1)
        self.DrawBox(x + (self.GetHeight() + w) * 4, y + (self.GetHeight() + h) * 1)
        self.DrawBox(x + (self.GetHeight() + w) * 5, y + (self.GetHeight() + h) * 1)

        self.DrawBox(x + (self.GetHeight() + w) * 1, y + (self.GetHeight() + h) * 2)
        self.DrawBox(x + (self.GetHeight() + w) * 3, y + (self.GetHeight() + h) * 2)

        self.DrawBox(x + (self.GetHeight() + w) * -1, y + (self.GetHeight() + h) * 3)
        self.DrawBox(x + (self.GetHeight() + w) * 0, y + (self.GetHeight() + h) * 3)
        self.DrawBox(x + (self.GetHeight() + w) * 1, y + (self.GetHeight() + h) * 3)
        self.DrawBox(x + (self.GetHeight() + w) * 2, y + (self.GetHeight() + h) * 3)
        self.DrawBox(x + (self.GetHeight() + w) * 3, y + (self.GetHeight() + h) * 3)
        self.DrawBox(x + (self.GetHeight() + w) * 4, y + (self.GetHeight() + h) * 3)
        self.DrawBox(x + (self.GetHeight() + w) * 5, y + (self.GetHeight() + h) * 3)
        self.DrawBox(x + (self.GetHeight() + w) * 6, y + (self.GetHeight() + h) * 3)

        self.DrawBox(x + (self.GetHeight() + w) * -1, y + (self.GetHeight() + h) * 4)
        self.DrawBox(x + (self.GetHeight() + w) * 0, y + (self.GetHeight() + h) * 4)
        self.DrawBox(x + (self.GetHeight() + w) * 1, y + (self.GetHeight() + h) * 4)
        self.DrawBox(x + (self.GetHeight() + w) * 2, y + (self.GetHeight() + h) * 4)
        self.DrawBox(x + (self.GetHeight() + w) * 3, y + (self.GetHeight() + h) * 4)
        self.DrawBox(x + (self.GetHeight() + w) * 4, y + (self.GetHeight() + h) * 4)
        self.DrawBox(x + (self.GetHeight() + w) * 5, y + (self.GetHeight() + h) * 4)

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

        opGetDeck = self.myDB.cursor()
        opGetDeck.execute("SELECT cardId FROM decks WHERE userID = 'yugi' ORDER BY name")
        opCards = opGetDeck.fetchall()
        for i in opCards:
            self.opDeck.append(i[0])
            self.opMainDeck.append(i[0])
        numpy.random.shuffle(self.opMainDeck)

    def GetHand(self):
        hand = 0
        for i in reversed(self.mainDeck):
            if hand == 5:
                break
            self.mainDeck.remove(i)
            self.hand.append(i)
            hand = hand + 1
        return self.hand

    def OpGetHand(self):
        hand = 0
        for i in reversed(self.opMainDeck):
            if hand == 5:
                break
            self.opMainDeck.remove(i)
            self.opHand.append(i)
            hand = hand + 1
        return self.opHand

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

    def OpGetDeckString(self):
        fieldInfo = ''
        n = 0
        for i in self.opDeck:
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

    def MyLifePoint(self, x, y):
        l = 20
        num = 0
        for n in str(self.lifePoints):
            if n == '0':
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + l + num * (l + 10), y), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + 2 * l),(x + l + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y), (x + num * (l + 10) + l, y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y + l),(x + num * (l + 10) + l, y + 2 * l), 1)
            elif n == '1':
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y), (x + num * (l + 10) + l, y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y + l),(x + num * (l + 10) + l, y + 2 * l), 1)
            elif n == '2':
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + l + num * (l + 10), y), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + l + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + 2 * l),(x + l + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y), (x + num * (l + 10) + l, y + l), 1)
            elif n == '3':
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + l + num * (l + 10), y), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + l + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + 2 * l), (x + l + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y), (x + num * (l + 10) + l, y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y + l), (x + num * (l + 10) + l, y + 2 * l), 1)
            elif n == '4':
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + l + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y), (x + num * (l + 10) + l, y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y + l), (x + num * (l + 10) + l, y + 2 * l), 1)
            elif n == '5':
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + l + num * (l + 10), y), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + l + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + 2 * l), (x + l + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y + l), (x + num * (l + 10) + l, y + 2 * l), 1)
            elif n == '6':
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + l + num * (l + 10), y), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + l + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + 2 * l), (x + l + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y + l), (x + num * (l + 10) + l, y + 2 * l), 1)
            elif n == '7':
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + l + num * (l + 10), y), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y), (x + num * (l + 10) + l, y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y + l), (x + num * (l + 10) + l, y + 2 * l), 1)
            elif n == '8':
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + l + num * (l + 10), y), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + l + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + 2 * l), (x + l + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y), (x + num * (l + 10) + l, y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y + l), (x + num * (l + 10) + l, y + 2 * l), 1)
            elif n == '9':
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + l + num * (l + 10), y), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + l), (x + l + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y + 2 * l), (x + l + num * (l + 10), y + 2 * l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10), y), (x + num * (l + 10), y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y), (x + num * (l + 10) + l, y + l), 1)
                pygame.draw.line(self.screen, 'red', (x + num * (l + 10) + l, y + l), (x + num * (l + 10) + l, y + 2 * l), 1)
            num = num + 1
