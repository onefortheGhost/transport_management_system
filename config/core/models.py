from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')

        if username is None:
            raise TypeError('Users must have a username.')

        user = self.model(email=self.normalize_email(email), username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, username, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    #   Roles and Permissions
    is_dispatcher = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


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
    Driver_License = models.CharField(max_length = 20)
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


class DispatchOrder(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Pending', 'Pending'),
        ('Dispatched', 'Dispatched'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )
    load_ID = models.CharField(max_length = 100)
    pickup_location = models.CharField(max_length = 100)
    pickup_date = models.DateTimeField()
    delivery_destination = models.CharField(max_length = 100)
    delivery_date = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer = models.CharField(max_length = 100)
    bill_of_lading = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100, choices=STATUS_CHOICES, default='Draft')

class Customer(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 5)
    phone_number = models.CharField(max_length = 10)
    email = models.EmailField()
    contact_person = models.CharField(max_length = 100)

class CustomerContact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class CustomerInvoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length = 100)
    invoice_date = models.DateField()
    invoice_due_date = models.DateField()
    invoice_amount = models.DecimalField(max_digits=5, decimal_places=2)