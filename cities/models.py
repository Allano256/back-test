from django.db import models
from django.conf import settings

from django.contrib.auth.models import User


class NewCity(models.Model):
    """
    Model for new City.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=150)
    date = models.DateField()
    notes = models.TextField(max_length=200)
    lng = models.FloatField(default=0.0)
    lat = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.city_name}, {self.date}, {self.notes}"
