from rest_framework import serializers
from .models import Vehicle, Driver, VehicleFuelRecord, VehicleInspection, VehicleMaintenance, VehicleInsurance
from django.contrib.auth import get_user_model

#Vehicle Serializer
class VehicleInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInsurance
        fields = '__all__'

class VehicleFuelRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleFuelRecord
        fields = '__all__'

class VehicleInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInspection
        fields = '__all__'

class VehicleMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMaintenance
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    inspections = VehicleInspectionSerializer(many=True, read_only=True)
    maintenance = VehicleMaintenanceSerializer(many=True, read_only=True)
    fuel_records = VehicleFuelRecordSerializer(many=True, read_only=True)
    insurance = VehicleInsuranceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Vehicle
        fields = '__all__'


#End Vehicle Serializer

#Driver Serializer
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
#End Driver Serializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'is_driver', 'is_dispatcher']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            is_driver=validated_data['is_driver'],
            is_dispatcher=validated_data['is_dispatcher']
        )
        return user
