from django import forms


class CantanteFormulario(forms.Form):

    # Especificar los campos
    nombre = forms.CharField()
    edad = forms.IntegerField()
    genero = forms.CharField()


class CancionFormulario(forms.Form):

    # Especificar los campos
    nombre = forms.CharField()
    duracion = forms.IntegerField()
    genero = forms.CharField()


class UsuarioFormulario(forms.Form):

    # Especificar los campos
    nombre = forms.CharField()
    mail = forms.CharField()
    edad = forms.IntegerField()
