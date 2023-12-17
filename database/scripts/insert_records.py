from db_connector import get_db_connection
from collections import defaultdict
import csv
# Define path to data
data_file = '../csv/healthcare_dataset.csv'

medications = set()
genders = set()
blood_types = set()
insurances = set()

# Populate data structures
with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') # csv_reader is an object that allows you to iterate over rows of your data. Each row is a list of values
    header = csv_reader.__next__() # skip the header
    for row in csv_reader:
        medications.add(row[13])
        genders.add(row[2])
        blood_types.add(row[3])
        insurances.add(row[8])



print(medications)

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
        cursor.execute("DELETE FROM medications")
        cursor.execute("DELETE FROM genders")
        cursor.execute("DELETE FROM blood_types")
        cursor.execute("DELETE FROM insurances")


        # Insert data in lookup tables
        for elem in medications:
            query = "INSERT INTO medications (medication) VALUES (%s)"
            cursor.execute(query, (elem,))        
        for elem in genders:
            query = "INSERT INTO genders (gender) VALUES (%s)"
            cursor.execute(query, (elem,))      
        for elem in blood_types:
            query = "INSERT INTO blood_types (blood_type) VALUES (%s)"
            cursor.execute(query, (elem,))   
        for elem in insurances:
            query = "INSERT INTO insurances (insurance) VALUES (%s)"
            cursor.execute(query, (elem,))        
       
        #Commit the changes in the database
        db_connection.commit()
        
    finally:
        # Ensure that the connection is closed
        db_connection.close()
        print("MySQL connection is closed")