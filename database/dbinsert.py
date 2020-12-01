import sqlite3

def insert(id, character, gif_url):
    sqliteConnection = sqlite3.connect('bone.db')
    cursor = sqliteConnection.cursor()
    print("Connected to BoneDB")
    sqlite_insert_query = """ INSERT INTO characters (id, character, gif_url) VALUES (?, ?, ?) """

    data_tuple = (id, character, gif_url)                                 
    cursor.execute(sqlite_insert_query, data_tuple)                                                 # execute the query
    sqliteConnection.commit()
    print("Entry inserted corectly")
    cursor.close()

    if (sqliteConnection):
        sqliteConnection.close()
        print("The sqlite connection is closed")

insert(1, "random chinese character", "randomgif.gov")