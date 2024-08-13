import math

import numpy.random
import pygame.transform


class CardEffects():
    def __init__(self, myDb):
        self.RATIO = 397 / 271
        self.width = 0
        self.myDb = myDb
        self.id = {}
        self.choice = False
        self.sacrifice = 0
        self.fieldInfo = [[], []]
        self.fieldInfoEncode = []

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

    def SummonSetCard(self, player, card):
        if card[9] in ['1', '2', '3', '4']:
            return True
        elif card[9] in ['5', '6']:
            if self.myMonster[player].count('empty') < 5:
                return True
            else:
                return False
        elif card[9] in ['7', '8', '9', '10', '11', '12']:
            if self.myMonster[player].count('empty') < 4:
                return True
            else:
                return False
        else:
            return False

    def Command(self, player, command, card):
        if player == 0:
            command[1] = int((command[1].topleft[0] - 400) / 101)
        if command[0] in ['Summon', 'Set'] and card[3] in ['effect', 'normal']:
            chose = True
            index = -1
            n = 0
            if card[9] in ['1', '2', '3', '4']:
                chose = False
            while chose:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        for i in self.myMonsterZone[player]:
                            if i != 'empty':
                                if i .collidepoint(pos):
                                    cardPos = i.topleft
                                    if (card[9] in ['5', '6']) and self.myMonster[player].count('empty') < 5:
                                        if cardPos[1] == 513:
                                            command.append(int((cardPos[0] - 400) / 161))
                                            chose = False
                                        elif cardPos[1] == 533:
                                            command.append(int((cardPos[0] - 380) / 161))
                                            chose = False
                                    elif (card[9] in ['7', '8', '9', '10', '11', '12'] and self.myMonster[player].count('empty') < 4):
                                        if cardPos[1] == 513:
                                            if not (index == int((cardPos[0] - 400) / 161)):
                                                command.append(int((cardPos[0] - 400) / 161))
                                                n = n + 1
                                                index = int((cardPos[0] - 400) / 161)
                                                if n == 2:
                                                    chose = False
                                        elif cardPos[1] == 533:
                                            if not (index == int((cardPos[0] - 380) / 161)):
                                                command.append(int((cardPos[0] - 380) / 161))
                                                n = n + 1
                                                index = int((cardPos[0] - 380) / 161)
                                                if n == 2:
                                                    chose = False

        while(len(command) < 4):
            command.append(-1)

        print('ok', self.fieldInfo[player])
        self.Save(player, command)

        command = self.Decoder(player, command)
        self.MainCommand(player, command)

    def Convert(self, fieldInfo):
        dataFieldInfo = []
        item = ['D', 'H', 'FUA', 'FDD']

        for i in fieldInfo:
            if i in item:
                dataFieldInfo.append(str(20600 + item.index(i)))
            elif i.startswith('H'):
                dataFieldInfo.append(str(20900 + int(i[1:])))
            elif i.startswith('FUA'):
                dataFieldInfo.append(str(20800 + int(i[3:])))
            elif i.startswith('FDD'):
                dataFieldInfo.append(str(20810 + int(i[3:])))
            elif i == 'G':
                dataFieldInfo.append(str(21000 + int(self.fieldInfo.count('G'))))
            else:
                dataFieldInfo.append(i)

        while len(dataFieldInfo) < 720:
            dataFieldInfo.append(str(20000))
        print(len(dataFieldInfo))
        return dataFieldInfo

    def Save(self, player, command):
        commandSave = []
        for i in command:
            commandSave.append(str(i))
        com = ':'.join(commandSave)
        data = self.Convert(self.fieldInfo[player])
        print('data: ', data)
        fieldInfo = ':'.join(data)
        myCursor = self.myDb.cursor()
        sql = """CREATE TABLE IF NOT EXISTS all_dual(field_Input TEXT,
                                                     field_Output TEXT,
                                                     dual_index INT AUTO_INCREMENT PRIMARY KEY
                                                     )
                 """
        myCursor.execute(sql)

        info = """INSERT INTO all_dual(field_Input,
                                       field_Output
                                       ) VALUES(%s, %s)
                         """
        myCursor.execute(info, (fieldInfo, com))
        self.myDb.commit()



    def Decoder(self, player, newCommand):
        command = []
        command.append(newCommand[0])
        command.append(newCommand[1])
        if command[0] in ['Summon', 'Set']:
            if (newCommand.count(-1) <= 2):
                command.append(self.GetCardDetail(self.myHand[player][newCommand[1]]))
            if (newCommand.count(-1) <= 1):
                command.append(newCommand[2])
                command.append(self.GetCardDetail(self.myMonster[player][newCommand[2]]))
            if (newCommand.count(-1) == 0):
                command.append(newCommand[3])
                command.append(self.GetCardDetail(self.myMonster[player][newCommand[3]]))
        return command

    def MainCommand(self, player, command):
        if command[0] == 'Summon':
            if len(command) == 3 and command[2][9] in ['1', '2', '3', '4']:
                self.NormalSummon(command, player)
            elif len(command) == 5 and command[2][9] in ['5', '6']:
                self.FieldToGraveyard(player, command, 3)
                self.myMonster[player][command[3]] = 'empty'
                self.myMonsterImage[player][command[3]] = 'empty'
                self.myMonsterZone[player][command[3]] = 'empty'
                self.NormalSummon(command, player)
            elif len(command) == 7 and command[2][9] in ['7', '8', '9', '10', '11', '12']:
                self.FieldToGraveyard(player, command, 3)
                self.myMonster[player][command[3]] = 'empty'
                self.myMonsterImage[player][command[3]] = 'empty'
                self.myMonsterZone[player][command[3]] = 'empty'

                self.FieldToGraveyard(player, command, 5)
                self.myMonster[player][command[5]] = 'empty'
                self.myMonsterImage[player][command[5]] = 'empty'
                self.myMonsterZone[player][command[5]] = 'empty'

                self.NormalSummon(command, player)
        if command[0] == 'Set':
            if len(command) == 3 and command[2][9] in ['1', '2', '3', '4']:
                self.NormalSet(command, player)
            elif len(command) == 5 and command[2][9] in ['5', '6']:
                self.FieldToGraveyard(player, command, 3)
                self.myMonster[player][command[3]] = 'empty'
                self.myMonsterImage[player][command[3]] = 'empty'
                self.myMonsterZone[player][command[3]] = 'empty'
                self.NormalSet(command, player)
            elif len(command) == 7 and command[2][9] in ['7', '8', '9', '10', '11', '12']:
                self.FieldToGraveyard(player, command, 3)
                self.myMonster[player][command[3]] = 'empty'
                self.myMonsterImage[player][command[3]] = 'empty'
                self.myMonsterZone[player][command[3]] = 'empty'

                self.FieldToGraveyard(player, command, 5)
                self.myMonster[player][command[5]] = 'empty'
                self.myMonsterImage[player][command[5]] = 'empty'
                self.myMonsterZone[player][command[5]] = 'empty'
                self.NormalSet(command, player)

    def FieldToGraveyard(self, player, command, index):
        if self.GetPosCard(player, 'FDD' + str(4 - command[index]), str(self.myMonster[player][command[index]])) == None:
            self.fieldInfo[player][self.GetPosCard(player, 'FUA' + str(4 - command[index]), str(self.myMonster[player][command[index]]))] = 'G'
        elif self.GetPosCard(player, 'FUA' + str(4 - command[index]), str(self.myMonster[player][command[index]])) == None:
            self.fieldInfo[player][self.GetPosCard(player, 'FDD' + str(4 - command[index]), str(self.myMonster[player][command[index]]))] = 'G'

    def NormalSummon(self, command, player):
        card = command[2]
        h = (self.GetHeight() - self.GetWidth()) / 2

        for i in self.myHand[player]:
            del self.id[str(self.myHandZone[player][self.myHand[player].index(i)].topleft[0]) + str(self.myHandZone[player][self.myHand[player].index(i)].topleft[1])]
        self.myHand[player].remove(str(card[0]))

        n = 0
        for i in self.myHand[player]:
            self.SetPosToCard(str(self.myHandZone[player][n].topleft[0]) + str(self.myHandZone[player][n].topleft[1]),i)
            n = n + 1

        item = 0
        for i in reversed(self.myMonster[player]):
            if i == 'empty':
                break
            else:
                item = item + 1
        n = -1
        for i in reversed(self.myMonster[player]):
            if i == 'empty':
                self.myMonster[player][n] = card[0]
                self.fieldInfo[player][self.GetPosCard(player, 'H' + str(command[1]), str(card[0]))] = 'FUA' + str(item)
                break
            n = n - 1

        s = command[1]
        while (s < len(self.myHand[player])):
            self.fieldInfo[player][self.fieldInfo[player].index('H' + str(s + 1))] = 'H' + str(s)
            s = s + 1

        self.myMonsterImage[player][n] = (pygame.image.load('images/' + str(self.myMonster[player][n]) + '.jpg'))
        n = n + 5
        self.myMonsterImage[player][n] = pygame.transform.scale(self.myMonsterImage[player][n],(self.GetWidth(), self.GetHeight()))
        self.myMonsterZone[player][n] = self.myMonsterImage[player][n].get_rect()
        self.myMonsterZone[player][n].topleft = (1044 - (4 - n) * 161, 513)
        self.SetPosToCard(str(1044 - (4 - n) * 161) + str(513), str(self.myMonster[player][n]))

    def NormalSet(self, command, player):
        card = command[2]
        h = (self.GetHeight() - self.GetWidth()) / 2

        for i in self.myHandZone[player]:
            del  self.id[str(i.topleft[0]) + str(i.topleft[1])]

        self.myHand[player].remove(str(card[0]))
        n = 0
        for i in self.myHand[player]:
            self.SetPosToCard(str(self.myHandZone[player][n].topleft[0]) + str(self.myHandZone[player][n].topleft[1]), i)
            n = n + 1

        item = 0
        for i in reversed(self.myMonster[player]):
            if i == 'empty':
                break
            else:
                item = item + 1

        n = -1
        for i in reversed(self.myMonster[player]):
            if i == 'empty':
                self.myMonster[player][n] = card[0]
                self.fieldInfo[player][self.GetPosCard(player,'H' + str(command[1]), str(card[0]))] = 'FDD' + str(item)
                break
            n = n - 1

        s = command[1]
        while (s < len(self.myHand[player])):
            self.fieldInfo[player][self.fieldInfo[player].index('H' + str(s + 1))] = 'H' + str(s)
            s = s + 1

        self.myMonsterImage[player][n] = (pygame.image.load('images/' + '000' + '.png'))
        n = n + 5
        self.myMonsterImage[player][n] = pygame.transform.scale(self.myMonsterImage[player][n],(self.GetWidth(), self.GetHeight()))
        self.myMonsterImage[player][n] = pygame.transform.rotate(self.myMonsterImage[player][n], 90)
        self.myMonsterZone[player][n] = self.myMonsterImage[player][n].get_rect()
        self.myMonsterZone[player][n].topleft = (1044 - (4 - n) * 161 - int(h), 513 + int(h))
        self.SetPosToCard(str(1044 - (4 - n) * 161 - int(h)) + str(513 + int(h)), str(self.myMonster[player][n]))

    def SetDeck(self):
        getDeck = self.myDb.cursor()
        getDeck.execute("SELECT cardId FROM decks WHERE userID = 'Starter Deck Yugi' ORDER BY name")
        cards = getDeck.fetchall()

        self.myDeck.append([])
        self.myMainDeck.append([])
        for i in cards:
            self.myDeck[0].append(i[0])
            self.myMainDeck[0].append(i[0])
        numpy.random.shuffle(self.myMainDeck[0])
        self.GetCardInfo(0)

        getDeck.execute("SELECT cardId FROM decks WHERE userID = 'Starter Deck Yugi' ORDER BY name")
        cards = getDeck.fetchall()
        self.myDeck.append([])
        self.myMainDeck.append([])
        for i in cards:
            self.myDeck[1].append(i[0])
            self.myMainDeck[1].append(i[0])
        numpy.random.shuffle(self.myMainDeck[1])
        self.GetCardInfo(1)

    def GetCardDetail(self, id):
        mydb = self.myDb.cursor()
        mydb.execute("SELECT * FROM cards WHERE id = '" + str(id) + "'" )
        return mydb.fetchall()[0]

    def GetCardInfo(self, player):
        allCardInfo = self.myDb.cursor()
        item2 = self.GetCardType("frameType")
        item3 = self.GetCardType("race")
        item4 = self.GetCardType("archetype")
        item5 = self.GetCardType("attribute")
        item6 = self.GetCardType("linkmarkers")
        for i in self.myDeck[0]:
            allCardInfo.execute("SELECT id, frameType, race, archetype, atk, def, level, attribute, scale, linkval, linkmarkers FROM cards WHERE id = '" + i + "'")
            item = allCardInfo.fetchall()[0]
            self.fieldInfo[player].append("D")
            for i in item:
                if i == "":
                    self.fieldInfo[player].append("20000")
                else:
                    if str(i) in item2:
                        self.fieldInfo[player].append(str(20100 + item2.index(str(i))))
                    elif str(i) in item3:
                        self.fieldInfo[player].append(str(20200 + item3.index(str(i))))
                    elif str(i) in item4:
                        self.fieldInfo[player].append(str(20300 + item4.index(str(i))))
                    elif str(i) in item5:
                        self.fieldInfo[player].append(str(20400 + item5.index(str(i))))
                    elif str(i) in item6:
                        self.fieldInfo[player].append(str(20500 + item6.index(str(i))))
                    else:
                        self.fieldInfo[player].append(str(i))

    def GetCardType(self, frameType):
        myDb = self.myDb.cursor()
        myDb.execute("SELECT " + frameType + " FROM cards ORDER BY " + frameType)
        items =  self.UniqueSet(myDb.fetchall())

        item = []
        for i in items:
            item.append(i[0])
        return item


    def SetHand(self):
        hand = 0
        myHand = []
        for i in reversed(self.myMainDeck[0]):
            if hand == 5:
                break
            elif len(myHand) > 0:
                if len(myHand[len(myHand) - 1]) == 5:
                    break
            self.myMainDeck[0].remove(i)
            myHand.append(i)
            self.fieldInfo[0][self.GetPosCard(0, 'D', i)] = 'H' + str(hand)
            hand = hand + 1
        self.myHand.append(myHand)
        hand = 0
        myHand = []
        for i in reversed(self.myMainDeck[1]):
            if hand == 5:
                break
            elif len(myHand) > 0:
                if len(myHand[len(myHand) - 1]) == 5:
                    break
            self.myMainDeck[1].remove(i)
            myHand.append(i)
            self.fieldInfo[1][self.GetPosCard(1, 'D', i)] = 'H' + str(hand)
            hand = hand + 1
        self.myHand.append(myHand)

    def GetPosCard(self, player, Pos, cardId):
        n = 0
        while n < len(self.fieldInfo[player]):
            if self.fieldInfo[player][n] == Pos and self.fieldInfo[player][n + 1] == cardId:
                return n
            n = n + 12

    def UniqueSet(self, cardsInfo):
        count = len(cardsInfo)
        n = 0
        j = 0
        myset = [cardsInfo[0]]
        match = 0
        same = True
        while n < count:
            while j < len(myset):
                if (myset[j] == cardsInfo[n]):
                    match = match + 1
                j = j + 1
            if (match == 0):
                myset.append(cardsInfo[n])
            match = 0
            j = 0
            n = n + 1

        return myset
