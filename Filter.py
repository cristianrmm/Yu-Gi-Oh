class Filter():
    def __init__(self, myDB):
        self.frame = 'all'
        self.archType = 'all'
        self.race = 'all'
        self.level = 'all'
        self.getMyCards = ['all', 'all', 'all', 'all']
        self.mydb = myDB

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

    def GetFrame(self, frame):
        self.frame = frame

    def GetArchType(self, archType):
        self.archType = archType

    def GetRace(self, race):
        self.race = race

    def GetLevel(self, level):
        self.level = level

    def GetAllCards(self):
        card = self.mydb.cursor()
        frame = ''
        archType = ''
        race = ''
        level = ''
        myset = ''

        set = []
        if (self.frame != 'all'):
            frame = "frameType LIKE '" + self.frame + "'"
            set.append(frame)
        if (self.archType != 'all' and self.archType != 'undefined'):
            archType = "archeType LIKE (%s)"
            set.append(archType)
        elif(self.archType == 'undefined'):
            archType = "archeType LIKE ''"
            set.append(archType)
        if (self.race != 'all'):
            race = "race LIKE '" + self.race + "'"
            set.append(race)
        if (self.level != 'all'):
            level = "level LIKE '" + self.level + "'"
            set.append(level)

        self.getMyCards[0] = frame
        self.getMyCards[1] = archType
        self.getMyCards[2] = race
        self.getMyCards[3] = level

        if len(self.getMyCards) > 1:
            n = 0
            for i in self.getMyCards:
                if len(i) > 0 and n == 0:
                    myset = myset + str(i)
                    n = n + 1
                elif len(i) != 0 and n != 0:
                    myset = myset + " AND " + str(i)

        if (self.frame == 'all' and self.archType == 'all' and self.race == 'all' and self.level == 'all'):
            card.execute("SELECT id, name, description, frameType, card_index FROM cards")
        elif (self.archType == 'all'):
            card.execute("SELECT id, name, description, frameType, card_index FROM cards WHERE " + myset)
        elif (self.archType == 'undefined'):
            card.execute("SELECT id, name, description, frameType, card_index FROM cards WHERE " + myset)
        else:
            card.execute("SELECT id, name, description, frameType, card_index FROM cards WHERE " + myset, (self.archType,))

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
