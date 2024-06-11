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

        self.fieldInfo = ''

        self.id = {}
        self.deck = []
        self.hand = []
        self.monsters = []
        self.monsterImage = []
        self.monsterzone = []
        self.spelltrapzone = []
        self.fieldZone = []
        self.graveYeard = []
        self.outOfPlay = []
        self.mainDeck = []
        self.extraDeck = []
        self.lifePoints = 8000

        self.opId = {}
        self.opDeck = []
        self.opHand = []
        self.opMonsterzone = []
        self.opGraveYeard = []
        self.opOutOfPlay = []
        self.opSpelltrapzon = []
        self.opFieldZone = []
        self.opMainDeck = []
        self.opExtraDeck = []
        self.opLifePoints = 8000
        self.screen = pygame.display.set_mode((0, 0))

    def command(self, screen, myHand, myCardHand, command, card, monsterImage, monsterZone, spellTrap, spellTrapZone, fieldImage, fieldZone):
        h = (self.GetHeight() - self.GetWidth()) / 2
        if command == 'Summon':
            self.ChangeCardSet(str(card[0]), 'H', 'FAP')
            for i in self.hand:
                del self.id[str(myCardHand[self.hand.index(i)].topleft[0]) + str(myCardHand[self.hand.index(i)].topleft[1])]
            myHand.remove(myHand[(self.hand.index(str(card[0])))])
            myCardHand.remove(myCardHand[(self.hand.index(str(card[0])))])
            self.hand.remove(str(card[0]))
            self.monsters.append(str(card[0]))

            n = 0
            for i in self.monsters:
                if (str(1044 - n * 161 - int(h)) + str(513 + int(h)) not in self.id):
                    monsterImage.append(pygame.image.load('images/' + i + '.jpg'))
                    monsterImage[len(monsterImage) - 1] = pygame.transform.scale(monsterImage[len(monsterImage) - 1], (self.GetWidth(), self.GetHeight()))
                    monsterZone.append(monsterImage[len(monsterImage) - 1].get_rect())
                    monsterZone[len(monsterZone) - 1].topleft = (1044 - n * 161, 513)
                    self.SetPosToCard(str(1044 - n * 161) + str(513), i)
                n = n + 1

        elif command == 'Set':
            if card[3] in ['normal', 'effect']:
                self.ChangeCardSet(str(card[0]), 'H', 'FDP')
                for i in self.hand:
                    del self.id[str(myCardHand[self.hand.index(i)].topleft[0]) + str(myCardHand[self.hand.index(i)].topleft[1])]
                myHand.remove(myHand[(self.hand.index(str(card[0])))])
                myCardHand.remove(myCardHand[(self.hand.index(str(card[0])))])
                self.hand.remove(str(card[0]))
                self.monsters.append(str(card[0]))
                n = 0
                for i in self.monsters:
                    if (str(1044 - n * 161) + str(513) not in self.id):
                        monsterImage.append(pygame.image.load('images/' + '000' + '.png'))
                        monsterImage[len(monsterImage) - 1] = pygame.transform.scale(monsterImage[len(monsterImage) - 1],(self.GetWidth(), self.GetHeight()))
                        monsterImage[len(monsterImage) - 1] = pygame.transform.rotate(monsterImage[len(monsterImage) - 1], 270)
                        monsterZone.append(monsterImage[len(monsterImage) - 1].get_rect())
                        monsterZone[len(monsterZone) - 1].topleft = (1044 - n * 161 - int(h), 513 + int(h))
                        self.SetPosToCard(str(1044 - n * 161 - int(h)) + str(513 + int(h)), i)
                    n = n + 1

            elif card[3] in ['spell', 'trap']:
                if card[5] != 'Field':
                    self.ChangeCardSet(str(card[0]), 'H', 'FD')
                    for i in self.hand:
                        del self.id[str(myCardHand[self.hand.index(i)].topleft[0]) + str(myCardHand[self.hand.index(i)].topleft[1])]
                    myHand.remove(myHand[(self.hand.index(str(card[0])))])
                    myCardHand.remove(myCardHand[(self.hand.index(str(card[0])))])
                    self.hand.remove(str(card[0]))
                    self.spelltrapzone.append(str(card[0]))
                    n = 0
                    for i in self.spelltrapzone:
                        if ((str(1044 - n * 161) + str(654)) not in self.id):
                            spellTrap.append(pygame.image.load('images/' + '000' + '.png'))
                            spellTrap[len(spellTrap) - 1] = pygame.transform.scale(spellTrap[len(spellTrap) - 1],(self.GetWidth(), self.GetHeight()))
                            spellTrapZone.append(spellTrap[len(spellTrap) - 1].get_rect())
                            spellTrapZone[len(spellTrapZone) - 1].topleft = (1044 - n * 161, 654)
                            self.SetPosToCard(str(1044 - n * 161) + str(654), i)
                        n = n + 1
                else:
                    self.ChangeCardSet(str(card[0]), 'H', 'FD')
                    for i in self.hand:
                        del self.id[str(myCardHand[self.hand.index(i)].topleft[0]) + str(
                            myCardHand[self.hand.index(i)].topleft[1])]
                    myHand.remove(myHand[(self.hand.index(str(card[0])))])
                    myCardHand.remove(myCardHand[(self.hand.index(str(card[0])))])
                    self.hand.remove(str(card[0]))
                    self.fieldZone.append(str(card[0]))
                    n = 0
                    for i in self.fieldZone:
                        if ((str(1044 - n * 161) + str(654)) not in self.id):
                            fieldImage.append(pygame.image.load('images/' + '000' + '.png'))
                            fieldImage[len(fieldImage) - 1] = pygame.transform.scale(fieldImage[len(fieldImage) - 1],(self.GetWidth(), self.GetHeight()))
                            fieldZone.append(fieldImage[len(fieldImage) - 1].get_rect())
                            fieldZone[len(fieldZone) - 1].topleft = (239, 513)
                            self.SetPosToCard(str(239) + str(513), i)
                        n = n + 1

        elif command == 'Activate':
            if card[5] != 'Field':
                self.ChangeCardSet(str(card[0]), 'H', 'A')
                for i in self.hand:
                    del self.id[str(myCardHand[self.hand.index(i)].topleft[0]) + str(myCardHand[self.hand.index(i)].topleft[1])]
                myHand.remove(myHand[(self.hand.index(str(card[0])))])
                myCardHand.remove(myCardHand[(self.hand.index(str(card[0])))])
                self.hand.remove(str(card[0]))
                self.spelltrapzone.append(str(card[0]))
                n = 0
                for i in self.spelltrapzone:
                    if ((str(1044 - n * 161) + str(654)) not in self.id):
                        spellTrap.append(pygame.image.load('images/' + i + '.jpg'))
                        spellTrap[len(spellTrap) - 1] = pygame.transform.scale(spellTrap[len(spellTrap) - 1],(self.GetWidth(), self.GetHeight()))
                        spellTrapZone.append(spellTrap[len(spellTrap) - 1].get_rect())
                        spellTrapZone[len(spellTrapZone) - 1].topleft = (1044 - n * 161, 654)
                        self.SetPosToCard(str(1044 - n * 161) + str(654), i)
                    n = n + 1
            else:
                self.ChangeCardSet(str(card[0]), 'H', 'FD')
                for i in self.hand:
                    del self.id[str(myCardHand[self.hand.index(i)].topleft[0]) + str(
                        myCardHand[self.hand.index(i)].topleft[1])]
                myHand.remove(myHand[(self.hand.index(str(card[0])))])
                myCardHand.remove(myCardHand[(self.hand.index(str(card[0])))])
                self.hand.remove(str(card[0]))
                self.fieldZone.append(str(card[0]))
                n = 0
                for i in self.fieldZone:
                    if ((str(1044 - n * 161) + str(654)) not in self.id):
                        fieldImage.append(pygame.image.load('images/' + i + '.jpg'))
                        fieldImage[len(fieldImage) - 1] = pygame.transform.scale(fieldImage[len(fieldImage) - 1],
                                                                                 (self.GetWidth(), self.GetHeight()))
                        fieldZone.append(fieldImage[len(fieldImage) - 1].get_rect())
                        fieldZone[len(fieldZone) - 1].topleft = (239, 513)
                        self.SetPosToCard(str(239) + str(513), i)
                    n = n + 1


    def GetCard(self, id):
        myCursor = self.myDB.cursor()
        myCursor.execute("SELECT * FROM cards WHERE id = '" + id + "'")
        cardInfo = myCursor.fetchall()
        return cardInfo

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

    def GetId(self):
        return self.id

    def DeleteKey(self, key):
        decriptKey = str(key.topleft[0]) + str(key.topleft[1])
        del self.id[decriptKey]

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
        index = 0
        for i in reversed(self.mainDeck):
            if hand == 5:
                break
            self.mainDeck.remove(i)
            self.hand.append(i)
            self.ChangeCardSet(i, 'D', 'H')
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

    def ChangeCardSet(self, i, original, newSet):
        index = 0
        fieldInfo = self.fieldInfo.split(':')
        for j in fieldInfo:
            if original + ',' + i == j:
                fieldInfo[index] = newSet + ',' + i
                self.fieldInfo = ':'.join(fieldInfo)
                break
            index = index + 1

    def GetDeckString(self):
        n = 0
        for i in self.deck:
            if n > 0:
                self.fieldInfo = self.fieldInfo + ':D,' + i
            else:
                self.fieldInfo = self.fieldInfo + 'D,' + i
                n = n + 1

    def OpGetDeckString(self):
        fieldInfo = ''
        n = 0
        for i in self.opDeck:
            if n > 0:
                fieldInfo = fieldInfo + ':' + i
            else:
                fieldInfo = fieldInfo + i
                n = n + 1

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
