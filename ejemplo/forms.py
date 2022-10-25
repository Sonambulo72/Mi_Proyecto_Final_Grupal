from django import forms
from ejemplo.models import Familiar,Auto,Moto


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=5)

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Familiar
        fields = ['nombre', 'direccion', 'numero_pasaporte']

# Agrego las dos clases Auto y Moto

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['patente', 'marca', 'kms']

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['patente', 'marca', 'cilindrada']
