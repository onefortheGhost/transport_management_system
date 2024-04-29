from rest_framework import serializers
from .models import Driver, DriverHistory, DriverLicense, DriverMedical

# Driver Serializers

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class DriverLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLicense
        fields = '__all__'

class DriverMedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverMedical
        fields = '__all__'

class DriverHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverHistory
        fields = '__all__'