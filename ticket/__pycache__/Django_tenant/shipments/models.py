from django.db import models
from locations.models import Location
from drivers.models import Driver
# Create your models here.
class Shipment(models.Model):
    origin = models.ForeignKey(Location, on_delete=models.CASCADE)
    destination = models.ForeignKey(Location, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    completion = models.DateTimeField()
    