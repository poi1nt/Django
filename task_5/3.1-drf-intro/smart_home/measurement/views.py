from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer


# получение датчиков, создание датчика
class SensorCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# обновление датчика
class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# добавление измерения
class MeasurementCreate(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer



