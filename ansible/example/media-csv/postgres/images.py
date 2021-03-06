import psycopg2
import csv
import pandas as pd


class Images(object):
    """postgres database class that holds testers jobs"""
    __DB_LOCATION = "beefy.ra.intel.com"
    __DB_PORT = 5432
    __LAIKA_IMAGE_CSV = "../data/data/Laika-Kubo.csv"

    def __init__(self, db_location=__DB_LOCATION, db_port=__DB_PORT):
        """Initialize db class variables"""
        self.__db_connection = psycopg2.connect(host=db_location, port=db_port, dbname="images", user="eddy", password="bowl")
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
                             (ID INT PRIMARY KEY    NOT NULL,
                             FILENAME       TEXT    NOT NULL,
                             PATH           TEXT    NOT NULL,
                             EXT            TEXT    NOT NULL,
                             TAGS           TEXT    NOT NULL,
                             SCENE_NO       INTEGER NULL,
                             SHOT_NO        INTEGER NULL,
                             FRAME_NO       INTEGER NULL);''')

    def drop_table(self):
        """drop a database table if it does exist already"""
        self.cur.execute('''DROP TABLE IF EXISTS IMAGES;''')

    def fill_table(self, path=__LAIKA_IMAGE_CSV):
        #path = '../data/data/laika-images.csv'

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            index = 0
            for row in reader:

                # index could be line number but our csv doesn't quite lineup
                # index = reader.line_num
                # we'll increment index at the end or figure out how to make this db autoincrement

                # insert a row
                self.cur.execute(
                    "INSERT INTO IMAGES (ID,FILENAME,PATH,EXT,TAGS) VALUES (" + str(index) + ", '" + row[
                        'ImageFilename'] + "', '" + row['ImageDirectory'] + "', '" + row['ImageExtension'] + "', 'original')");

                # print once every hundred rows so we know something is happening
                if (index % 100 == 0):
                    print(index, ':', row['ImageFilename'], row['ImageExtension'])

                # commit each insertion
                self.commit()
                index += 1

            print(index, ' rows inserted!')

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def get_by_sql(self, sql):
        """execute a row of data to current cursor"""
        image = pd.read_sql_query(sql, self.__db_connection)
        return image

    def get_by_name(self, filename):
        """execute a row of data to current cursor"""
        image = self.get_by_sql("SELECT * FROM IMAGES where FILENAME = '" + filename + "'")
        return image

    def get_by_index(self, index):
        """execute a row of data to current cursor"""
        image = self.get_by_sql("SELECT * FROM IMAGES where ID = " + str(index))
        return image

    def get_all_by_tag(self, tag):
        """execute a row of data to current cursor"""
        sql = "SELECT * FROM IMAGES where TAGS LIKE '%" + tag + "%'"
        print(sql)
        image = self.get_by_sql(sql)
        return image

    def get_all(self):
        images_table = self.get_by_sql("SELECT * FROM IMAGES")
        return images_table

    # #not quite working
    # def update(self, panda):
    #     panda.to_sql("IMAGES", self.__db_connection, if_exists="replace")

    def commit(self):
        """commit changes to database"""
        self.__db_connection.commit()

