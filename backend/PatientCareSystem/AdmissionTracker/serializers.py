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
    medication = MedicationSerializer(many=True, read_only=True) # medication added to patients through the admission form only
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

        # One to many relationship
        patient = Patient(**{**validated_data, 
                        'gender': Gender.objects.get(pk=gender_data['id']),
                        'blood_type': BloodType.objects.get(pk=blood_type_data['id']) 
                        })
        patient.save() # save before you tacke many to many relationships
        return patient
        # # # many to many relationships
        # medication_ids = [medication["id"] for medication in medication_data]
        # for medication_id in medication_ids:
        #     medication_obj = Medication.objects.get(pk = medication_id)
        #     patient.medication.add(medication_obj)
    
    def update(self, instance, validated_data):
        gender_data = validated_data.pop('gender', None)
        blood_type_data = validated_data.pop('blood_type', None)

        # Update the Patient instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update Gender
        if gender_data:
            gender_id = gender_data.get('id')
            if gender_id:
                instance.gender = Gender.objects.get(pk=gender_id)
                instance.save()

        # Update Blood Type
        if blood_type_data:
            blood_type_id = blood_type_data.get('id')
            if blood_type_id:
                instance.blood_type = BloodType.objects.get(pk=blood_type_id)
                instance.save()
        return instance
    
    # # Handle many-to-many relationship for medication
    #     if medication_data:
    #         medication_data = validated_data.pop('medication', [])
    #         medication_ids = [medication['id'] for medication in medication_data]
    #         medications = Medication.objects.filter(id__in=medication_ids)
    #         instance.medication.set(medications)
    #         return instance

    


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

    def create(self, validated_data):
        '''
        Needed for all foreign keys.
        read_only=False allows POST and PUT request to change data on server
        By default create method does not support nested data.
        Nested data are better than flat data for front end because it needs the id as key for elements
        therefore we must override create()
        '''
        
        patient_data = self.initial_data["patient"]
        hospital_data = self.initial_data["hospital"]
        doctor_data = self.initial_data["doctor"]
        medication_data = self.initial_data["medication"]
        insurance_data = self.initial_data["insurance"]
        admissiontype_data = self.initial_data["admission_type"]
        testresult_data = self.initial_data["test_result"]
        medicalcondition_data = self.initial_data["medical_condition"]

        # One to many relationship
        admission = Admission(**{**validated_data, 
                        'patient': Patient.objects.get(pk=patient_data['id']),
                        'hospital': Hospital.objects.get(pk=hospital_data['id']),
                        'doctor': Doctor.objects.get(pk=doctor_data['id']),
                        'medication': Medication.objects.get(pk=medication_data['id']),
                        'insurance': Insurance.objects.get(pk=insurance_data['id']),
                        'admission_type': AdmissionType.objects.get(pk=admissiontype_data['id']),
                        'test_result': TestResult.objects.get(pk=testresult_data['id']),
                        'medical_condition': MedicalCondition.objects.get(pk=medicalcondition_data['id']),
                        })
        admission.save() # save before you tacke many to many relationships

        # many to many relationships
        medication = Medication.objects.get(pk=medication_data['id'])
        patient = Patient.objects.get(pk=patient_data['id'])
        patient.medication.add(medication)
            
        return admission
