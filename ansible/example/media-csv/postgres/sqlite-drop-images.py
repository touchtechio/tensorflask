import sqlite3
conn = sqlite3.connect('Laika-Kubo.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

cursor.execute('''DROP TABLE IF EXISTS IMAGES;''')

conn.commit()

conn.close()
