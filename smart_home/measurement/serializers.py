from rest_framework import serializers
from .models import Sensor, Measurements


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['temperature', 'created_at']


class MeasurementsSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = '__all__'


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['name', 'description', 'measurements']

