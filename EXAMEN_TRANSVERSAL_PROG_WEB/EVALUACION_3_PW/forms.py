from django import forms
from django.forms import ModelForm
from base_de_datos.models import usuario
from .views import FormularioRegistro,usuario_registro,formulario


class FormRegistro(ModelForm):
    class Meta:
        model = usuario
        fields =['nombre_usuario','contrasena']
