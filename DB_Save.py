import tkinter.messagebox
from tkinter import ttk
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
        choice.attributes('-topmost', True)
        ok = Button(choice, text='ok')
        ok.grid(row=0, column=0)

        name = Entry(choice)
        name.grid(row=0, column=1)

        ok.bind('<Button-1>', lambda Event: self.NewName(Event, choice, name))

    def NewName(self, Event, choice, name):
        my_cursor = self.myDb.cursor()

        my_cursor.execute("SELECT userId FROM decks")
        userDeck = my_cursor.fetchall()
        users = [[0]]
        if (len(userDeck) > 0):
            users = self.UniqueSet(userDeck)

        if (name.get() not in users[0]):
            for i in self.deckNPC.get_children():
                self.deckNPC.delete(i)
            self.deck.config(text=name.get())
            self.deckNPC.insert(parent='', index=100, iid=100, text='Deck')
            self.deckNPC.insert(parent='', index=200, iid=200, text='Extra')
            choice.destroy()
        else:
            tkinter.messagebox.showwarning(title='User Name', message='The user name already exist')

    def DB_Save(self):
        save = self.myDb.cursor()
        save.execute("DELETE FROM decks WHERE userId = '" + self.deck['text'] + "'")
        self.myDb.commit()
        n = 0
        for i in self.card:
            sqlSave = """INSERT INTO decks(userId,
                                           cardID,
                                           name,
                                           cardPosition,
                                           cardIndex
                                           )VALUES(%s, %s, %s, %s, %s)
            
                    """
            save.execute(sqlSave, (self.deck['text'], str(i[0]), str(i[1]), str(i[2]), str(i[3])))
            n = n + 1
        self.myDb.commit()
        save.close()

    def Open(self):
        my_cursor = self.myDb.cursor()
        my_cursor.execute('SELECT userId FROM decks')
        fetchAll = my_cursor.fetchall()

        if len(fetchAll) > 0:
            allUsers = self.UniqueSet(fetchAll)

            openDeck = Tk()
            submit = Button(openDeck, text='Open')
            openDeck.attributes('-topmost', True)
            cards = ttk.Treeview(openDeck)
            cards['columns'] = ('User',)
            cards.column('#0')
            cards.column('User', anchor=CENTER)
            cards.heading('#0')
            cards.heading('User', text='User')
            cards.grid(row=0, column=0)
            submit.grid(row=1, column=0)
            submit.bind('<Button-1>', lambda Event: self.OpenDeck(cards, openDeck))

            n = 0
            for i in allUsers:
                cards.insert(parent='', index='end', iid=n, text=str(n), values=i)
                n = n + 1
        else:
            tkinter.messagebox.showwarning(title='Decks', message='There does not exist any decks')

    def OpenDeck(self, cards, openDeck):
        user = cards.selection()
        for i in self.deckNPC.get_children():
            self.deckNPC.delete(i)
        self.deckNPC.insert(parent='', index=100, iid=100, text='Deck')
        self.deckNPC.insert(parent='', index=200, iid=200, text='Extra')

        my_cursor = self.myDb.cursor()
        my_cursor.execute("SELECT * FROM decks WHERE userId = '" + cards.item(user)['values'][0] + "'")
        userCards = my_cursor.fetchall()

        self.deck.config(text=cards.item(user)['values'][0])

        for i in userCards:
            self.deckNPC.insert(parent='100', index='end', iid=int(i[4]) - 100, text='', values=(int(i[4]) - 100, i[1], i[2], i[3]))
            self.card.append([i[1], i[2], i[3], i[4]])
        openDeck.destroy()

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
