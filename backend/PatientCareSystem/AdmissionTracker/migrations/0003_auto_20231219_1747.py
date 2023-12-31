# Generated by Django 3.0.3 on 2023-12-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmissionTracker', '0002_auto_20231219_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='medication',
            field=models.ManyToManyField(blank=True, null=True, through='AdmissionTracker.PatientMedicationLink', to='AdmissionTracker.Medication'),
        ),
    ]