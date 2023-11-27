# serializers.py
from rest_framework import serializers
from .models import Vibracion

class VibracionSerializer(serializers.ModelSerializer):
    intensidad = serializers.CharField(read_only=True)

    class Meta:
        model = Vibracion
        fields = ['intensidad', 'timestamp', 'valor_numerico']

    def create(self, validated_data):
        valor_numerico = validated_data.get('valor_numerico')
        validated_data['intensidad'] = self.calcular_intensidad(valor_numerico)
        return super().create(validated_data)

    def calcular_intensidad(self, valor_numerico):
        if valor_numerico >= 850:
            return 'Fuerte'
        elif valor_numerico >= 400:
            return 'Moderado'
        elif valor_numerico >= 0:
            return 'Débil'
        else:
            return 'Desconocido'
