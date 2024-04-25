from rest_framework import serializers
from .models import Vehicle, VehicleFuelRecord, VehicleInspection, VehicleMaintenance, VehicleInsurance

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