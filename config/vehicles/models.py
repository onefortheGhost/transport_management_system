from django.db import models

# Create your models here.
class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('Truck', 'Truck')
    )

    make = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    year = models.PositiveIntegerField()

    vin = models.CharField(max_length = 17, blank=True, null=True, unique=True)
    license_plate = models.CharField(max_length = 7, blank=True, null=True)
    mileage = models.PositiveIntegerField(blank=True, null=True) # miles
    fuel_capacity = models.PositiveIntegerField(blank=True, null=True) # gallons
    yard_assignment = models.CharField(max_length = 100, blank=True, null=True)
    registration_owner = models.CharField(max_length = 100, blank=True, null=True)

class VehicleInspection(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name = 'inspections', on_delete=models.CASCADE)
    inspection_interval = models.PositiveIntegerField(blank=True, null=True) # miles
    inspection_mileage = models.PositiveIntegerField(blank=True, null=True) # miles
    inspection_date = models.DateField(blank=True, null=True)

class VehicleInsurance(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name = 'insurance', on_delete=models.CASCADE)
    insurance_provider = models.CharField(max_length = 100, blank=True, null=True)
    insurance_policy_number = models.CharField(max_length = 100, blank=True, null=True)
    insurance_start = models.DateField(blank=True, null=True)
    insurance_expiration = models.DateField(blank=True, null=True)


class VehicleFuelRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name = 'fuel_records', on_delete=models.CASCADE)
    fuel_date = models.DateField()
    fuel_amount = models.PositiveIntegerField() # gallons
    fuel_cost = models.DecimalField(max_digits=5, decimal_places=2) # dollars
    fuel_odometer = models.PositiveIntegerField() # miles

class VehicleMaintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='maintenance', on_delete=models.CASCADE)
    empty_weight = models.PositiveIntegerField(blank=True, null=True) # lbs
    oil_change_interval = models.PositiveIntegerField(blank=True, null=True) # miles
    oil_change_mileage = models.PositiveIntegerField(blank=True, null=True) # miles
    tire_change_interval = models.PositiveIntegerField(blank=True, null=True) # miles
    tire_change_mileage = models.PositiveIntegerField(blank=True, null=True) # miles

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
  