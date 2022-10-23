from django import forms
#from django.forms import forms
from ejemplo.models import Familiar

from ejemplo.models import Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=5)

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Familiar
        fields = ['nombre', 'direccion', 'numero_pasaporte']
