import factory
import random
from random import randint
from random import choice


from .models import *


class TestResultfactory(factory.django.DjangoModelFactory):
   test_result = choice(["Normal", "Abnormal", "Inconclusive"])

   class Meta:
       model = TestResult

class Medicationfactory(factory.django.DjangoModelFactory):
   medication =  choice(["Aspirin", "Ibuprofen", "Paracetamol"])
   
   class Meta:
       model = Medication

class MedicalConditionfactory(factory.django.DjangoModelFactory):
   medical_condition = choice(["Obesity", "Arthritis", "Diabetes"])
   
   class Meta:
       model = MedicalCondition

class Insurancefactory(factory.django.DjangoModelFactory):
   insurance = choice(["Medicare", "Aetna", "Cigna"])
   
   class Meta:
       model = Insurance

class Hospitalfactory(factory.django.DjangoModelFactory):
   hospital = 'Walton LLC'
   
   class Meta:
       model = Hospital

class Genderfactory(factory.django.DjangoModelFactory):
   gender = choice(["Male", "Female"])
   
   class Meta:
       model = Gender

class Doctorfactory(factory.django.DjangoModelFactory):
   doctor = 'Paul Baker'
   
   class Meta:
       model = Doctor

class BloodTypefactory(factory.django.DjangoModelFactory):
   blood_type = choice(["O-", "O+", "B-", "B+","AB+", "A+"])
   
   class Meta:
       model = BloodType

class AdmissionTypefactory(factory.django.DjangoModelFactory):
   admission_type = choice(["Elective", "Emergency", "Urgent"])

   class Meta:
       model = AdmissionType


class PatientFactory(factory.django.DjangoModelFactory):
   name = 'Tiffany Ramirez'
   age = 81
   gender = factory.SubFactory(Genderfactory)
   blood_type = factory.SubFactory(BloodTypefactory)

   class Meta:
       model = Patient


class PatientFactory(factory.django.DjangoModelFactory):
   name = 'Tiffany Ramirez'
   age = 81
   gender = factory.SubFactory(Genderfactory)
   blood_type = factory.SubFactory(BloodTypefactory)

   class Meta:
       model = Patient

class AdmissionFactory(factory.django.DjangoModelFactory):
    date_of_admission = "2022-11-17" 
    room_number = randint(1, 10000)
    billing_amount = 325423.214
    discharge_date = "2022-12-01"
    patient = factory.SubFactory(PatientFactory)
    hospital = factory.SubFactory(Hospitalfactory)
    doctor = factory.SubFactory(Doctorfactory)
    medication = factory.SubFactory(Medicationfactory)
    insurance = factory.SubFactory(Insurancefactory)
    admission_type = factory.SubFactory(AdmissionTypefactory)
    test_result = factory.SubFactory(TestResultfactory)
    medical_condition = factory.SubFactory(MedicalConditionfactory)

    class Meta:
        model = Admission
