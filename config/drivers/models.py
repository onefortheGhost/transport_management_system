from django.db import models

# Create your models here.
class Driver(models.Model):
    First_Name = models.CharField(max_length = 100)
    Middle_Name = models.CharField(max_length = 100, blank=True, null=True)
    Last_Name = models.CharField(max_length = 100)
    Date_of_Birth = models.DateField()

    Address = models.CharField(max_length = 100)
    City = models.CharField(max_length = 100)
    State = models.CharField(max_length = 2)

    Phone_Number = models.CharField(max_length = 10)
    Email = models.EmailField()

    Additional_Info = models.TextField(blank=True, null=True)

class DriverLicense(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Driver_License = models.CharField(max_length = 20 unique=True)
    Driver_License_State = models.CharField(max_length = 2)
    Driver_License_Date_Issuance = models.DateField()
    Driver_License_Date_Expiration = models.DateField(blank=True, null=True)
    Driver_License_Class = models.CharField(max_length = 4, blank=True, null=True)
    Driver_License_Restrictions = models.CharField(max_length = 4, blank=True, null=True)
    Driver_License_Endorsements = models.CharField(max_length = 4, blank=True, null=True)
    License_Photo_Front = models.ImageField(upload_to='license_photos/', blank=True, null=True)
    License_Photo_Back = models.ImageField(upload_to='license_photos/', blank=True, null=True)

class DriverMedical(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

class DriverHistory(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

