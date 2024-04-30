from django.db import models

class DispatchBoard(models.Model):
    date_dispatch_creation = models.DateTimeField(auto_now_add=True)
    date_dispatch_last_modified = models.DateTimeField(auto_now=True)
    driver = models.ForeignKey('drivers.Driver', related_name='dispatch', on_delete=models.CASCADE) #TODO - Verify that delete cascade is correct
    pickup_date = models.DateField()
    pickup_location = models.CharField(max_length=255)

    dropoff_date = models.DateField()
    dropoff_location = models.CharField(max_length=255)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.driver} - {self.date} - {self.location}'