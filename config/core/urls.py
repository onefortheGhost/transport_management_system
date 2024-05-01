from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

app_name = 'core'

router = DefaultRouter()
router.register(r'homepage', views.HomePageAPIViewSet, basename='homepage')

router.register(r'vehicles', views.VehicleViewSet, basename='vehicle-list')
router.register(r'drivers', views.DriverViewSet, basename='driver')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', views.HomePageView.as_view(), name='workspace'),
    path('workspace/dispatch-board/', views.WorkspaceDispatchBoard.as_view(), name='dispatch-board'),
    path('workspace/vehicle-management/', views.WorkspaceVehicles.as_view(), name='vehicles'),
    path('workspace/vehicle-profile/<int:pk>/', views.WorkspaceVehicleProfile.as_view(), name='vehicle-profile'),
    path('workspace/driver-management/', views.WorkspaceDrivers.as_view(), name='drivers'),
    path('workspace/driver-profile/<int:pk>/', views.WorkspaceDriverProfile.as_view(), name='driver-profile'),
]