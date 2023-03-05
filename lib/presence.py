import os
import sqlite3
from sqlite3 import OperationalError
from lib.db import Database

class PresenceManagement(Database):
    def __init__(self, db_file):
        super().__init__(db_file)

    def get_presence(self, meetingid):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute(f"SELECT aanwezigheid.aanwezigheid, aanwezigheid.student, aanwezigheid.meeting, "
                           f"student.voornaam, student.achternaam "
                           f"FROM aanwezigheid INNER JOIN student "
                           f"ON aanwezigheid.student=student.id AND aanwezigheid.meeting IN ({meetingid})")


            presence_db_info = cursor.fetchall()
            conn.close()

            presence_info = []
            for info in presence_db_info:
                presence_info.append({
                    "presence": info[0],
                    "student": info[1],
                    "meeting": info[2],
                    "first name": info[3],
                    "last name": info[4]
                })
        except OperationalError as e:
            print("yeet")
            raise e
        return presence_info

    def update_presence(self, json_data):
        try:
            json_presence = json_data["presence"]
            json_student = json_data["student"]
            json_meeting = json_data["meeting"]
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute(f"UPDATE aanwezigheid SET aanwezigheid = ? "
                           f"WHERE student = ? AND meeting = ?", (json_presence, json_student, json_meeting))
            conn.commit()
            conn.close()

        except OperationalError as e:
            print("yeet")
            raise e
    def update_presence(self, json_data):
        try:
            json_presence = json_data["presence"]
            json_student = json_data["student"]
            json_meeting = json_data["meeting"]
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute(f"UPDATE aanwezigheid SET aanwezigheid = ? "
                           f"WHERE student = ? AND meeting = ?", (json_presence, json_student, json_meeting))
            conn.commit()
            conn.close()

        except OperationalError as e:
            print("yeet")
            raise e
