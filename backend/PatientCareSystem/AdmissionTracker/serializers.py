from rest_framework import serializers
from .models import *

#TODO add the serializes for the lookup tables

class TestResultSerializer(serializers.ModelSerializer):
   class Meta:
       model = TestResult
       fields = ['id', 'test_result']

class MedicationSerializer(serializers.ModelSerializer):
   class Meta:
       model = Medication
       fields = ['id','medication']

class MedicalConditionSerializer(serializers.ModelSerializer):
   class Meta:
       model = MedicalCondition
       fields = ['id','medical_condition']

class InsuranceSerializer(serializers.ModelSerializer):
   class Meta:
       model = Insurance
       fields = ['id','insurance']

class HospitalSerializer(serializers.ModelSerializer):
   class Meta:
       model = Hospital
       fields = ['id','hospital']

class GenderSerializer(serializers.ModelSerializer):
   class Meta:
       model = Gender
       fields = ['id','gender']

class DoctorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Doctor
       fields = ['id','doctor']

class BloodTypeSerializer(serializers.ModelSerializer):
   class Meta:
       model = BloodType
       fields = ['id','blood_type']

class AdmissionTypeSerializer(serializers.ModelSerializer):
   
   class Meta:
       model = AdmissionType
       fields = ['id','admission_type']

class PatientSerializer(serializers.ModelSerializer):
    gender = GenderSerializer(read_only=True)
    blood_type = BloodTypeSerializer(read_only=True)
    medication = MedicationSerializer(many=True, read_only=True)
    class Meta:
        model = Patient
        fields = ['id','name', 'age', 'gender', 
                    'blood_type', 'medication']



class AdmissionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    hospital = HospitalSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    medication = MedicationSerializer(read_only=True)
    insurance = InsuranceSerializer(read_only=True)
    admission_type = AdmissionTypeSerializer(read_only=True)
    test_result = TestResultSerializer(read_only=True)
    medical_condition = MedicalConditionSerializer(read_only=True)
    class Meta:
        model = Admission
        fields = ['id', 'date_of_admission', 'room_number',
                     'billing_amount', 'discharge_date',
                    'patient', 'hospital',
                    'doctor', 'medication',
                    'insurance', 'admission_type',
                    'test_result', 'medical_condition']

