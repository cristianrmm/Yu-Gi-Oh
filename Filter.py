class Filter():
    def __init__(self, myDB):
        self.mydb = myDB

    def FrameType(self):
        frame = self.mydb.cursor()
        frame.execute("SELECT frameType FROM cards")
        set = ['all']
        for i in self.UniqueSet(frame.fetchall()):
            set.append(i[0])
        return set

    def RaceType(self):
        frame = self.mydb.cursor()
        frame.execute("SELECT race FROM cards WHERE frameType != 'skill' ORDER BY race")
        set = ['all']
        for i in self.UniqueSet(frame.fetchall()):
            set.append(i[0])
        return set

    def Level(self):
        frame = self.mydb.cursor()
        frame.execute("SELECT level FROM cards WHERE level > '0' ORDER BY CAST(level AS SIGNED INTEGER)")
        set = ['all']
        for i in self.UniqueSet(frame.fetchall()):
            set.append(i[0])
        return set


    def ArcheType(self):
        frame = self.mydb.cursor()
        frame.execute("SELECT archetype FROM cards ORDER BY archetype")
        set = ['all']
        for i in self.UniqueSet(frame.fetchall()):
            if i[0] == "":
                set.append('undefined')
            else:
                set.append(i[0])
        return set

    def getAllFrameCards(self, frame):
        card = self.mydb.cursor()
        if frame == 'all':
            card.execute("SELECT id, name, description, frameType, card_index FROM cards")
        else:
            card.execute("SELECT id, name, description, frametype, card_index FROM cards WHERE frameType LIKE '" + frame +"'")
        return card.fetchall()

    def getAllRaceCards(self, race):
        card = self.mydb.cursor()
        if race == 'all':
            card.execute("SELECT id, name, description, frameType, card_index FROM cards")
        else:
            card.execute("SELECT id, name, description, frametype, card_index FROM cards WHERE race LIKE '" + race +"'")
        return card.fetchall()

    def getAllLevelCards(self, level):
        card = self.mydb.cursor()
        if level == 'all':
            card.execute("SELECT id, name, description, frameType, card_index FROM cards")
        else:
            card.execute("SELECT id, name, description, frametype, card_index FROM cards WHERE level LIKE '" + level +"'")
        return card.fetchall()

    def getAllArchCards(self, archetype):
        card = self.mydb.cursor()
        if archetype == 'all':
            card.execute("SELECT id, name, description, frameType, card_index FROM cards")
        elif (archetype == 'undefined'):
            card.execute("SELECT id, name, description, frametype, card_index FROM cards WHERE archetype LIKE ''")
        else:
            card.execute("SELECT id, name, description, frametype, card_index FROM cards WHERE archetype LIKE (%s)",  (archetype,))
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
