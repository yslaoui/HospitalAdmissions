from django.db import models



# Lookup tables
class TestResult(models.Model):
    test_result = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self) :
        return self.test_result

class Medication(models.Model):
    medication = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self) :
        return self.medication

class MedicalCondition(models.Model):
    medical_condition = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self) :
        return self.medical_condition

class Insurance(models.Model):
    insurance = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self) :
        return self.insurance
   

class Hospital(models.Model):
    hospital = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self) :
        return self.hospital


class Gender(models.Model):
    gender = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self) :
        return self.gender


class Doctor(models.Model):
    doctor = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self) :
        return self.doctor


class BloodType(models.Model):
    blood_type = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self) :
        return self.blood_type

 

class AdmissionType(models.Model):
    admission_type = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self) :
        return self.admission_type


# Patient table

class Patient(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    blood_type = models.ForeignKey(BloodType, null=True, on_delete=models.SET_NULL)
    medication = models.ManyToManyField(Medication, through="PatientMedicationLink", null=True, blank=True)

    def __str__(self) :
        return self.name

class Admission(models.Model):
    date_of_admission = models.DateField(null=False, blank=False)
    room_number = models.IntegerField(null=True, blank=True)
    billing_amount = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    discharge_date = models.DateField(null=True, blank=True)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    hospital = models.ForeignKey(Hospital, null=True,  on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.DO_NOTHING)
    medication = models.ForeignKey(Medication, null=True, on_delete=models.DO_NOTHING)
    insurance = models.ForeignKey(Insurance, null=True, on_delete=models.DO_NOTHING)
    admission_type = models.ForeignKey(AdmissionType, null=True, on_delete=models.DO_NOTHING)
    test_result = models.ForeignKey(TestResult, null=True, on_delete=models.DO_NOTHING)
    medical_condition = models.ForeignKey(MedicalCondition, null=True, on_delete=models.DO_NOTHING)

    def __str__(self) :
        admission_id = 'admissions' + str(self.id)
        return admission_id

class PatientMedicationLink(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    medication = models.ForeignKey(Medication, on_delete=models.DO_NOTHING)
    
# class GeneAttributeLink(models.Model):
#     gene = models.ForeignKey(Gene, on_delete=models.DO_NOTHING) 
#     attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)    
