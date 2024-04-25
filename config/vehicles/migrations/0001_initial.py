# Generated by Django 5.0.3 on 2024-04-23 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('vin', models.CharField(blank=True, max_length=17, null=True, unique=True)),
                ('license_plate', models.CharField(blank=True, max_length=7, null=True)),
                ('mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('fuel_capacity', models.PositiveIntegerField(blank=True, null=True)),
                ('yard_assignment', models.CharField(blank=True, max_length=100, null=True)),
                ('registration_owner', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleFuelRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_date', models.DateField()),
                ('fuel_amount', models.PositiveIntegerField()),
                ('fuel_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fuel_odometer', models.PositiveIntegerField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuel_records', to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleInspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_interval', models.PositiveIntegerField(blank=True, null=True)),
                ('inspection_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('inspection_date', models.DateField(blank=True, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspections', to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_provider', models.CharField(blank=True, max_length=100, null=True)),
                ('insurance_policy_number', models.CharField(blank=True, max_length=100, null=True)),
                ('insurance_start', models.DateField(blank=True, null=True)),
                ('insurance_expiration', models.DateField(blank=True, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance', to='vehicles.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty_weight', models.PositiveIntegerField(blank=True, null=True)),
                ('oil_change_interval', models.PositiveIntegerField(blank=True, null=True)),
                ('oil_change_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('tire_change_interval', models.PositiveIntegerField(blank=True, null=True)),
                ('tire_change_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance', to='vehicles.vehicle')),
            ],
        ),
    ]
