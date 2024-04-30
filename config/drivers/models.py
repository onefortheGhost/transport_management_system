from django.db import models

STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
    ('AS', 'American Samoa'),
    ('DC', 'District of Columbia'),
    ('FM', 'Federated States of Micronesia'),
    ('GU', 'Guam'),
    ('MH', 'Marshall Islands'),
    ('MP', 'Northern Mariana Islands'),
    ('PW', 'Palau'),
    ('PR', 'Puerto Rico'),
    ('VI', 'Virgin Islands'),
    ('AE', 'Armed Forces Africa'),
    ('AA', 'Armed Forces Americas (except Canada)'),
    ('AE', 'Armed Forces Canada'),
    ('AE', 'Armed Forces Europe'),
    ('AE', 'Armed Forces Middle East'),
    ('AP', 'Armed Forces Pacific'),
)

# Create your models here.
class Driver(models.Model):
    First_Name = models.CharField(max_length = 100)
    Middle_Name = models.CharField(max_length = 100, blank=True, null=True)
    Last_Name = models.CharField(max_length = 100)
    Date_of_Birth = models.DateField(blank=True, null=True)

    Address = models.CharField(max_length = 100, blank=True, null=True)
    City = models.CharField(max_length = 100, blank=True, null=True)
    State = models.CharField(max_length = 2, choices=STATES, blank=True, null=True)

    Phone_Number = models.CharField(max_length = 10, blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)

    Additional_Info = models.TextField(blank=True, null=True)

class DriverLicense(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Driver_License = models.CharField(max_length = 20, unique=True) # Unique number across all drivers
    Driver_License_State = models.CharField(max_length = 2, choices=STATES) # State where license was issued - Dependency on STATES
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

