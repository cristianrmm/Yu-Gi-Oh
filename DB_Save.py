from tkinter import *

class DB_Save():
    def __init__(self, myDB, deck, deckNPC):
        self.myDb = myDB
        self.deck = deck
        self.deckNPC = deckNPC
        self.card = []

    def GetDeckName(self):
        return self.deck['text']

    def SetDeck(self, deck):
        self.card = deck

    def DB_CreateTable(self):
        my_cursor = self.myDb.cursor()

        sqlCode = """CREATE TABLE IF NOT EXISTS Decks(
                    userId VARCHAR(20),
                    cardID VARCHAR(15),
                    name VARCHAR(127),
                    cardPosition VARCHAR(5),
                    cardIndex INT(5)
                    )
                    """
        my_cursor.execute(sqlCode)
        self. myDb.commit()
        my_cursor.close()

    def NewDeck(self):
        choice = Tk()

        ok = Button(choice, text='ok')
        ok.grid(row=0, column=0)

        name = Entry(choice)
        name.grid(row=0, column=1)

        ok.bind('<Button-1>', lambda Event: self.NewName(Event, choice, name))

    def NewName(self, Event, choice, name):
        for i in self.deckNPC.get_children():
            self.deckNPC.delete(i)
        self.deck.config(text=name.get())
        self.deckNPC.insert(parent='', index=100, iid=100, text='Deck')
        self.deckNPC.insert(parent='', index=200, iid=200, text='Extra')
        choice.destroy()

    def DB_Save(self):
        save = self.myDb.cursor()
        save.execute("DELETE FROM decks WHERE userId = '" + self.deck['text'] + "'")
        n = 0
        for i in self.card:
            sqlSave = """INSERT INTO decks(userId,
                                           cardID,
                                           name,
                                           cardPosition,
                                           cardIndex
                                           )VALUES(%s, %s, %s, %s, %s)
            
                    """
            save.execute(sqlSave, (self.deck['text'], str(i[0]), str(i[1]), str(i[2]), str(n)))
            n = n + 1
        self.myDb.commit()
        save.close()
