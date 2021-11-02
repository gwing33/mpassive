from django.db import models
# from django.contrib.auth.models import User


class Device(models.Model):
    id = models.fields.UUIDField(primary_key=True)
    name = models.fields.CharField(max_length=255)
    ip = models.fields.GenericIPAddressField()


class Sensor(models.Model):
    id = models.fields.UUIDField(primary_key=True)
    type = models.fields.CharField(max_length=50)
    device_id = models.ForeignKey(Device, on_delete=models.DO_NOTHING)


class SensorData(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
