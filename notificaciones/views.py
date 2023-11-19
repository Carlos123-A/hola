# notificaciones/views.py

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import Vibracion
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Vibracion
from .serializers import VibracionSerializer

class ListaVibracionesAPI(ModelViewSet):
    queryset = Vibracion.objects.all()
    serializer_class = VibracionSerializer

    @action(detail=False, methods=['post'])
    def enviar_datos(self, request):
        serializer = VibracionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Otras acciones del ModelViewSet (list, retrieve, create, etc.) permanecen aquí


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Asegúrate de que el nombre del template sea correcto

def listar_vibraciones(request):
    vibraciones = Vibracion.objects.all()
    return render(request, 'notificaciones/listar_vibraciones.html', {'vibraciones': vibraciones})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log in the user
            user = form.get_user()
            login(request, user)
            return redirect('/notificaciones/')  # Redirige a la página deseada
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def registro_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar_vibraciones')  # Puedes redirigir a la página que desees después del registro
    else:
        form = CustomUserCreationForm()

    return render(request, 'registro_usuario.html', {'form': form})


class ListaVibracionesAPI(ModelViewSet):
    queryset = Vibracion.objects.all()
    serializer_class = VibracionSerializer

