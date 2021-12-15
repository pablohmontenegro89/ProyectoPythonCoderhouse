from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('cantantes', views.cantantes, name="Cantantes"),
    path('canciones', views.canciones, name="Canciones"),
    path('usuarios', views.usuarios, name="Usuarios"),
    path('cantanteFormulario', views.cantanteFormulario, name="CantanteFormulario"),
    path('cancionFormulario', views.cancionFormulario, name="CancionFormulario"),
    path('usuarioFormulario', views.usuarioFormulario, name="UsuarioFormulario"),
]
