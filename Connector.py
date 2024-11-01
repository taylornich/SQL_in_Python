import mysql.connector
from mysql.connector import Error


def connect_db():
    db_name = "gym_management_assignment"
    user = "root"
    password = ""
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
# not returning the if statement but not giving errors either? come back to this. 

        if conn.is_connected:
            print("Connected to MySQL Databse successfully.")

    except Error as e:
        print(f"Error: {e}")
        return None
