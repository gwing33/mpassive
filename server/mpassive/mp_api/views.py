from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from mpassive.mp_app.models import Device, Sensor, SensorData
from .serializers import UserSerializer, GroupSerializer, DeviceSerializer, SensorSerializer, SensorDataSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows devices to be viewed or edited.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sensors to be viewed or edited.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Sensor.objects.all()
        device_id = self.request.query_params.get('device_id')
        if device_id is not None:
            queryset = queryset.filter(device_id=device_id)
        return queryset

    @action(detail=True)
    def sensor_data(self, request, pk=None):
        """
        Returns a list of all data that belongs to a sensor
        """
        # user = self.get_object()
        # groups = SensorData.objects.all()
        return Response([data.sensor_id for data in SensorData])
