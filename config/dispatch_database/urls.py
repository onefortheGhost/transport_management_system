from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register(r'', views.DispatchDatabaseViewSet, basename='dispatch-database'),
router.register(r'(?P<dispatch_id>\d+)/', views.DispatchDatabaseViewSet, basename='dispatch'),

urlpatterns = [
    path('', include(router.urls)),
]