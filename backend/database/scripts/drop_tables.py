from db_connector import get_db_connection
from collections import defaultdict
import csv

# Get the database connection
db_connection = get_db_connection()

if db_connection is not None and db_connection.is_connected():
    try:
        # Perform database operations
        db_info = db_connection.get_server_info()
        print(f"Successfully connected to MySQL Server version {db_info}")
        # Create a cursor object using the cursor() method
        cursor = db_connection.cursor()
        # Delete all records from the database to start afresh 
        cursor.execute("DROP TABLE IF EXISTS admissions")
        cursor.execute("DROP TABLE IF EXISTS patients")
        cursor.execute("DROP TABLE IF EXISTS admission_types")
        cursor.execute("DROP TABLE IF EXISTS blood_types")
        cursor.execute("DROP TABLE IF EXISTS doctors")
        cursor.execute("DROP TABLE IF EXISTS genders")
        cursor.execute("DROP TABLE IF EXISTS hospitals")
        cursor.execute("DROP TABLE IF EXISTS insurance")
        cursor.execute("DROP TABLE IF EXISTS medical_conditions")
        cursor.execute("DROP TABLE IF EXISTS medications")
        cursor.execute("DROP TABLE IF EXISTS test_results")

        #Commit the changes in the database
        db_connection.commit()
        
    finally:
        # Ensure that the connection is closed
        db_connection.close()
        print("MySQL connection is closed")
