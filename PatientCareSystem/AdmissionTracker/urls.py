from django.urls import include, path
from . import api

urlpatterns = [
    path('api/admissions', api.AdmissionList.as_view(), name='admission_list_api'), 
    path('api/admissions/<int:pk>', api.AdmissionDetail.as_view(), name='admission_detail_api'),
]
