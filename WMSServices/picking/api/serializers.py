from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from picking.models import Picking

class PickingSerializer(ModelSerializer):
    last_modification = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status = serializers.CharField(source='status.name')
    class Meta:
        model = Picking
        fields = '__all__'