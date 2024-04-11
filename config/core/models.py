from django.db import models

# Create your models here.

class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('Truck', 'Truck')
    )

    make = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.make} {self.model}"
    
class Driver(models.Model):

    First_Name = models.CharField(max_length = 100)
    Middle_Name = models.CharField(max_length = 100)
    Last_Name = models.CharField(max_length = 100)
    # Age

    # Address

    # License_Number
    # License_Date_Issuance
    # License_Date_Expiration
    # Endorsements
    # License_Photo_Front
    # License_Photo_Back

    # Medical

    # Driver_History

    