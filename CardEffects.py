import math

import numpy.random
import pygame.transform


class CardEffects():
    def __init__(self, myDb):
        self.RATIO = 397 / 271
        self.width = 0
        self.myDb = myDb
        self.id = {}

        self.myLifePoints = [8000, 8000]
        self.myDeck = []
        self.myMainDeck = []

        self.myHand = []
        self.myHandZone = []
        self.myHandImage = []

        self.myMonster = [['empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty']]
        self.myMonsterZone = [['empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty']]
        self.myMonsterImage = [['empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty']]

        self.mySpellTrap = [['empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty']]
        self.mySpellTrapZone = [['empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty']]
        self.mySpellTrapImage = [['empty', 'empty', 'empty', 'empty', 'empty'], ['empty', 'empty', 'empty', 'empty', 'empty']]

        self.myField = [['empty'], ['empty']]
        self.myFieldZone = [['empty'], ['empty']]
        self.myFieldImage = [['empty'], ['empty']]

    def ChangeMyLifePoints(self, n, lifePoint):
        self.myLifePoints[n] = self.myLifePoints + lifePoint
        self.myLifePoints[n] = self.myLifePoints + lifePoint

    def SetPosToCard(self, key, value):
        self.id[key] = value

    def GetPosToCard(self, key):
        return self.id[key]

    def DeleteKey(self, key):
        decriptKey = str(key.topleft[0]) + str(key.topleft[1])
        del self.id[decriptKey]

    def SetMyHand(self, n, myHand):
        if len(self.myHand) == 0:
            self.myHand.append([])
            self.myHand.append([])

        if n == 0:
            self.myHand[0] = myHand
        if n == 1:
            self.myHand[1] = myHand

    def SetMyHandZone(self, n, myHandZone):
        if len(self.myHandZone) == 0:
            self.myHandZone.append([])
            self.myHandZone.append([])

        self.myHandZone[n].append(myHandZone)

    def SetMyHandImage(self, n, myHandImage):
        if len(self.myHandImage) == 0:
            self.myHandImage.append([])
            self.myHandImage.append([])

        self.myHandImage[n].append(myHandImage)

    def DeleteMyHandZoneImage(self):
        self.myHandImage = []
        self.myHandZone = []

    def SetMyMonster(self, n, myMonster):
        if len(self.myMonster) == 0:
            self.myMonster.append([])
            self.myMonster.append([])

        self.myMonster[n] = myMonster

    def SetMyMonsterZone(self, n, myMonsterZone):
        if len(self.myMonsterZone) == 0:
            self.myMonsterZone.append([])
            self.myMonsterZone.append([])

        self.myMonsterZone[n] = myMonsterZone

    def SetMyMonsterImage(self, n, myMonsterImage):
        if len(self.myMonsterImage) == 0:
            self.myMonsterImage.append([])
            self.myMonsterImage.append([])

        self.myMonsterImage[n] = myMonsterImage

    def SetMySpeelTrap(self, n, mySpellTrap):
        if len(self.mySpellTrap) == 0:
            self.mySpellTrap.append([])
            self.mySpellTrap.append([])

        self.mySpellTrap[n] = mySpellTrap

    def SetMySpeelTrapZone(self, n, mySpellTrapZone):
        if len(self.mySpellTrapZone) == 0:
            self.mySpellTrapZone.append([])
            self.mySpellTrapZone.append([])

        self.mySpellTrapZone[n] = mySpellTrapZone

    def SetMySpeelTrapImage(self, n, mySpellTrapImage):
        if len(self.mySpellTrapImage) == 0:
            self.mySpellTrapImage.append([])
            self.mySpellTrapImage.append([])

        self.mySpellTrapImage[n] = mySpellTrapImage

    def SetMyField(self, n, myField):
        if len(self.myField) == 0:
            self.myField.append([])
            self.myField.append([])

        self.myField[n] = myField

    def SetMyFieldZone(self, n, myFieldZone):
        if len(self.myFieldZone) == 0:
            self.myFieldZone.append([])
            self.myFieldZone.append([])

        self.myFieldZone[n] = myFieldZone

    def SetMyFieldImage(self, n, myFieldImage):
        if len(self.myFieldImage) == 0:
            self.myFieldImage.append([])
            self.myFieldImage.append([])

        self.myFieldImage[n] = myFieldImage

    def SetWidth(self, width):
        self.width = width

    def GetCard(self, id):
        myCursor = self.myDb.cursor()
        myCursor.execute("SELECT * FROM cards WHERE id = '" + id + "'")
        cardInfo = myCursor.fetchall()
        return cardInfo

    def GetWidth(self):
        return self.width

    def GetHeight(self):
        return math.floor(self.RATIO * self.width)

    def GetLifePoints(self):
        return self.myLifePoints

    def GetMyDeck(self):
        return self.myDeck

    def GetMyMainDeck(self):
        return self.myMainDeck

    def GetMyHand(self):
        return self.myHand

    def GetMyHandZone(self):
        return self.myHandZone

    def GetMyHandImage(self):
        return self.myHandImage

    def GetMyMonster(self):
        return self.myMonster

    def GetMyMonsterZone(self):
        return self.myMonsterZone

    def GetMyMonsterImage(self):
        return self.myMonsterImage

    def GetMySpellTrap(self):
        return self.mySpellTrap

    def GetMySpellTrapZone(self):
        return self.mySpellTrapZone

    def GetMySpellTrapImage(self):
        return self.mySpellTrapImage

    def GetMyField(self):
        return self.myField

    def GetMyFieldZone(self):
        return self.myFieldZone

    def GetMyFieldImage(self):
        return self.myFieldImage

    def Command(self, player, command, card):
        print(card)
        print(self.myHand)
        print(self.myHandZone)
        print(self.myHandImage)
        print(len(self.id), self.id)



        if command == 'Summon':
            if (card[3] in ['effect', 'normal']):
                if (card[9] in ['1', '2', '3', '4']):
                    for i in self.myHand[player]:
                        del self.id[str(self.myHandZone[player][self.myHand[player].index(i)].topleft[0]) + str(self.myHandZone[player][self.myHand[player].index(i)].topleft[1])]
                    self.myHand[player].remove(str(card[0]))
                    n = -1
                    for i in reversed(self.myMonster[player]):
                        if i == 'empty':
                            self.myMonster[player][n] = card[0]
                            break
                        n = n - 1
                    n = 0
                    for i in self.myMonster[player]:
                        if i != 'empty':
                            self.myMonsterImage[player][n] = (pygame.image.load('images/'+ str(i) + '.jpg'))
                            self.myMonsterImage[player][n] = pygame.transform.scale(self.myMonsterImage[player][n], (self.GetWidth(), self.GetHeight()))
                            self.myMonsterZone[player][n] = self.myMonsterImage[player][n].get_rect()
                            self.myMonsterZone[player][n].topleft = (1044 - (4-n) * 161, 513)
                            self.SetPosToCard(str(1044 - (4-n) * 161) + str(513), str(i))
                        n = n + 1

    def SetDeck(self):
        getDeck = self.myDb.cursor()
        getDeck.execute("SELECT cardId FROM decks WHERE userID = 'yugi' ORDER BY name")
        cards = getDeck.fetchall()

        self.myDeck.append([])
        self.myMainDeck.append([])
        for i in cards:
            self.myDeck[0].append(i[0])
            self.myMainDeck[0].append(i[0])
        numpy.random.shuffle(self.myMainDeck[0])

        getDeck.execute("SELECT cardId FROM decks WHERE userID = 'yugi' ORDER BY name")
        cards = getDeck.fetchall()
        self.myDeck.append([])
        self.myMainDeck.append([])
        for i in cards:
            self.myDeck[1].append(i[0])
            self.myMainDeck[1].append(i[0])
        numpy.random.shuffle(self.myMainDeck[1])

    def SetHand(self):
        hand = 0
        myHand = []
        for i in reversed(self.myMainDeck[0]):
            if hand == 5:
                break
            elif len(self.myHand) > 0:
                if len(self.myHand[len(self.myHand) - 1] == 5):
                    break
            self.myMainDeck[0].remove(i)
            myHand.append(i)
            hand = hand + 1
        self.myHand.append(myHand)
