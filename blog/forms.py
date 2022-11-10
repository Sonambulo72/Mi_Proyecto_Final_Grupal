from django import forms
from blog.models import Usuario

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','email', 'contraseña']
