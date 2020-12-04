import sqlite3

def pullCharacter(id):
    sqliteConnection = sqlite3.connect('bone.db')
    cursor = sqliteConnection.cursor()
    print("Connected to BoneDB")
    cursor.execute("SELECT * FROM characters WHERE id=?", (id,))
    row = cursor.fetchone()
    val = row[1]
    return val
    cursor.close()

def pullURL(id):
    sqliteConnection = sqlite3.connect('bone.db')
    cursor = sqliteConnection.cursor()
    print("Connected to BoneDB")
    cursor.execute("SELECT * FROM characters WHERE id=?", (id,))
    row = cursor.fetchone()
    val = row[2]
    return val
    cursor.close()
print("Character 2 info: ")
print(pullCharacter(2))
print(pullURL(2))
