# Generated by Django 5.0.3 on 2024-04-18 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customuser_is_dispatcher_customuser_is_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('contact_person', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='driver',
            name='Driver_License',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='Driver_License_Class',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='Driver_License_Date_Expiration',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='Driver_License_Date_Issuance',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='Driver_License_Endorsements',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='Driver_License_Restrictions',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='Driver_License_State',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='License_Photo_Back',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='License_Photo_Front',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='destination_eta',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='destination_gps',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='empty_weight',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_GPM',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_GPM_Total',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_GPM_rolling_average_1000',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_GPM_rolling_average_10000',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_GPM_rolling_average_5000',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_MPG',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_MPG_Total',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_MPG_rolling_average_1000',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_MPG_rolling_average_10000',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_MPG_rolling_average_5000',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='inspection_date',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='inspection_interval',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='inspection_mileage',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='insurance_expiration',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='insurance_policy_number',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='insurance_provider',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='insurance_start',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='location',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='location_gps',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='oil_change_interval',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='oil_change_mileage',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='tire_change_interval',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='tire_change_mileage',
        ),
        migrations.AddField(
            model_name='driver',
            name='Additional_Info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(blank=True, max_length=17, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='CustomerContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=100)),
                ('invoice_date', models.DateField()),
                ('invoice_due_date', models.DateField()),
                ('invoice_amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
        ),
        migrations.CreateModel(
            name='DispatchOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_ID', models.CharField(max_length=100)),
                ('pickup_location', models.CharField(max_length=100)),
                ('pickup_date', models.DateTimeField()),
                ('delivery_destination', models.CharField(max_length=100)),
                ('delivery_date', models.DateTimeField()),
                ('customer', models.CharField(max_length=100)),
                ('bill_of_lading', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Pending', 'Pending'), ('Dispatched', 'Dispatched'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Draft', max_length=100)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.driver')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DriverHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.driver')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Driver_License', models.CharField(max_length=20)),
                ('Driver_License_State', models.CharField(max_length=2)),
                ('Driver_License_Date_Issuance', models.DateField()),
                ('Driver_License_Date_Expiration', models.DateField(blank=True, null=True)),
                ('Driver_License_Class', models.CharField(blank=True, max_length=4, null=True)),
                ('Driver_License_Restrictions', models.CharField(blank=True, max_length=4, null=True)),
                ('Driver_License_Endorsements', models.CharField(blank=True, max_length=4, null=True)),
                ('License_Photo_Front', models.ImageField(blank=True, null=True, upload_to='license_photos/')),
                ('License_Photo_Back', models.ImageField(blank=True, null=True, upload_to='license_photos/')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.driver')),
            ],
        ),
        migrations.CreateModel(
            name='DriverMedical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.driver')),
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
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleInspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_interval', models.PositiveIntegerField(blank=True, null=True)),
                ('inspection_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('inspection_date', models.DateField(blank=True, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehicle')),
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
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehicle')),
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
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehicle')),
            ],
        ),
    ]
