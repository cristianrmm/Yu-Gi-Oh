import requests
import json
import io
import os
import time
import mysql.connector
import datetime

def main():
    myCards = MyFile()['data']
    myDB = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        passwd= '',
        database='yu_gi_oh'
    )
    InsertItemDB(myDB, myCards, 100)
    myDB.close()

#naive approach
def InsertItemDB(mydb, set, qty):
    CreateTableItems(myDB, MonsterInfo(myCards))
    n = CountRowDB(myDB)
    info = MonsterInfo(myCards)
    max = n
    print("start")
    s = time.time()
    while n < max + qty:
        InsertCardToDB(myDB, info, myCards, n)
        n += 1
    myDB.close()
    e = time.time()
    print('done time:' + str(datetime.timedelta(seconds=e - s)))

def CountRowDB(mydb):
    my_cursor = mydb.cursor()
    count = """
            SELECT COUNT(*) FROM cards
            """

    my_cursor.execute(count)
    n = my_cursor.fetchall()
    mydb.commit()
    my_cursor.close()
    return n[0][0]

def ReDefine(elements):
    for i in elements:
        if i == 'desc':
            elements[elements.index(i)] = 'description'
    return elements

def Convert(list):
    return tuple(i for i in list)

def InsertCardToDB(mydb, info, cardInfo, index):
    my_cursor = mydb.cursor()
    info = ReDefine(info)
    values = [''] * len(info)
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

    cardInfo[index] = LinkMarkerDirection(cardInfo[index])
    for i in cardInfo[index]:
        for j in info:
            if j == 'description':
                values[info.index(j)] = cardInfo[index]['desc']
            if j in cardInfo[index]:
                values[info.index(j)] = cardInfo[index][j]
    values.append(False)
    my_cursor.execute(sql_command, Convert(values))

    mydb.commit()
    my_cursor.close()

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

def CreateTable(mydb):
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE DATABASE yu_gi_oh")
    mydb.commit()
    my_cursor.close()

def ZeroToEmpty(num):
    if num == '0':
        return ""
    else:
        return num

def CreateTableItems(mydb, elements):
    elements = ReDefine(elements)

    my_cursor = mydb.cursor()
    my_cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Cards(
                        ''' + str(elements[0]) + ''' INT(9),
                        ''' + str(elements[1]) + ''' VARCHAR(127),
                        ''' + str(elements[2]) + ''' VARCHAR(63),
                        ''' + str(elements[3]) + ''' VARCHAR(31),
                        ''' + str(elements[4]) + ''' VARCHAR(2047),
                        ''' + str(elements[5]) + ''' VARCHAR(31),
                        ''' + str(elements[6]) + ''' VARCHAR(62),
                        ''' + str(elements[7]) + ''' VARCHAR(4),
                        ''' + str(elements[8]) + ''' VARCHAR(4),
                        ''' + str(elements[9]) + ''' VARCHAR(2),
                        ''' + str(elements[10]) + ''' VARCHAR(15),
                        ''' + str(elements[11]) + ''' VARCHAR(511),
                        ''' + str(elements[12]) + ''' VARCHAR(1023),
                        ''' + ZeroToEmpty(str(elements[13])) + ''' VARCHAR(2),
                        ''' + ZeroToEmpty(str(elements[14])) + ''' VARCHAR(1),
                        ''' + str(elements[15]) + ''' VARCHAR(63),
                        active_card BOOLEAN NOT NULL DEFAULT 0,
                        card_index INT AUTO_INCREMENT PRIMARY KEY,
                        CONSTRAINT my_cards UNIQUE ('''+ str(elements[0]) +''',  '''+ str (elements[1]) +''')
                        )
                      ''')
    mydb.commit()
    my_cursor.close()

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

def Save(data):
    my_json_path = os.path.join(
        #os.path.dirname(__file__), "c:\\Users\\crist\\OneDrive\\Desktop\\Large data\\Yu-Gi_Oh.json"
        os.path.dirname(__file__), "Yu-Gi_Oh.json"
    )

    with open(my_json_path, "w") as f:
        json.dump(data, f)

#Get all cards Info other wise this program won't work
def Api():
    try:
        api = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
        print(api.status_code)
        myapi = json.loads(api.content)
        Save(myapi)
        print(myapi['data'][0]['id'])

    except Exception as e:
        return("Error..")

def MyFile():
    my_json_path = os.path.join(
        #os.path.dirname(__file__), "c:\\Users\\crist\\OneDrive\\Desktop\\Large data\\Yu-Gi_Oh.json"
        os.path.dirname(__file__), "Yu-Gi_Oh.json"
    )

    with open(my_json_path) as f:
        d = json.load(f)
        return d

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

#Get every main unique key from the Json file
def CardDesc(cardsInfo):
    allsets= []
    n = 1
    for i in UniqueSet(cardsInfo):
        for j in i:
            if j not in allsets:
                allsets.append(j)
    return allsets

if __name__ == "__main__":
    main()