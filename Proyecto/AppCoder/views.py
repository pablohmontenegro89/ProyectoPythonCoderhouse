from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
#from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
# Para el login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
# Create your views here.


def cantanteFormulario(request):
    # obtiene la dirección y el anioFund

    if request.method == "POST":
        miCantanteFormulario = CantanteFormulario(request.POST)
        if miCantanteFormulario.is_valid():  # va con ()
            informacion = miCantanteFormulario.cleaned_data  # va sin () creo
            cantanteInsta = Cantante(
                nombre=informacion["nombre"], edad=informacion["edad"], genero=informacion["genero"])
            cantanteInsta.save()  # guarda en bd
            return render(request, 'AppCoder/inicio.html')
    else:
        miCantanteFormulario = CantanteFormulario()
    # return HttpResponse("Esto es una prueba de inicio")
    return render(request, 'AppCoder/cantanteFormulario.html', {"miCantanteFormulario": miCantanteFormulario})


def cancionFormulario(request):
    # obtiene la dirección y el anioFund

    if request.method == "POST":
        miCancionFormulario = CancionFormulario(request.POST)
        if miCancionFormulario.is_valid():  # va con ()
            informacion = miCancionFormulario.cleaned_data  # va sin () creo
            cancionInsta = Cancion(
                nombre=informacion["nombre"], duracion=informacion["duracion"], genero=informacion["genero"])
            cancionInsta.save()  # guarda en bd
            return render(request, 'AppCoder/inicio.html')
    else:
        miCancionFormulario = CancionFormulario()
    # return HttpResponse("Esto es una prueba de inicio")
    return render(request, 'AppCoder/cancionFormulario.html', {"miCancionFormulario": miCancionFormulario})


def usuarioFormulario(request):
    # obtiene la dirección y el anioFund

    if request.method == "POST":
        miUsuarioFormulario = UsuarioFormulario(request.POST)
        if miUsuarioFormulario.is_valid():  # va con ()
            informacion = miUsuarioFormulario.cleaned_data  # va sin () creo
            UsuarioInsta = Usuario(
                nombre=informacion["nombre"], mail=informacion["mail"], edad=informacion["edad"])
            UsuarioInsta.save()  # guarda en bd
            return render(request, 'AppCoder/inicio.html')
    else:
        miUsuarioFormulario = UsuarioFormulario()
    # return HttpResponse("Esto es una prueba de inicio")
    return render(request, 'AppCoder/usuarioFormulario.html', {"miUsuarioFormulario": miUsuarioFormulario})


def inicio(request):
    # return HttpResponse("Esto es una prueba de inicio")
    diccionario = {}
    cantidadDeAvatares = 0

    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id)

        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1

        diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url

    # return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html', diccionario)


def cantantes(request):
    return render(request, 'AppCoder/cantantes.html')


def canciones(request):
    return render(request, 'AppCoder/canciones.html')


def usuarios(request):
    return render(request, 'AppCoder/usuarios.html')


def about(request):
    return render(request, 'AppCoder/about.html')


def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
        # respuesta = f"ESTOY BUSCANDO A :{request.GET['nombre']}"

        # el diccionario lo agregué yo
        return render(request, "AppCoder/resultadoBusqueda.html", {"usuarios": usuarios, "nombre": nombre})
    else:
        respuesta = "Che, mandame información"
    return HttpResponse(respuesta)


def busquedaUsuario(request):
    return render(request, 'AppCoder/busquedaUsuario.html')


class UsuarioList(ListView):
    model = Usuario
    template_name = "AppCoder/usuarios_list.html"


class UsuarioDetalle(DetailView):
    model = Usuario
    template_name = "AppCoder/usuario_detalle.html"


class UsuarioCreacion(CreateView):
    model = Usuario
    success_url = "../AppCoder/usuario/list"  # AppCoder/template/AppCoder/editar
    fields = ["nombre", "mail", "edad"]


class UsuarioUpdate(UpdateView):

    model = Usuario
    success_url = "../usuario/list"
    fields = ["nombre", "mail", "edad"]


class UsuarioDelete(DeleteView):

    model = Usuario
    success_url = "../usuario/list"


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:

                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje": f"BIENVENIDO, {usuario}!!!!"})

            else:

                return render(request, "AppCoder/inicio.html", {"mensaje": f"DATOS MALOS :(!!!!"})

        else:

            return render(request, "AppCoder/inicio.html", {"mensaje": f"FORMULARIO erroneo"})

    form = AuthenticationForm()  # Formulario sin nada para hacer el login

    return render(request, "AppCoder/login.html", {"form": form})


def register(request):

    if request.method == 'POST':

        #form = UserCreationForm(request.POST)

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']

            form.save()

            return render(request, "AppCoder/inicio.html",  {"mensaje": f"{username} Creado :)"})

    else:
        #form = UserCreationForm()

        form = UserRegisterForm()

    return render(request, "AppCoder/register.html",  {"form": form})


@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


@login_required
def agregarAvatar(request):
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():  # Si pasó la validación de Django

            u = User.objects.get(username=request.user)

            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])

            avatar.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = AvatarFormulario()  # Formulario vacio para construir el html

    return render(request, "AppCoder/agregarAvatar.html", {"miFormulario": miFormulario})
