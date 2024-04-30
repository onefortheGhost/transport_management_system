from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register(r'', views.DispatchBoardViewSet, basename='dispatch-board'),
router.register(r'(?P<dispatch_id>\d+)/', views.DispatchBoardViewSet, basename='dispatch'),

urlpatterns = [
    path('', include(router.urls)),
]