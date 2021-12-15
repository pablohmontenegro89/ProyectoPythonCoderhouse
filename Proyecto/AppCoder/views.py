from django.shortcuts import render
#from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
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
    return render(request, 'AppCoder/inicio.html')


def cantantes(request):
    return render(request, 'AppCoder/cantantes.html')


def canciones(request):
    return render(request, 'AppCoder/canciones.html')


def usuarios(request):
    return render(request, 'AppCoder/usuarios.html')
