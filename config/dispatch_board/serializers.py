from rest_framework import serializers

class DispatchBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchBoard
        fields = '__all__'