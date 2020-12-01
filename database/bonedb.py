import sqlite3

conn = sqlite3.connect('bone.db')
print("Opened database successfully");

conn.execute('CREATE TABLE characters (id INTEGER PRIMARY KEY, character TEXT NOT NULL, gif_url TEXT)')
print("Table created successfully");
conn.close()