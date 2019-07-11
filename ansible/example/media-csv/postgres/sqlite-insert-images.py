import sqlite3
import csv

conn = sqlite3.connect('MissingLink_Groundtruth_PNG.sqlite')
cursor = conn.cursor()
print("Opened database successfully")


IMAGE_CSV = '../data/data/MissingLink_Groundtruth_PNG.csv'
path = IMAGE_CSV

# with open(path) as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(reader.line_num, ':', row['ImageFilename'])


with open(path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("INSERT INTO IMAGES (ID,FILENAME,PATH,TAGS) VALUES ("+str(reader.line_num)+", '"+row['ImageFilename']+"', '"+row['ImageDirectory']+"', 'original')");
        if (reader.line_num % 100 == 0):
            print(reader.line_num, ':', row['ImageFilename'])

        conn.commit()






conn.close()
