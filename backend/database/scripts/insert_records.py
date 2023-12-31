from db_connector import get_db_connection
from collections import defaultdict
import csv
import pandas as pd
# Define path to data
data_file = '../csv/healthcare_dataset_with_pks.csv'

# Initialize data structures
    #Lookup tables
medications = set()
genders = set()
blood_types = set()
insurances = set()
admission_types = set()
test_results = set()
test_results = set()
medical_conditions = set()
hospitals = set()
doctors = set()

    #Mother table
admissions = defaultdict(list)
    #Transitive table
patients = defaultdict(dict)

# Populate data structures
with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') # csv_reader is an object that allows you to iterate over rows of your data. Each row is a list of values
    header = csv_reader.__next__() # skip the header
    for row in csv_reader:
        #lookup tables
        genders.add(row[5])
        blood_types.add(row[6])
        medical_conditions.add(row[7])
        doctors.add(row[9])
        hospitals.add(row[10])
        insurances.add(row[11])
        admission_types.add(row[14])
        medications.add(row[16])
        test_results.add(row[17])
        #transitive table
        patients[row[0]]['name'] = row[3]
        patients[row[0]]['age'] = row[4]
        patients[row[0]]['gender'] = row[5]
        patients[row[0]]['blood_type'] = row[6]
        #mother table [patientID, medical condition, date of admission, doctor, hospital, insurance, billing amount, room number, admission type, discharge date, medication, test results]
        admissions[row[1]] = [row[0]] + [row[7]] + [row[8]] + [row[9]] + [row[10]] + [row[11]] + [row[12]] + [row[13]] + [row[14]] + [row[15]] + [row[16]]+ [row[17]]    


print(admissions)
print('the 10th element is' + admissions['10000'][1])
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
        cursor.execute("DELETE FROM admission_types")
        cursor.execute("DELETE FROM test_results")
        cursor.execute("DELETE FROM medical_conditions")
        cursor.execute("DELETE FROM doctors")
        cursor.execute("DELETE FROM hospitals")
        cursor.execute("DELETE FROM patients")
        cursor.execute("DELETE FROM admissions")

        # reset the id
        cursor.execute("ALTER TABLE medications AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE genders AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE blood_types AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE insurances AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE admission_types AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE test_results AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE medical_conditions AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE doctors AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE hospitals AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE patients AUTO_INCREMENT = 1")
        cursor.execute("ALTER TABLE admissions AUTO_INCREMENT = 1")

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
        for elem in admission_types:
            query = "INSERT INTO admission_types (admission_type) VALUES (%s)"
            cursor.execute(query, (elem,))  
        for elem in test_results:
            query = "INSERT INTO test_results (test_result) VALUES (%s)"
            cursor.execute(query, (elem,))  
        for elem in medical_conditions:
            query = "INSERT INTO medical_conditions (medical_condition) VALUES (%s)"
            cursor.execute(query, (elem,))
        for elem in doctors:
            query = "INSERT INTO doctors (doctor) VALUES (%s)"
            cursor.execute(query, (elem,)) 
        for elem in hospitals:
            query = "INSERT INTO hospitals (hospital) VALUES (%s)"
            cursor.execute(query, (elem,))     

        # Insert data in patients table
        for key in patients.keys():
            query = '''INSERT INTO patients (name, age, gender_id, blood_type_id) 
                        VALUES (%s, %s, 
                        (SELECT id FROM genders WHERE gender=%s), 
                        (SELECT id FROM blood_types WHERE blood_type=%s)
                        )'''
            cursor.execute(query, (patients[key]['name'],
                                   patients[key]['age'],
                                   patients[key]['gender'], 
                                   patients[key]['blood_type']
                                   ))   
            
        # Insert data in admissions table
        for key in admissions.keys():
            query = '''INSERT INTO admissions 
                       (date_of_admission, billing_amount, discharge_date, room_number, patient_id, hospital_id, doctor_id, medication_id, insurance_id, admission_type_id, test_result_id, medical_condition_id)
                       VALUES (%s, %s, %s, %s, %s,
                       (SELECT id FROM hospitals WHERE hospital=%s),
                       (SELECT id FROM doctors WHERE doctor=%s),
                       (SELECT id FROM medications WHERE medication=%s),
                       (SELECT id FROM insurances WHERE insurance=%s),
                       (SELECT id FROM admission_types WHERE admission_type=%s),
                       (SELECT id FROM test_results WHERE test_result=%s),
                       (SELECT id FROM medical_conditions WHERE medical_condition=%s) 
                       )'''
            cursor.execute(query, (admissions[key][2], admissions[key][6], admissions[key][9], admissions[key][7], admissions[key][0], admissions[key][4], admissions[key][3], admissions[key][10], admissions[key][5], admissions[key][8], admissions[key][11], admissions[key][1] ))
        #Commit the changes in the database
        db_connection.commit()
        
    finally:
        db_connection.close()
        print("MySQL connection is closed")

# 10000': ['10000', 'Arthritis', '2023-03-22', 
#           'Tasha Avila', 'Torres, Young and Stewart', 
#           'Aetna', '37223.965864725855', '290', 
#           'Emergency', '2023-04-15', 'Penicillin', 
#           'Abnormal']})




