from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('cantantes', views.cantantes, name="Cantantes"),
    path('canciones', views.canciones, name="Canciones"),
    path('usuarios', views.usuarios, name="Usuarios"),
    path('cantanteFormulario', views.cantanteFormulario, name="CantanteFormulario"),
    path('cancionFormulario', views.cancionFormulario, name="CancionFormulario"),
    path('usuarioFormulario', views.usuarioFormulario, name="UsuarioFormulario"),
    path('usuario/list', views.UsuarioList.as_view(), name="ListUsuarios"),
    path(r'^(?P<pk>\d+)$', views.UsuarioDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.UsuarioCreacion.as_view(), name='Usuariocre'),
    path(r'^editar/(?P<pk>\d+)$', views.UsuarioUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.UsuarioDelete.as_view(), name='Delete'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(
        template_name='AppCoder/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('busquedaUsuario', views.busquedaUsuario),
    path('buscar/', views.buscar),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('about', views.about, name="About"),
]
