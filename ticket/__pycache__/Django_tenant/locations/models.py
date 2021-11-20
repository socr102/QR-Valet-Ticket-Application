from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255,unique=True)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()