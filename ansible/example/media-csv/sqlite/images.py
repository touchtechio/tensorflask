import sqlite3
import csv
import pandas as pd


class Images(object):
    """sqlite3 database class that holds testers jobs"""
    __DB_LOCATION = "laika_images.sqlite"
    __LAIKA_IMAGE_CSV = "../data/data/laika-images.csv"

    def __init__(self, db_location=None):
        """Initialize db class variables"""
        if db_location is not None:
            self.__db_connection = sqlite3.connect(db_location)
        else:
            self.__db_connection = sqlite3.connect(self.__DB_LOCATION)
        self.cur = self.__db_connection.cursor()

    def __del__(self):
        self.__db_connection.close()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.__db_connection.rollback()
        else:
            self.__db_connection.commit()
        self.__db_connection.close()

    def close(self):
        """close sqlite3 connection"""
        self.__db_connection.close()

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS IMAGES
                             (ID INT PRIMARY KEY     NOT NULL,
                             FILENAME       TEXT    NOT NULL UNIQUE,
                             PATH           TEXT    NOT NULL,
                             TAGS           TEXT    NOT NULL);''')

    def drop_table(self):
        """drop a database table if it does exist already"""
        self.cur.execute('''DROP TABLE IF EXISTS IMAGES;''')

    def fill_table(self, path=__LAIKA_IMAGE_CSV):
        #path = '../data/data/laika-images.csv'

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.cur.execute(
                    "INSERT INTO IMAGES (ID,FILENAME,PATH,TAGS) VALUES (" + str(reader.line_num) + ", '" + row[
                        'ImageFilename'] + "', '" + row['ImageDirectory'] + "', 'original')");
                if (reader.line_num % 100 == 0):
                    print(reader.line_num, ':', row['ImageFilename'])

                self.commit()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def get_all(self):
        images_table = pd.read_sql_query("SELECT * FROM IMAGES", self.__db_connection)
        return images_table

    def commit(self):
        """commit changes to database"""
        self.__db_connection.commit()

