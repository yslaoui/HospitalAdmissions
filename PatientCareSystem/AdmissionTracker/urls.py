from django.urls import include, path
from . import api

urlpatterns = [
    path('api/admissions', api.AdmissionList.as_view(), name='admission_list_api'), 
    path('api/admissions/<int:pk>', api.AdmissionDetail.as_view(), name='admission_detail_api'),

    path('api/testresults', api.TestResultList.as_view(), name='admission_list_api'), 
    path('api/testresults/<int:pk>', api.TestResultDetail.as_view(), name='admission_detail_api'),

    path('api/medications', api.MedicationList.as_view(), name='admission_list_api'), 
    path('api/medications/<int:pk>', api.MedicationDetail.as_view(), name='admission_detail_api'),

    path('api/medicalconditions', api.MedicalConditionList.as_view(), name='admission_list_api'), 
    path('api/medicalconditions/<int:pk>', api.MedicalConditionDetail.as_view(), name='admission_detail_api'),

    path('api/insurances', api.InsuranceList.as_view(), name='admission_list_api'), 
    path('api/insurances/<int:pk>', api.InsuranceDetail.as_view(), name='admission_detail_api'),

    path('api/hospitals', api.HospitalList.as_view(), name='admission_list_api'), 
    path('api/hospitals/<int:pk>', api.HospitalDetail.as_view(), name='admission_detail_api'),

    path('api/genders', api.GenderList.as_view(), name='admission_list_api'), 
    path('api/genders/<int:pk>', api.GenderDetail.as_view(), name='admission_detail_api'),

    path('api/doctors', api.DoctorList.as_view(), name='admission_list_api'), 
    path('api/doctors/<int:pk>', api.DoctorDetail.as_view(), name='admission_detail_api'),

    path('api/bloodtypes', api.BloodTypeList.as_view(), name='admission_list_api'), 
    path('api/bloodtypes/<int:pk>', api.BloodTypeDetail.as_view(), name='admission_detail_api'),

    path('api/admissiontypes', api.AdmissionTypeList.as_view(), name='admission_list_api'), 
    path('api/admissiontypes/<int:pk>', api.AdmissionTypeDetail.as_view(), name='admission_detail_api'),


    path('api/patients', api.PatientList.as_view(), name='admission_list_api'), 
    path('api/patients/<int:pk>', api.PatientDetail.as_view(), name='admission_detail_api'),

    path('api/admissions', api.AdmissionTypeList.as_view(), name='admission_list_api'), 
    path('api/admissions/<int:pk>', api.AdmissionTypeDetail.as_view(), name='admission_detail_api'),

]

