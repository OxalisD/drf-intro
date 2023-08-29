from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurements

from .serializers import SensorSerializer, MeasurementsSerializer, \
    SensorDetailSerializer, MeasurementsSerializerAdd


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementView(ListCreateAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializerAdd


