import sqlite3
conn = sqlite3.connect('MissingLink_Groundtruth_PNG.sqlite')
cursor = conn.cursor()
print("Opened database successfully")



cursor.execute('''CREATE TABLE IF NOT EXISTS IMAGES
         (ID INT PRIMARY KEY     NOT NULL,
         FILENAME       TEXT    NOT NULL,
         PATH           TEXT    NOT NULL,
         TAGS           TEXT    NOT NULL);''')

conn.commit()





conn.close()
