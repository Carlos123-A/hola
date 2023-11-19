from rest_framework import serializers
from .models import Vibracion

class VibracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vibracion
        fields = ['intensidad', 'timestamp']
