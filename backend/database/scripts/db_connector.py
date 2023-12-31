# db_connector.py
import os
import mysql.connector
from mysql.connector import Error

def get_db_connection():
    # Retrieve password from environment variable
    db_password = os.getenv('MY_DATABASE_PASSWORD') # command line export MY_DATABASE_PASSWORD='yourActualPassword'

    try:
        # Establish a database connection
        db_connection = mysql.connector.connect(
            host="localhost",         # Your host, usually localhost
            user="quantumleap",       # Your MySQL username
            password=db_password,     # Your MySQL password
            database="admissions"     # Name of the database
        )
        return db_connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
