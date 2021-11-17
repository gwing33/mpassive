import uuid
from django.db import models
# from django.contrib.auth.models import User

class Device(models.Model):
    id = models.fields.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.fields.CharField(max_length=255)
    ip = models.fields.GenericIPAddressField()


class Sensor(models.Model):
    id = models.fields.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.fields.CharField(max_length=50)
    device_id = models.ForeignKey(Device, on_delete=models.DO_NOTHING)


class SensorData(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
