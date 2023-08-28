from rest_framework import serializers

from measurement.models import Sensor, Measurement


class MeasurementSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSensorSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']