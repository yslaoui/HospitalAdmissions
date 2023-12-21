# Configuring the script to work with the bioweb django project
import os
import sys

import django
from django.db import connection
import csv
from collections import defaultdict

sys.path.append('/home/quantumleap/Documents/git/uol/course/4_Level6S1/django/midterm/work/PatientCareSystem')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PatientCareSystem.settings')

django.setup()

# Import models to be able to add data to models
from AdmissionTracker.models import *

# Import logging library
import logging
logger = logging.getLogger(__name__)

# Define path to data
data_file = './healthcare_dataset_small.csv'


admissions = Admission.objects.get(pk=25)
print(admissions)