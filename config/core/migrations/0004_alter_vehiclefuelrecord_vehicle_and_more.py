# Generated by Django 5.0.3 on 2024-04-18 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_customer_remove_driver_driver_license_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclefuelrecord',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuel_record', to='core.vehicle'),
        ),
        migrations.AlterField(
            model_name='vehicleinspection',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspections', to='core.vehicle'),
        ),
        migrations.AlterField(
            model_name='vehicleinsurance',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance', to='core.vehicle'),
        ),
        migrations.AlterField(
            model_name='vehiclemaintenance',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance', to='core.vehicle'),
        ),
    ]