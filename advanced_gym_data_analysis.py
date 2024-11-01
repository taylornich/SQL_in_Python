# question 2 task 1

from Connector import connect_db
from mysql.connector import Error

def get_members_in_age_range(start_age, end_age):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s and %s"
            cursor.execute(query, (start_age, end_age))
            result = cursor.fetchall()


            if result:
                print("Members in the specified age range: ")

                for row in result:
                    id, name, age = row

                    print(f"Member ID: {id}, Name: {name}, Age: {age}")
            
            else:
                print("No members in that age range were found in the database.")

        except Error as e:
            print(f"Error: {e}")

        finally: 
            cursor.close()
            conn.close()
