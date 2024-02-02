from django.urls import path, re_path
from . import api
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views
from django.views.decorators.csrf import csrf_exempt
# from django.urls import path, re_path
# from django.views.generic import TemplateView
# from . import views  # Assuming your views are in the same directory
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^app/.*', TemplateView.as_view(template_name='index.html')),
    # path('login', view.user_login)    
    # path('/login', views.user_ )
    path('login', views.user_login, name='user_login'),
    path('api/admissions', api.AdmissionList.as_view(), name='admissions_list_api'), 
    path('api/admissions/<int:pk>', api.AdmissionDetail.as_view(), name='admissions_detail_api'),

    path('api/testresults', api.TestResultList.as_view(), name='testresults_list_api'), 
    path('api/testresults/<int:pk>', api.TestResultDetail.as_view(), name='testresults_detail_api'),

    path('api/medications', api.MedicationList.as_view(), name='medications_list_api'), 
    path('api/medications/<int:pk>', api.MedicationDetail.as_view(), name='medications_detail_api'),

    path('api/medicalconditions', api.MedicalConditionList.as_view(), name='medicalconditions_list_api'), 
    path('api/medicalconditions/<int:pk>', api.MedicalConditionDetail.as_view(), name='medicalconditions_detail_api'),

    path('api/insurances', api.InsuranceList.as_view(), name='insurances_list_api'), 
    path('api/insurances/<int:pk>', api.InsuranceDetail.as_view(), name='insurances_detail_api'),

    path('api/hospitals', api.HospitalList.as_view(), name='hospitals_list_api'), 
    path('api/hospitals/<int:pk>', api.HospitalDetail.as_view(), name='hospitals_detail_api'),

    path('api/genders', api.GenderList.as_view(), name='genders_list_api'), 
    path('api/genders/<int:pk>', api.GenderDetail.as_view(), name='genders_detail_api'),

    path('api/doctors', api.DoctorList.as_view(), name='doctors_list_api'), 
    path('api/doctors/<int:pk>', api.DoctorDetail.as_view(), name='doctors_detail_api'),

    path('api/bloodtypes', api.BloodTypeList.as_view(), name='bloodtypes_list_api'), 
    path('api/bloodtypes/<int:pk>', api.BloodTypeDetail.as_view(), name='bloodtypes_detail_api'),

    path('api/admissiontypes', api.AdmissionTypeList.as_view(), name='admissiontypes_list_api'), 
    path('api/admissiontypes/<int:pk>', api.AdmissionTypeDetail.as_view(), name='admissiontypes_detail_api'),


    path('api/patients', csrf_exempt(api.PatientList.as_view()), name='patients_list_api'), 
    path('api/patients/<int:pk>', csrf_exempt(api.PatientDetail.as_view()), name='patients_detail_api'),

    path('api/admissions', api.AdmissionTypeList.as_view(), name='admissions_list_api'), 
    path('api/admissions/<int:pk>', api.AdmissionTypeDetail.as_view(), name='admissions_detail_api')
]

# Serving static files in development
if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

