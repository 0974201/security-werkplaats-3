import mysql.connector
from mysql.connector import errorcode

class mysql_test:
    """testen of de database werkt want shit blifjt doodgaan"""

    def __init__(self, conf):
        try:
            #self.cnx = None
            self.cnx = mysql.connector.connect(**conf)
            cursor = self.cnx.cursor()

        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("u done goofed")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("F in the chat for the db")
            raise e