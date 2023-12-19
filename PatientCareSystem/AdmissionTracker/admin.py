from django.contrib import admin
from .models import *
# Register your models here.

class AdmissionAdmin(admin.ModelAdmin):
   list_display = ('date_of_admission', 'room_number', 'billing_amount',
                   'discharge_date', 'patient', 'hospital',
                   'doctor','medication','insurance',
                    'admission_type','test_result','medical_condition' )

class PatientAdmin(admin.ModelAdmin):
   list_display = ('name', 'age', 'gender',
                   'blood_type')

class TestResultAdmin(admin.ModelAdmin):
   list_display = ('test_result',)

class MedicationAdmin(admin.ModelAdmin):
   list_display = ('medication',)

class MedicalConditionAdmin(admin.ModelAdmin):
   list_display = ('medical_condition',)

class InsuranceAdmin(admin.ModelAdmin):
   list_display = ('insurance',)

class HospitalAdmin(admin.ModelAdmin):
   list_display = ('hospital',)

class GenderAdmin(admin.ModelAdmin):
   list_display = ('gender',)

class DoctorAdmin(admin.ModelAdmin):
   list_display = ('doctor',)

class BloodTypeAdmin(admin.ModelAdmin):
   list_display = ('blood_type',)

class AdmissionTypeAdmin(admin.ModelAdmin):
   list_display = ('admission_type',)


admin.site.register(Admission, AdmissionAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(TestResult, TestResultAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(MedicalCondition, MedicalConditionAdmin)
admin.site.register(Insurance, InsuranceAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(BloodType, BloodTypeAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(AdmissionType,AdmissionTypeAdmin)
