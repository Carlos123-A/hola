from django.urls import path, include
from .views import listar_vibraciones, login_view, registro_usuario,  ListaVibracionesAPI, profile_view
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'vibraciones', ListaVibracionesAPI, 'api')


urlpatterns = [
    path('vibraciones/', listar_vibraciones, name='listar_vibraciones'),
    path('api/', include(router.urls) ),  
    path('login/', login_view, name='login'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('vibraciones/enviar_datos/', ListaVibracionesAPI.as_view({'post': 'enviar_datos'}), name='enviar_datos'),

]