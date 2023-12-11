# models.py
from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models



class Vibracion(models.Model):
    intensidad = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    valor_numerico = models.DecimalField(default=50.0, max_digits=5, decimal_places=2)

    def calcular_intensidad(self):
        if self.valor_numerico >= 2:  
            return 'Fuerte'
        elif self.valor_numerico >= 1:  
            return 'Moderado'
        elif self.valor_numerico >= 0:  
            return 'Débil'
        else:
            return 'Desconocido'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
