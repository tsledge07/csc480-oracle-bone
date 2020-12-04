import sqlite3

def insert(id, character, gif_url):
    sqliteConnection = sqlite3.connect('bone.db')
    cursor = sqliteConnection.cursor()
    print("Connected to BoneDB")
    sqlite_insert_query = """ INSERT INTO characters (id, character, gif_url) VALUES (?, ?, ?) """
    data_tuple = (id, character, gif_url) 
    cursor.execute(sqlite_insert_query, data_tuple) # execute the query
    sqliteConnection.commit()
    print("Entry inserted corectly")
    cursor.close()

    if (sqliteConnection):
        sqliteConnection.close()
        print("The sqlite connection is closed")

insert(1, "邬", "https://www.hanzi5.com/assets/bishun/animation/90ac-bishun.gif")
insert(2, "郗", "https://www.hanzi5.com/assets/bishun/animation/90d7-bishun.gif")
insert(3, "郇", "https://www.hanzi5.com/assets/bishun/animation/90c7-bishun.gif")
insert(4, "魏", "https://www.hanzi5.com/assets/bishun/animation/9b4f-bishun.gif")
insert(5, "魄", "https://www.hanzi5.com/assets/bishun/animation/9b44-bishun.gif")
insert(6, "骸", "https://www.hanzi5.com/assets/bishun/animation/9ab8-bishun.gif")
insert(7, "髁", "https://www.hanzi5.com/assets/bishun/animation/9ac1-bishun.gif")
insert(8, "骰", "https://www.hanzi5.com/assets/bishun/animation/9ab0-bishun.gif")
insert(9, "髂", "https://www.hanzi5.com/assets/bishun/animation/9ac2-bishun.gif")
insert(10, "髌", "https://www.hanzi5.com/assets/bishun/animation/9acc-bishun.gif")
