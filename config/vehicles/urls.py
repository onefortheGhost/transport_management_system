from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()

router.register(r'', views.VehicleViewSet, basename='vehicle-list'),
router.register(r'(?P<vehicle_id>\d+)/', views.VehicleViewSet, basename='vehicle'),
router.register(r'(?P<vehicle_id>\d+)/fuel_records', views.VehicleFuelRecordViewSet, basename='vehicle-fuel-records'),
router.register(r'(?P<vehicle_id>\d+)/insurance', views.VehicleInsuranceViewSet, basename='vehicle-insurance'),
router.register(r'(?P<vehicle_id>\d+)/maintenance', views.VehicleMaintenanceViewSet, basename='vehicle-maintenance'),
router.register(r'(?P<vehicle_id>\d+)/inspections', views.VehicleInspectionsViewSet, basename='vehicle-inspections'),

urlpatterns = [
    path('', include(router.urls)),
]