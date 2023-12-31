# Configuring the script to work with the bioweb django project
import os
import sys

import django
from django.db import connection
import csv
from collections import defaultdict

sys.path.append('/home/quantumleap/Documents/git/uol/course/4_Level6S1/django/midterm/work/PatientCareSystem')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PatientCareSystem.settings')

django.setup()

# Import models to be able to add data to models
from AdmissionTracker.models import *

# Import logging library
import logging
logger = logging.getLogger(__name__)

# Define path to data
data_file = './healthcare_dataset_small.csv'

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

# print(patients)
# print('the 2nd element is' + admissions['10000'][1])

# Deleting data from database -- allows you to run the script as many time as you want without duplicating insertions
PatientMedicationLink.objects.all().delete()
Admission.objects.all().delete()
Patient.objects.all().delete()
AdmissionType.objects.all().delete()
BloodType.objects.all().delete()
Doctor.objects.all().delete()
Gender.objects.all().delete()
Hospital.objects.all().delete()
Insurance.objects.all().delete()
MedicalCondition.objects.all().delete()
Medication.objects.all().delete()
TestResult.objects.all().delete()

# Reseting the primary key sequences

with connection.cursor() as cursor:
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_medication'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_patientmedicationlink'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_patient'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_admission'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_admissiontype'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_doctor'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_hospital'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_insurance'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_medicalcondition'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_testresult'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_bloodtype'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='AdmissionTracker_gender'")



# foreign key dictionaries
patient_rows = {}
doctor_rows = {}
hospital_rows = {}
blood_type_rows = {}
admission_type_rows = {}
gender_rows = {}
insurance_rows = {}
medical_condition_rows = {}
medication_rows = {}
test_result_rows = {}


# INSERTING DATA FROM SETS

for entry in test_results: 
    try:
        row = TestResult.objects.create(test_result=entry) # create an instance of Ec class. Equivalemntly insert the string entry in the ec_name column
        row.save() # save the data in the database. Attention migration is concerned with database schema, not data records
        test_result_rows[entry] = row # saving the instance because it is a foreign key in gene data
    except Exception as e:
        logger.error(f"error creating EC object {e}")
# print(test_result_rows)

for entry in medications: 
    try:
        row = Medication.objects.create(medication=entry) 
        row.save() 
        medication_rows[entry] = row 
    except Exception as e:
        logger.error(f"error creating EC object {e}")
# print(medication_rows)

for entry in medical_conditions: 
    try:
        row = MedicalCondition.objects.create(medical_condition=entry) 
        row.save() 
        medical_condition_rows[entry] = row 
    except Exception as e:
        logger.error(f"error creating EC object {e}")
# print(medical_condition_rows)

for entry in insurances: 
    try:
        row = Insurance.objects.create(insurance=entry) 
        row.save() #
        insurance_rows[entry] = row 
    except Exception as e:
        logger.error(f"error creating EC object {e}")
# print(insurance_rows)

for entry in genders: 
    try:
        row = Gender.objects.create(gender=entry) 
        row.save() 
        gender_rows[entry] = row 
    except Exception as e:
        logger.error(f"error creating EC object {e}")
# print(gender_rows)

for entry in admission_types: 
    try:
        row = AdmissionType.objects.create(admission_type=entry) 
        row.save() 
        admission_type_rows[entry] = row 
    except Exception as e:
        logger.error(f"error creating EC object {e}")
# print(admission_type_rows)

for entry in blood_types: 
    try:
        row = BloodType.objects.create(blood_type=entry) 
        row.save() 
        blood_type_rows[entry] = row 
    except Exception as e:
        logger.error(f"error creating EC object {e}")
# print(blood_type_rows)


for entry in hospitals: 
    try:
        row = Hospital.objects.create(hospital=entry) 
        row.save() 
        hospital_rows[entry] = row 
    except Exception as e:
        logger.error(f"error creating EC object {e}")
# print(hospital_rows)

for entry in doctors: 
    try:
        row = Doctor.objects.create(doctor=entry) 
        row.save() 
        doctor_rows[entry] = row 
    except Exception as e:
        logger.error(f"error creating EC object {e}")
# print(doctor_rows)



## INSERTING DATA FROM DICTIONARY OF DICTIONARIES (transitive table)
# print(gender_rows)
for key in patients.keys():
    try:
        row = Patient.objects.create(
            name = patients[key]['name'],
            age = patients[key]['age'],
            gender = gender_rows[patients[key]['gender']],
            blood_type = blood_type_rows[patients[key]['blood_type']]
        )
        row.save()
        patient_rows[key] = row
        
    except Exception as e:
        logger.error(f"error creating Patient object {e}")
print(patient_rows)



## INSERTING DATA FROM DICTIONARY OF LISTS (mother table)

for key in admissions.keys():
    # print(patient_rows[admissions[key][0]])
    try:
        row = Admission.objects.create(
            date_of_admission = admissions[key][2],
            billing_amount = admissions[key][6],
            discharge_date = admissions[key][9],
            room_number = admissions[key][7],
            patient = patient_rows[admissions[key][0]],
            hospital = hospital_rows[admissions[key][4]],
            doctor = doctor_rows[admissions[key][3]],
            medication = medication_rows[admissions[key][10]],
            insurance = insurance_rows[admissions[key][5]],
            admission_type = admission_type_rows[admissions[key][8]],
            test_result = test_result_rows[admissions[key][11]],
            medical_condition = medical_condition_rows[admissions[key][1]]
        )
        row.save()      
    except Exception as e:
        logger.error(f"error creating Patient object {e}")



# Creating the patient medication link table 

for key in admissions.keys():
    try:
        # Fetch the patient instance
        patient_instance = patient_rows[admissions[key][0]]
        
        #Fetch the medication instance (if many instances, I would use a for loop here)
        medication_instance = medication_rows[admissions[key][10]]

        # Add the medication to the patient's medications. I use .add() for the many to many relationships
        patient_instance.medication.add(medication_instance)

        patient_instance.save()

    except Exception as e:
        logger.error(f"error processing admission {e}")

# print(patients)
print(admissions)

