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

    def getAllFrameCards(self, frame):
        card = self.mydb.cursor()
        if frame == 'all':
            card.execute("SELECT id, name, description, frameType, card_index FROM cards")
        else:
            card.execute("SELECT id, name, description, frametype, card_index FROM cards WHERE frameType LIKE '" + frame +"'")
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
