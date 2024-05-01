from rest_framework import serializers
from .models import Dispatch

class DispatchDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = '__all__'