class Filter():
    def __init__(self, myDB):
        self.indexFrame = 0
        self.indexArche = 0
        self.indexRace = 0
        self.indexLevel = 0
        self.indexAttribute = 0
        self.indexAttack = 0
        self.indexDefense = 0
        self.frame = 'all'
        self.archeType = 'all'
        self.race = 'all'
        self.level = 'all'
        self.attribute = 'all'
        self.attack = 'all'
        self.defense = 'all'
        self.getMyCards = ['all', 'all', 'all', 'all', 'all', 'all', 'all']
        self.getMyPreviousCards = ['all', 'all', 'all', 'all', 'all', 'all', 'all']
        self.mydb = myDB

    def SetPrevious(self, type,  index, frameType):
        if (type == 'frame'):
            self.getMyPreviousCards[0] = frameType
            self.indexFrame = index
        elif (type == 'arche'):
            self.getMyPreviousCards[1] = frameType
            self.indexArche = index
        elif (type == 'race'):
            self.getMyPreviousCards[2] = frameType
            self.indexRace = index
        elif (type == 'level'):
            self.getMyPreviousCards[3] = frameType
            self.indexLevel = index
        elif (type == 'attribute'):
            self.getMyPreviousCards[4] = frameType
            self.indexAttribute = index
        elif (type == 'attack'):
            self.getMyPreviousCards[5] = frameType
            self.indexAttack = index
        elif (type == 'defense'):
            self.getMyPreviousCards[5] = frameType
            self.indexDefense = index

    def GetPrevious(self, type, frameType):
        if (type == 'frame'):
            self.frame = self.getMyPreviousCards[0]
            return self.indexFrame
        elif (type == 'arche'):
            self.archeType = self.getMyPreviousCards[1]
            return self.indexArche
        elif (type == 'race'):
            self.race = self.getMyPreviousCards[2]
            return self.indexRace
        elif (type == 'level'):
            self.level = self.getMyPreviousCards[3]
            return self.indexLevel
        elif (type == 'attribute'):
            self.attribute = self.getMyPreviousCards[4]
            return self.indexAttribute
        elif (type == 'attack'):
            self.attack = self.getMyPreviousCards[4]
            return self.indexAttack
        elif (type == 'defense'):
            self.defense = self.getMyPreviousCards[4]
            return self.indexDefense

    def FrameType(self):
        cardFrame = self.mydb.cursor()
        cardFrame.execute("SELECT frameType FROM cards")
        set = ['all']
        for i in self.UniqueSet(cardFrame.fetchall()):
            set.append(i[0])
        return set

    def RaceType(self):
        cardFrame = self.mydb.cursor()
        cardFrame.execute("SELECT race FROM cards WHERE frameType != 'skill' ORDER BY race")
        set = ['all']
        for i in self.UniqueSet(cardFrame.fetchall()):
            set.append(i[0])
        return set

    def Level(self):
        cardFrame = self.mydb.cursor()
        cardFrame.execute("SELECT level FROM cards WHERE level > '0' ORDER BY CAST(level AS SIGNED INTEGER)")
        set = ['all']
        for i in self.UniqueSet(cardFrame.fetchall()):
            set.append(i[0])
        return set

    def Attribute(self):
        cardFrame =  self.mydb.cursor()
        cardFrame.execute("SELECT attribute FROM cards")
        set = ['all']
        for i in self.UniqueSet(cardFrame.fetchall()):
            if i[0] == "":
                set.append('undefined')
            else:
                set.append(i[0])
        return set

    def ArcheType(self):
        cardFrame = self.mydb.cursor()
        cardFrame.execute("SELECT archetype FROM cards ORDER BY archetype")
        set = ['all']
        for i in self.UniqueSet(cardFrame.fetchall()):
            if i[0] == "":
                set.append('undefined')
            else:
                set.append(i[0])
        return set

    def Attack(self):
        cardFrame = self.mydb.cursor()
        cardFrame.execute("SELECT atk FROM cards WHERE atk > '0' ORDER BY CAST(atk AS SIGNED INTEGER)")
        set = ['all', '0']
        for i in self.UniqueSet(cardFrame.fetchall()):
            set.append(i[0])
        return set

    def Defense(self):
        cardFrame = self.mydb.cursor()
        cardFrame.execute("SELECT def FROM cards WHERE def > '0' ORDER BY CAST(def AS SIGNED INTEGER)")
        set = ['all', '0']
        for i in self.UniqueSet(cardFrame.fetchall()):
            set.append(i[0])
        return set

    def GetCardInfo(self, cardType, info):
        if cardType == 'frame':
            self.frame = info
        elif cardType == 'arche':
            self.archeType = info
        elif cardType == 'race':
            self.race = info
        elif cardType == 'level':
            self.level = info
        elif cardType == 'attribute':
            self.attribute = info
        elif cardType == 'attack':
            self.attack = info
        elif cardType == 'defense':
            self.defense = info

    def GetAllCards(self):
        card = self.mydb.cursor()
        frame = ''
        archType = ''
        race = ''
        level = ''
        attribute = ''
        attack = ''
        defense = ''
        myset = ''

        set = []
        if (self.frame != 'all'):
            frame = "frameType LIKE '" + self.frame + "'"
            set.append(frame)

        if (self.archeType != 'all' and self.archeType != 'undefined'):
            archType = "archeType LIKE (%s)"
            set.append(archType)
        elif(self.archeType == 'undefined'):
            archType = "archeType LIKE ''"
            set.append(archType)

        if (self.race != 'all'):
            race = "race LIKE '" + self.race + "'"
            set.append(race)

        if (self.level != 'all'):
            level = "level LIKE '" + self.level + "'"
            set.append(level)

        if (self.attack != 'all'):
            attack = "atk LIKE '" + self.attack + "'"
            set.append(attack)

        if (self.defense != 'all'):
            defense = "def LIKE '" + self.defense + "'"
            set.append(defense)

        if (self.attribute != 'all' and self.attribute != 'undefined'):
            attribute = "attribute LIKE '" + self.attribute  + "'"
        elif (self.attribute == 'undefined'):
            attribute = "attribute LIKE ''"

        self.getMyCards[0] = frame
        self.getMyCards[1] = archType
        self.getMyCards[2] = race
        self.getMyCards[3] = level
        self.getMyCards[4] = attribute
        self.getMyCards[5] = attack
        self.getMyCards[6] = defense

        if len(self.getMyCards) > 1:
            n = 0
            for i in self.getMyCards:
                if len(i) > 0 and n == 0:
                    myset = myset + str(i)
                    n = n + 1
                elif len(i) != 0 and n != 0:
                    myset = myset + " AND " + str(i)

        code = "SELECT id, name, description, frameType, card_index FROM cards WHERE " + myset

        if (self.frame == 'all' and self.archeType == 'all' and self.race == 'all' and self.level == 'all' and self.attribute == 'all' and self.attack == 'all' and self.defense == 'all'):
            card.execute("SELECT id, name, description, frameType, card_index FROM cards")
        elif (self.archeType == 'all'):
            card.execute(code)
        elif (self.archeType == 'undefined'):
            card.execute(code)
        else:
            card.execute(code, (self.archeType,))

        return card.fetchall()

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
