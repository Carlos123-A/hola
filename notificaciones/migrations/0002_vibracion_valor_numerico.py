# Generated by Django 4.2.7 on 2023-11-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vibracion',
            name='valor_numerico',
            field=models.IntegerField(default=50),
        ),
    ]