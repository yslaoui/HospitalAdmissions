import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy


from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


from .model_factories import *
from .serializers import *
import logging


class AdmissionTest(APITestCase):
   
    admission1 = None
    admission2 = None
    admission3 = None
    good_url = ''
    bad_url = ''
    delete_url = ''
    post_url = ''


    def setUp(self):
        self.admission1 = AdmissionFactory.create(pk=1)
        self.admission2 = AdmissionFactory.create(pk=2)
        self.admission3 = AdmissionFactory.create(pk=3)
        self.admission4 = AdmissionFactory.create(pk=4)
        self.good_url = reverse('admissions_detail_api', kwargs={'pk': 1})
        self.bad_url = '/api/admissions/H'
        self.delete_url = reverse('admissions_detail_api', kwargs={'pk': 3})
        self.post_url = reverse('admissions_list_api')

    def tearDown(self):
        models_to_clear =  [
                TestResult, Medication, MedicalCondition, Insurance, 
                Hospital, Gender, Doctor, BloodType, AdmissionType, 
                Patient, Admission ]
        factories_to_clear =  [
                TestResultfactory, MedicalConditionfactory, MedicalConditionfactory, 
                Insurancefactory, Hospitalfactory, Genderfactory, Doctorfactory, 
                BloodTypefactory, AdmissionFactory,  PatientFactory, AdmissionFactory ]
        for model in models_to_clear:
             model.objects.all().delete()
        for factory in factories_to_clear:
            factory.reset_sequence(0)

    def test_admissionDetailReturnSuccess(self):
        admission = self.admission1
        response = self.client.get(self.good_url, format = 'json')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('hospital' in data)
        self.assertEqual(data['medication'], 1)


    def test_geneDetailReturnFailureOnBadPk(self):
        admission = self.admission2
        url = self.bad_url
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_geneDetailDeleteSuccess(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, 204)

#     def test_genePostSuccess(self):
#         # sel.client.post does not accept a model instance, but a python dictionary
#         # Setup logger
#         logger = logging.getLogger('django')
#         post_data = {
#             "date_of_admission": self.admission4.date_of_admission,
#             "room_number": self.admission4.room_number,
#             "billing_amount": self.admission4.billing_amount,
#             "discharge_date": self.admission4.discharge_date,
#             "patient": self.admission4.patient.id,
#             "hospital": self.admission4.hospital.id,
#             "doctor": self.admission4.doctor.id,
#             "medication": self.admission4.medication.id,
#             "insurance": self.admission4.insurance.id,
#             "admission_type": self.admission4.admission_type.id,
#             "test_result": self.admission4.test_result.id,
#             "medical_condition": self.admission4.medical_condition.id
# }
#         response = self.client.post(self.post_url, post_data, format='json')
#         # Log the response
#         logger.debug(response)
#         self.assertEqual(response.status_code, 201)  