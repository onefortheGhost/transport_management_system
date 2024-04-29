from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Vehicle
from .serializers import VehicleSerializer, VehicleFuelRecordSerializer, VehicleInsuranceSerializer, VehicleMaintenanceSerializer, VehicleInspectionSerializer

#   API Views
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleFuelRecordViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleFuelRecordSerializer

    def get_queryset(self):
        vehicle = get_object_or_404(Vehicle, id=self.kwargs['vehicle_id'])
        return vehicle.fuel_records.all()

class VehicleInsuranceViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleInsuranceSerializer

    def get_queryset(self):
        vehicle = get_object_or_404(Vehicle, id=self.kwargs['vehicle_id'])
        return vehicle.insurance.all()

class VehicleMaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleMaintenanceSerializer

    def get_queryset(self):
        vehicle = get_object_or_404(Vehicle, id=self.kwargs['vehicle_id'])
        return vehicle.maintenance.all()
    
class VehicleInspectionsViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleInspectionSerializer

    def get_queryset(self):
        vehicle = get_object_or_404(Vehicle, id=self.kwargs['vehicle_id'])
        return vehicle.inspections.all()
    
# End API Views