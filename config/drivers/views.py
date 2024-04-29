from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Driver, DriverLicense, DriverMedical, DriverHistory
from .serializers import DriverSerializer, DriverLicenseSerializer, DriverMedicalSerializer, DriverHistorySerializer


#  API Views
class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverLicenseViewSet(viewsets.ModelViewSet):
    queryset = DriverLicense.objects.all()
    serializer_class = DriverLicenseSerializer

    def get_queryset(self):
        driver = get_object_or_404(Driver, id=self.kwargs['driver_id'])
        return driver.license.all()
    
class DriverMedicalViewSet(viewsets.ModelViewSet):
    queryset = DriverMedical.objects.all()
    serializer_class = DriverMedicalSerializer

    def get_queryset(self):
        driver = get_object_or_404(Driver, id=self.kwargs['driver_id'])
        return driver.medical.all()
    
class DriverHistoryViewSet(viewsets.ModelViewSet):
    queryset = DriverHistory.objects.all()
    serializer_class = DriverHistorySerializer

    def get_queryset(self):
        driver = get_object_or_404(Driver, id=self.kwargs['driver_id'])
        return driver.history.all()