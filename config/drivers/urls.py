from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()

router.register(r'', views.DriverViewSet, basename='driver-list'),
router.register(r'(?P<driver_id>\d+)/', views.DriverViewSet, basename='driver'),
router.register(r'(?P<driver_id>\d+)/license/', views.DriverLicenseViewSet, basename='driver-license'),
router.register(r'(?P<driver_id>\d+)/medical/', views.DriverMedicalViewSet, basename='driver-medical'),
router.register(r'(?P<driver_id>\d+)/history/', views.DriverHistoryViewSet, basename='driver-history'),

urlpatterns = [
    path('', include(router.urls)),
]