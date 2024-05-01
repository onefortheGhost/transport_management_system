from rest_framework import viewsets
from .models import Dispatch
from .serializers import DispatchDatabaseSerializer


# API Serializers

class DispatchDatabaseViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchDatabaseSerializer