import math
import tkinter.messagebox

import requests
import json
import os
import time
import mysql.connector
import urllib
import glob
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from Filter import  Filter

def main():
    myCards = MyFile()['data']
    myDB = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='yu_gi_oh'
    )
    allSets = AllCardSets(myCards)
    DB_Access(myDB, myCards, allSets)
    SaveImages(myCards)
    Main_Window(myDB)
    myDB.close()

def Main_Window(myDB):
    root = Tk()
    root.attributes('-fullscreen', True)
    cardId = DB_GetCardInfo(myDB)
    #Display all card Info for the user from Treeview
    index = 0
    sampleSize = 100
    cardSet = [0]
    images = []
    name_Label = []
    des_Label = []
    type_Label = []
    my_Label = []
    label = [my_Label, name_Label, des_Label, type_Label]

    f = Filter(myDB)

    images = [(ImageTk.PhotoImage(Image.open("images\\" + str(cardId[0][0]) + ".jpg").resize((271, 395))))]

    mainFrame = LabelFrame(root, text="main")
    selection = LabelFrame(root, text="slection")
    selection.grid(row=0, column=0, sticky=N)
    mainFrame.grid(row=0, column=1)
    my_Label.append(Label(mainFrame, image = images[0]))
    my_Label[0].grid(row=0, column= 0, rowspan=3, sticky=W)

    name_Label.append(Label(mainFrame, text="Name: \n" + str(cardId[sampleSize * cardSet[0]][1]), justify="left"))
    name_Label[0].grid(row=0, column=1, sticky=W)

    des_Label.append(Label(mainFrame, text="Description: \n"  + str(cardId[sampleSize * cardSet[0]][2]), justify="left", wraplength=1000))
    des_Label[0].grid(row=1, column=1, sticky=W)

    type_Label.append(Label(mainFrame, text="Card Type: \n" + str(cardId[sampleSize * cardSet[0]][3]), justify="left"))
    type_Label[0].grid(row=2, column=1, sticky=W)


    frameType = ttk.Combobox(selection)
    archeType = ttk.Combobox(selection)
    raceType = ttk.Combobox(selection)
    levelType = ttk.Combobox(selection)
    frameType['values'] = f.FrameType()
    archeType['values'] = f.ArcheType()
    raceType['values'] = f.RaceType()
    levelType['values'] = f.Level()
    frameType.current(0)
    archeType.current(0)
    raceType.current(0)
    levelType.current(0)

    table = Frame(mainFrame)
    #seting up a look up table
    my_tree = ttk.Treeview(table)
    my_tree['columns'] = ('id', 'name')
    my_tree.column('#0', stretch=NO)
    my_tree.column('id', anchor=W)
    my_tree.column('name', anchor=CENTER)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('id', text='id', anchor=W)
    my_tree.heading('name', text='name', anchor=CENTER)

    count = 0
    location = sampleSize * cardSet[0] + count
    while location < sampleSize * (cardSet[0] + 1) and location < len(cardId):
        my_tree.insert(parent='', index='end', iid=location, text=str(location), values=(str(cardId[location][0]), str(cardId[location][1])))
        count += 1
        location = sampleSize * cardSet[0] + count

    previousSet = Button(table, text='<', command=lambda: NextSet('-', label, mainFrame, cardSet, my_tree, cardId, sampleSize, images, initialSet, previousSet, nextSet, imageSet), state=DISABLED)
    imageSet = Label(table, text=str(cardSet[0])+ ':' + str(math.floor(len(cardId) / sampleSize)))
    nextSet = Button(table, text='>', command=lambda: NextSet('+', label, mainFrame, cardSet, my_tree, cardId, sampleSize, images, initialSet, previousSet, nextSet, imageSet))

    frameType.grid(row=0, column=0, sticky=N)
    archeType.grid(row=1, column=0, sticky=N)
    raceType.grid(row=2, column=0, sticky=N)
    levelType.grid(row=3, column=0, sticky=N)
    table.grid(row=5, column=0, columnspan=2, sticky=W)
    my_tree.grid(row=0, column=0, columnspan=3)
    previousSet.grid(row=1, column=0, sticky=W)
    imageSet.grid(row=1, column=1)

    nextSet.grid(row=1, column=2, sticky=E)

    initialSet = [sampleSize * cardSet[0]]
    frameType.bind('<<ComboboxSelected>>', lambda Event: Select(frameType, f, 'frame', mainFrame, label, my_tree, sampleSize, cardId, cardSet, images, imageSet, previousSet, nextSet, initialSet))
    archeType.bind('<<ComboboxSelected>>', lambda Event: Select(archeType, f, 'arche', mainFrame, label, my_tree, sampleSize, cardId, cardSet, images, imageSet, previousSet, nextSet, initialSet))
    raceType.bind('<<ComboboxSelected>>', lambda Event: Select(raceType, f, 'race', mainFrame, label, my_tree, sampleSize, cardId, cardSet, images, imageSet, previousSet, nextSet, initialSet))
    levelType.bind('<<ComboboxSelected>>', lambda Event: Select(levelType, f, 'level', mainFrame, label, my_tree, sampleSize, cardId, cardSet, images, imageSet, previousSet, nextSet, initialSet))
    my_tree.bind('<Button-1>', lambda Event: SelectItem(Event, label, mainFrame, images, my_tree, cardId, initialSet))
    root.bind('<Escape>', lambda Event: Quit(root))
    root.mainloop()

def Select(frameType, f, cardtype, root, label, my_tree, sampleSize, cardId, cardSet, images, imageSet, ps, ns, initialSet):

    cardSet[0] = 0

    for i in my_tree.get_children():
        my_tree.delete(i)

    if cardtype == 'frame':
        f.GetFrame(frameType.get())
    elif cardtype == 'arche':
        f.GetArchType(frameType.get())
    elif cardtype == 'race':
        f.GetRace(frameType.get())
    elif cardtype == 'level':
        f.GetLevel(frameType.get())

    if (len(f.GetAllCards()) > 0):
        cardId.clear()
        for i in f.GetAllCards():
            cardId.append(i)
    else:
        tkinter.messagebox.showwarning(title='No Cards', message='No match found')

    imageSet['text'] = str(cardSet[0]) + ':' + str(math.floor(len(cardId) / sampleSize))

    ps['state'] = DISABLED
    if (math.floor(len(cardId)  / sampleSize) == 0):
        ns['state'] = DISABLED
    else:
        ns['state'] = ACTIVE

    count = 0
    location = sampleSize * cardSet[0] + count
    while location < sampleSize * (cardSet[0] + 1) and location <= len(cardId) - 1:
        my_tree.insert(parent='', index='end', iid=location, text=str(location), values=(str(cardId[location][0]), str(cardId[location][1])))
        count += 1
        location = sampleSize * cardSet[0] + count
    initialSet = sampleSize * cardSet[0]

    images[0] = ImageTk.PhotoImage(Image.open('Images\\' + str(cardId[0][0]) + '.jpg').resize((271, 395)))

    label[0][0].destroy()
    label[1][0].destroy()
    label[2][0].destroy()
    label[3][0].destroy()

    label[0][0] = Label(root, image = images[0])
    label[0][0].grid(row=0, column= 0, rowspan=3, sticky=W)

    index = sampleSize * cardSet[0]
    label[1][0] = Label(root, text="Name: \n" + str(cardId[index][1]), justify="left")
    label[1][0].grid(row=0, column=1, columnspan=3, sticky=W)

    label[2][0] = Label(root, text="Description: \n" + str(cardId[index][2]), justify="left", wraplength=1000)
    label[2][0].grid(row=1, column=1, columnspan=3, sticky=W)

    label[3][0] = Label(root, text="Card type: \n" + str(cardId[index][3]), justify="left")
    label[3][0].grid(row=2, column=1, columnspan=3, sticky=W)


def NextSet(nexstep, label, root, cardSet, my_tree, cardId, sampleSize, images, initialSet, ps, ns, imageSet):
    images.clear()
    label[0][0].destroy()
    label[1][0].destroy()
    label[2][0].destroy()
    label[3][0].destroy()

    if nexstep == '+':
        cardSet[0] = cardSet[0] + 1
        imageSet['text'] = str(cardSet[0]) + ':' + str(math.floor(len(cardId) / sampleSize))

        if (cardSet[0]) == math.floor(len(cardId) / sampleSize):
            ns['state'] = DISABLED

        ps['state'] = ACTIVE
    elif nexstep == '-':
        cardSet[0] = cardSet[0] - 1
        imageSet['text'] = str(cardSet[0]) + ':' + str(math.floor(len(cardId) / sampleSize))
        ns['state'] = ACTIVE
        if cardSet[0] == 0:
            ps['state'] = DISABLED

        if (cardSet[0] < math.floor(len(cardId) / sampleSize)):
            ns['state'] = ACTIVE

    for i in my_tree.get_children():
        my_tree.delete(i)

    count = 0
    location = sampleSize * cardSet[0] + count
    images.append(ImageTk.PhotoImage(Image.open('Images\\' + str(cardId[location][0]) + '.jpg').resize((271, 395))))
    while location < sampleSize * (cardSet[0] + 1) and location < len(cardId):
        my_tree.insert(parent='', index='end', iid=location, text=str(location), values=(str(cardId[location][0]), str(cardId[location][1])))
        count += 1
        location = sampleSize * cardSet[0] + count
    initialSet[0] = sampleSize * cardSet[0]

    label[0][0] = Label(root, image = images[0])
    label[0][0].grid(row=0, column= 0, rowspan=3, sticky=W)

    index = sampleSize * cardSet[0]
    label[1][0] = Label(root, text="Name: \n" + str(cardId[index][1]), justify="left")
    label[1][0].grid(row=0, column=1, columnspan=3, sticky=W)

    label[2][0] = Label(root, text="Description: \n" + str(cardId[index][2]), justify="left", wraplength=1000)
    label[2][0].grid(row=1, column=1, columnspan=3, sticky=W)

    label[3][0] = Label(root, text="Card type: \n" + str(cardId[index][3]), justify="left")
    label[3][0].grid(row=2, column=1, columnspan=3, sticky=W)

def SelectItem(Event, label, root, images, myTree, cardId, initialSet):
    item = myTree.identify('item', Event.x, Event.y)
    if(len(myTree.item(item)['values']) != 0):
        label[0][0].destroy()
        label[1][0].destroy()
        label[2][0].destroy()
        label[3][0].destroy()

        images[0] = ImageTk.PhotoImage(Image.open("images\\" + str(myTree.item(item)['values'][0]) + ".jpg").resize((271, 395)))
        index = int(myTree.item(item)['text'])

        # Display all card Info for the user from Treeview
        label[0][0] = Label(root, image=images[0])
        label[0][0].grid(row=0, column=0, rowspan=3, sticky=W)

        label[1][0] = Label(root, text="Name: \n" + str(cardId[index][1]), justify="left")
        label[1][0].grid(row=0, column=1, columnspan=3, sticky=W)

        label[2][0] = Label(root, text="Description: \n" + str(cardId[index][2]), justify="left", wraplength=1000)
        label[2][0].grid(row=1, column=1, columnspan=3, sticky=W)

        label[3][0] = Label(root, text="Card type: \n" + str(cardId[index][3]), justify="left")
        label[3][0].grid(row=2, column=1, columnspan=3, sticky=W)


def DB_GetCardInfo(myDB):
    myCursor = myDB.cursor()
    myCursor.execute("SELECT id, name, description, frameType, card_index FROM cards")
    return myCursor.fetchall()

def Quit(root):
    root.destroy()

# access my Main Database
def DB_Access(myDB, myCards, allSets):
    # create the tables if they don't exist
    DB_CreateTabelSets(myDB, myCards)
    DB_CreateTableItems(myDB, MonsterInfo(myCards))

    # insert every element into the tables
    DB_InsertCard(myDB, MonsterInfo(myCards), myCards, len(myCards))
    DB_InsertCardSet(myDB, allSets, len(allSets))

def DB_InsertCardSet(myDB, allSets, qty):
    setOrder = ['id', 'set_name', 'card_set', 'region', 'num', 'set_rarity', 'set_rarity_code', 'set_price']
    my_cursor = myDB.cursor()
    index = DB_CountRow(myDB, 'card_set')
    sql_command = """INSERT INTO card_set(""" + setOrder[0] + """,
                                         """ + setOrder[1] + """,
                                         """ + setOrder[2] + """,
                                         """ + setOrder[3] + """,
                                         """ + setOrder[4] + """,
                                         """ + setOrder[5] + """,
                                         """ + setOrder[6] + """,
                                         """ + setOrder[7] + """
                                         ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)  
                                         """

    num = 0
    while num < qty - index:
        mylist = GetTuple(allSets[index + num], setOrder)
        my_cursor.execute(sql_command, mylist)
        num += 1

    myDB.commit()
    my_cursor.close()

#creatre card_set table
def DB_CreateTabelSets(mydb, myCards):
    my_crusor = mydb.cursor()
    my_crusor.execute("""
                    CREATE TABLE IF NOT EXISTS card_set(
                    """ + list(myCards[1]['card_sets'][0].keys())[4] + """ VARCHAR(15),
                    """ + list(myCards[1]['card_sets'][0].keys())[0] + """ VARCHAR(127),
                    """ + list(myCards[1]['card_sets'][0].keys())[5] + """ VARCHAR(7),
                    """ + list(myCards[1]['card_sets'][0].keys())[6] + """ VARCHAR(7),
                    """ + list(myCards[1]['card_sets'][0].keys())[7] + """ VARCHAR(7),
                    """ + list(myCards[1]['card_sets'][0].keys())[1] + """ VARCHAR(63),
                    """ + list(myCards[1]['card_sets'][0].keys())[2] + """ VARCHAR(15),
                    """ + list(myCards[1]['card_sets'][0].keys())[3] + """ VARCHAR(15),
                    card_index INT AUTO_INCREMENT PRIMARY KEY
                    )
                    """)
    mydb.commit()
    my_crusor.close()

#count how many rows are in a given table
def DB_CountRow(mydb, table):
    my_cursor = mydb.cursor()
    count = """
            SELECT COUNT(*) FROM """ + table + """
            """

    my_cursor.execute(count)
    n = my_cursor.fetchall()
    mydb.commit()
    my_cursor.close()
    return n[0][0]

def DB_InsertCard(mydb, info, cardInfo, qty):
    index = DB_CountRow(mydb, 'cards')
    my_cursor = mydb.cursor()
    info = ReDefine(info)
    sql_command = """INSERT INTO cards(""" + info[0] + """,
                                        """ + info[1] + """,
                                        """ + info[2] + """,
                                        """ + info[3] + """,
                                        """ + info[4] + """,
                                        """ + info[5] + """,
                                        """ + info[6] + """,
                                        """ + info[7] + """,
                                        """ + info[8] + """,
                                        """ + info[9] + """,
                                        """ + info[10] + """,
                                        """ + info[11] + """,
                                        """ + info[12] + """,
                                        """ + info[13] + """,
                                        """ + info[14] + """,
                                        """ + info[15] + """,
                                        active_card 
                                        )  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    num = 0
    while num < qty - index:
        values = RenameCollumn(index + num, info, cardInfo)
        my_cursor.execute(sql_command, Convert(values))
        num += 1

    mydb.commit()
    my_cursor.close()

def DB_CreateTable(mydb):
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE DATABASE yu_gi_oh")
    mydb.commit()
    my_cursor.close()

def DB_CreateTableItems(mydb, elements):
    elements = ReDefine(elements)

    my_cursor = mydb.cursor()
    my_cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Cards(
                        """ + str(elements[0]) + """ INT(9),
                        """ + str(elements[1]) + """ VARCHAR(127),
                        """ + str(elements[2]) + """ VARCHAR(63),
                        """ + str(elements[3]) + """ VARCHAR(31),
                        """ + str(elements[4]) + """ VARCHAR(2047),
                        """ + str(elements[5]) + """ VARCHAR(31),
                        """ + str(elements[6]) + """ VARCHAR(62),
                        """ + str(elements[7]) + """ VARCHAR(4),
                        """ + str(elements[8]) + """ VARCHAR(4),
                        """ + str(elements[9]) + """ VARCHAR(2),
                        """ + str(elements[10]) + """ VARCHAR(15),
                        """ + str(elements[11]) + """ VARCHAR(511),
                        """ + str(elements[12]) + """ VARCHAR(1023),
                        """ + ZeroToEmpty(str(elements[13])) + """ VARCHAR(2),
                        """ + ZeroToEmpty(str(elements[14])) + """ VARCHAR(1),
                        """ + str(elements[15]) + """ VARCHAR(63),
                        active_card BOOLEAN NOT NULL DEFAULT 0,
                        card_index INT AUTO_INCREMENT PRIMARY KEY,
                        CONSTRAINT my_cards UNIQUE ("""+ str(elements[0]) +""",  """+ str (elements[1]) +""")
                        )
                      """)
    mydb.commit()
    my_cursor.close()

#collect all sets in yugioh
def AllCardSets(myCards):
    mySets = []
    index= 0
    while index < len(myCards):
        if 'card_sets' in myCards[index]:
            for i in myCards[index]['card_sets']:
                i['id'] = myCards[index]['id']
                set = ExpendSetCode(i['set_code'])
                del i['set_code']
                i['card_set'] = set[0]
                i['region'] = set[1]
                i['num'] = set[2]
                mySets.append(i)
        index = index + 1
    return mySets

#Get all cards Info other wise this program won't work
def Api():
    try:
        api = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
        print(api.status_code)
        myapi = json.loads(api.content)
        #Save(myapi)
        print(myapi['data'][0]['id'])

    except Exception as e:
        return("Error..")

#Get every main unique key from the Json file
def CardDesc(cardsInfo):
    allsets= []
    n = 1
    for i in UniqueSet(cardsInfo):
        for j in i:
            if j not in allsets:
                allsets.append(j)
    return allsets

#Gets only the spesifc traits of the monster usful for the dual
def ClearSet(mycards):
    item = []
    num = 0
    for i in UniqueSet(mycards):
        item.append([])
        for j in MonsterInfo(mycards, False):
            if j in i:
                item[num].append(j)

        num = num + 1
    return item

def Convert(list):
    return tuple(i for i in list)

#ensures that two set of list or dictionaries are the same
def Dect_Equal(list1, list2):
    same = True
    for i in list1:
        if i in list2:
            same = True
        else:
            return False
    for i in list2:
        if i in list1:
            same = True
        else:
            return False
    return same

#split the set_code to three indevidual componets of set, region, and number of the card in the set
def ExpendSetCode(setCode):
    set = setCode.split('-')
    region = ""
    num = ""
    if len(set) > 1:
        for i in set[1]:
            if i.isdigit():
                num = num + i
            else:
                region = region + i
        set.pop(1)
    set.append(region)
    set.append(num)
    return set

#get the values froma the dictionary
def GetTuple(myDict, myList):
    toTuple = []

    for i in myList:
        toTuple.append(myDict[i])
    return Convert(toTuple)

def LinkMarkerDirection(myCard):
    direction = ''
    n = 0
    if 'linkmarkers' in myCard:
        for i in myCard['linkmarkers']:
            if n == 0:
                direction = i
                n = 1
            else:
                direction = direction + "," + i
    myCard['linkmarkers'] = direction
    return myCard

#Default value to false to obtain all cards info for dual if set to true archetype will not be on the list
def MonsterInfo(set, archetype = False):
    cardSet = []
    if archetype:
        cardSet = ['ygoprodeck_url', 'card_sets', 'card_images', 'card_prices', 'banlist_info', 'archetype']
    else:
        cardSet = ['ygoprodeck_url', 'card_sets', 'card_images', 'card_prices', 'banlist_info']
    monseterInfo = []
    for i in CardDesc(set):
        if i not in cardSet:
            monseterInfo.append(i)
    return monseterInfo

def MyFile():
    my_json_path = os.path.join(
        #os.path.dirname(__file__), "c:\\Users\\crist\\OneDrive\\Desktop\\Large data\\Yu-Gi_Oh.json"
        os.path.dirname(__file__), "Yu-Gi_Oh.json"
    )

    with open(my_json_path) as f:
        d = json.load(f)
        return d

def Save(data):
    my_json_path = os.path.join(
        # os.path.dirname(__file__), "c:\\Users\\crist\\OneDrive\\Desktop\\Large data\\Yu-Gi_Oh.json"
        os.path.dirname(__file__), "Yu-Gi_Oh.json"
    )

    with open(my_json_path, "w") as f:
        json.dump(data, f)

#upload every card to file only once including the new cards that are not in the current list
#Order does matter
def SaveImages(myCards):
    length = 0
    fileSize = len(glob.glob('images\\*.jpg'))
    while length < len(myCards) - fileSize:
        urllib.request.urlretrieve(myCards[length + fileSize]['card_images'][0]['image_url'], 'images\\' + str(myCards[length + fileSize]['card_images'][0]['id']) + '.jpg')
        length += 1
        time.sleep(50/1000)

def ReDefine(elements):
    for i in elements:
        if i == 'desc':
            elements[elements.index(i)] = 'description'
    return elements

def RenameCollumn(index, info, cardInfo):
    values = [''] * len(info)
    cardInfo[index] = LinkMarkerDirection(cardInfo[index])
    for i in cardInfo[index]:
        for j in info:
            if j == 'description':
                values[info.index(j)] = cardInfo[index]['desc']
            if j in cardInfo[index]:
                values[info.index(j)] = cardInfo[index][j]
    values.append(False)
    return values

#removes every duplicate from the list
def UniqueSet(cardsInfo):
    count = len(cardsInfo)
    n = 0
    j = 0
    myset = [cardsInfo[0]]
    match = 0
    same = True
    while n < count:
        while j < len(myset):
            if(Dect_Equal(myset[j],cardsInfo[n])):
                match = match + 1
            j = j + 1
        if (match == 0):
             myset.append(cardsInfo[n])
        match = 0
        j = 0
        n = n + 1

    return myset

def ZeroToEmpty(num):
    if num == '0':
        return ""
    else:
        return num

if __name__ == "__main__":
    main()
