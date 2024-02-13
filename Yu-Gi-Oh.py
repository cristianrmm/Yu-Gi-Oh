import requests
import json
import os
import time
import mysql.connector
import datetime
import urllib
import glob


def main():
    myCards = MyFile()['data']

    allSets = AllCardSets(myCards)
    DB_Access(myCards, allSets)
    SaveImages(myCards)


# access my Main Database
def DB_Access(myCards, allSets):
    myDB = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='yu_gi_oh'
    )
    #create the tables if they don't exist
    DB_CreateTabelSets(myDB, myCards)
    DB_CreateTableItems(myDB, MonsterInfo(myCards))

    #insert every element into the tables
    DB_InsertCard(myDB, MonsterInfo(myCards), myCards, len(myCards))
    DB_InsertCardSet(myDB, allSets, len(allSets))
    myDB.close()

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
