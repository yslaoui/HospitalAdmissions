"""PatientCareSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('AdmissionTracker.urls')),
    path('admin/', admin.site.urls),
    path('apischema/',
         get_schema_view(
             title = 'Patient Admission Tracker REST API',
             description = 'API for interacting with gene records',
             version = '1.0'
         ), name='openapi-schema'), 
    path('swaggerdocs/',
         TemplateView.as_view(
             template_name = 'AdmissionTracker/swagger-docs.html',
             extra_context = {'schema_url': 'openapi-schema'}
         ), name='swagger-ui')
]
