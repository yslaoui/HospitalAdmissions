from rest_framework import serializers
from .models import *

class AdmissionSerializer(serializers.ModelSerializer):
   class Meta:
       model = Admission
       fields = ['date_of_admission', 'room_number',
                 'billing_amount', 'discharge_date',
                 'patient', 'hospital',
                 'doctor', 'medication',
                 'insurance', 'admission_type',
                 'test_result', 'medical_condition']



# class Admission(models.Model):
#     date_of_admission = models.DateField(null=False, blank=False)
#     room_number = models.IntegerField(null=True, blank=True)
#     billing_amount = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
#     discharge_date = models.DateField(null=True, blank=True)
#     patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
#     hospital = models.ForeignKey(Hospital, null=True,  on_delete=models.DO_NOTHING)
#     doctor = models.ForeignKey(Doctor, null=True, on_delete=models.DO_NOTHING)
#     medication = models.ForeignKey(Medication, null=True, on_delete=models.DO_NOTHING)
#     insurance = models.ForeignKey(Insurance, null=True, on_delete=models.DO_NOTHING)
#     admission_type = models.ForeignKey(AdmissionType, null=True, on_delete=models.DO_NOTHING)
#     test_result = models.ForeignKey(TestResult, null=True, on_delete=models.DO_NOTHING)
#     medical_condition = models.ForeignKey(MedicalCondition, null=True, on_delete=models.DO_NOTHING)

