import mysql.connector
from mysql.connector import errorcode
from lib.db_test import mysql_test

class ClassManagement(mysql_test):
    """regelt de klassen enzo"""

    def __init__(self, conf):
        super().__init__(conf)

    def get_class(self):
        try:
            conn = mysql.connector.connect()
            conn.reconnect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM klas")

            classes = cursor.fetchall()
            print(classes)

            conn.commit() 

            conn.close()

        except mysql.connector.Error as e:
            print("yeet")
            raise e

        return classes


    def get_enrollment(self):
        try:
            conn = mysql.connector.connect()
            conn.reconnect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM enrollment")
            enrollment = cursor.fetchall()
            conn.commit() 

            conn.close()

        except mysql.connector.Error as e:
            print("yeet")
            raise e
        return enrollment
    
    def add_class(self, klas):
        try:
            conn = mysql.connector.connect()
            #conn.reconnect()
            cursor = conn.cursor()

            cursor.execute(f"INSERT INTO klas (id) VALUES (?)", [klas])
            conn.commit() 

            conn.close()

        except mysql.connector.Error as e:
            print("yeet")
            raise e

    def edit_class(self, klas):
        try:
            conn = mysql.connector.connect()
            conn.reconnect()
            cursor = conn.cursor()

            cursor.execute(f"UPDATE klas SET id = ? WHERE id = ?", [klas])
            conn.commit() 

            conn.close()

        except mysql.connector.Error as e:
            print("yeet")
            raise e


    def delete_class(self, klas):
        try:
            conn = mysql.connector.connect()
            conn.reconnect()
            cursor = conn.cursor()

            cursor.execute(f"DELETE FROM klas WHERE id = ?", [klas])

            conn.commit() 

            conn.close()

        except mysql.connector.Error as e:
            print("yeet")
            raise e
