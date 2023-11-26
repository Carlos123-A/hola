# Generated by Django 4.2.7 on 2023-11-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificaciones', '0002_vibracion_valor_numerico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vibracion',
            name='valor_numerico',
            field=models.DecimalField(decimal_places=2, default=50.0, max_digits=5),
        ),
    ]