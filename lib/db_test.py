import mysql.connector
from mysql.connector import errorcode

class mysql_test:
    """regelt de meetings enzo"""

    def __init__(self, conf):
        self.cnx = None
        self.cnx = mysql.connector.connect(**conf)

        try:
            cursor = self.cnx.cursor()
            cursor.execute()
            print()

        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("u done goofed")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("F in the chat for the db")
            raise e

    def create_meeting(self):
        pass

    def get_meeting(self):
        pass

    def update_meeting(self):
        pass

    def delete_meeting(self):
        pass