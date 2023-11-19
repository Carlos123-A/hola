from django.db import models

from django.contrib.auth.models import User

class Vibracion(models.Model):
    intensidad = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

