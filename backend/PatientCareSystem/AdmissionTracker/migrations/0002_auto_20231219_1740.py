# Generated by Django 3.0.3 on 2023-12-19 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdmissionTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientMedicationLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AdmissionTracker.Medication')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AdmissionTracker.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='medication',
            field=models.ManyToManyField(through='AdmissionTracker.PatientMedicationLink', to='AdmissionTracker.Medication'),
        ),
    ]
