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
    gender = GenderSerializer(read_only=False)
    blood_type = BloodTypeSerializer(read_only=False)
    medication = MedicationSerializer(many=True, read_only=True)
    class Meta:
        model = Patient
        fields = ['id','name', 'age', 'gender', 
                    'blood_type', 'medication']


    def create(self, validated_data):
        '''
        Needed for all foreign keys.
        read_only=False allows POST and PUT request to change data on server
        By default create method does not support nested data.
        Nested data are better than flat data for front end because it needs the id as key for elements
        therefore we must override create()
        '''
        
        gender_data = self.initial_data["gender"]
        blood_type_data = self.initial_data["blood_type"]
        medication_data = self.initial_data["medication"]

        # One to many relationship
        patient = Patient(**{**validated_data, 
                        'gender': Gender.objects.get(pk=gender_data['id']),
                        'blood_type': BloodType.objects.get(pk=blood_type_data['id']) 
                        })
        patient.save() # save before you tacke many to many relationships

        # # many to many relationships
        medication_ids = [medication["id"] for medication in medication_data]
        for medication_id in medication_ids:
            medication_obj = Medication.objects.get(pk = medication_id)
            patient.medication.add(medication_obj)

        return patient



    # def create(self, validated_data):
    #     '''
    #     Needed for all foreign keys.
    #     read_only=False allows POST and PUT request to change data on server
    #     By default create method does not support nested data.
    #     Nested data are better than flat data for front end because it needs the id as key for elements
    #     therefore we must override create()
    #     '''
    #     gender_data = self.initial_data["gender"]
    #     blood_type = self.initial_data["blood_type"]
    #     patient = Patient(**{**validated_data, 
    #                     'gender': Gender.objects.get(pk=gender_data['id']),
    #                     'blood_type': BloodType.objects.get(pk=gender_data['id']) 
    #                     })
    #     patient.save()
    #     return patient

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

