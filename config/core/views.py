from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Vehicle, Driver
from .serializers import VehicleSerializer, DriverSerializer, UserSerializer, VehicleMaintenanceSerializer, VehicleFuelRecordSerializer, VehicleInsuranceSerializer, VehicleInspectionSerializer
from rest_framework.permissions import AllowAny

# API Views

User = get_user_model()

class HomePageAPIViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []
    permission_classes = []

    def list(self, request):
        return Response({'message': 'Welcome to the API'})

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

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)
    def perform_create(self, serializer):
        serializer.save()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

# Frontend Views

class HomePageView(TemplateView):
    template_name = 'index.html' 

class WorkspaceDispatchBoard(TemplateView):
    template_name = 'dispatch_board.html'

class WorkspaceVehicles(TemplateView):
    template_name = 'vehicle_management.html'

class WorkspaceVehicleProfile(DetailView):
    template_name = 'vehicle_profile.html'

class WorkspaceDrivers(TemplateView):
    template_name = 'drivers.html'
