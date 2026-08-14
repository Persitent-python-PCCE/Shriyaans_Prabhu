import os
import mysql.connector as con
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()
class DataBase:
    def __init__(self):
        self.host=os.getenv("DB_HOST") 
        self.port=os.getenv("DB_PORT",3306)
        self.user=os.getenv("DB_USER")
        self.password=os.getenv("DB_PASSWORD")
        self.database=os.getenv("DB_NAME")
    def connect(self):
        try:
            connection=con.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                # print("DataBase Connected !")
                return connection
        except Error as E:
            print(f"Connection Failed: {E}")
        return None
# db=DataBase()
# connection_setup=db.connect()
# if connection_setup:
#     connection_setup.close()
#     print("DataBase closed.")
