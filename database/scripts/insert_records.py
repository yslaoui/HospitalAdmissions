from db_connector import get_db_connection
from collections import defaultdict
import csv
# Define path to data
data_file = '../csv/healthcare_dataset.csv'

medications = set()

# Populate data structures
with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') # csv_reader is an object that allows you to iterate over rows of your data. Each row is a list of values
    header = csv_reader.__next__() # skip the header
    for row in csv_reader:
        medications.add(row[13])

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
        # ... rest of your code ...
    # Loop through the rows in the CSV file
        for elem in medications:
            # Create the INSERT INTO statement
            query = "INSERT INTO medications (medication) VALUES (%s)"
            # Execute the SQL command
            cursor.execute(query, (elem,))
        #Commit the changes in the database
        db_connection.commit()
        
    finally:
        # Ensure that the connection is closed
        db_connection.close()
        print("MySQL connection is closed")