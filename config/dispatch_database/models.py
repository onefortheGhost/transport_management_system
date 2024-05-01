from django.db import models


class Dispatch(models.Model):
    date_dispatch_creation = models.DateTimeField(auto_now_add=True)
    date_dispatch_last_modified = models.DateTimeField(auto_now=True)

    driver = models.ForeignKey('drivers.Driver', related_name='dispatch', on_delete=models.CASCADE) #TODO - Verify that delete cascade is correct
    vehicle = models.ForeignKey('vehicles.Vehicle', related_name='dispatch', on_delete=models.CASCADE) #TODO - Verify that delete cascade is correct
    status = models.CharField(max_length=255, default='Pending')

    # Pickup information
    pickup_date_start = models.DateField()
    pickup_date_end = models.DateField()
    pickup_location = models.CharField(max_length=255)

    # Dropoff information
    dropoff_date_start = models.DateField()
    dropoff_date_end = models.DateField()
    dropoff_location = models.CharField(max_length=255)

    # Payload Information
    load_type = models.CharField(max_length=255)
    load_weight = models.DecimalField(max_digits=10, decimal_places=2)
    load_value = models.DecimalField(max_digits=10, decimal_places=2)
    load_hazmat = models.BooleanField(default=False)

    # Additional information
    is_team_driving = models.BooleanField(default=False)
    is_expedited = models.BooleanField(default=False)
    is_underweightlimit = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.driver} - {self.date} - {self.location}'