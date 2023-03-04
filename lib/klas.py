import os
import sqlite3
from sqlite3 import OperationalError


class ClassManagement:
    """regelt de klassen enzo"""

    def __init__(self, db_file):
        self.db_file = db_file
        if not os.path.exists(self.db_file):
            raise FileNotFoundError(f"F in the chat for {db_file}")

    def get_class(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM klas")
            classes = cursor.fetchall()
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print("yeet")
            raise e

        return classes

    def get_enrollment(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM enrollment")
            enrollment = cursor.fetchall()
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print("yeet")
            raise e
        return enrollment