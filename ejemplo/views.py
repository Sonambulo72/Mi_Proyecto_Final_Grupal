from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, PersonaForm 
from django.views import View

#resueve lista de personas por Funcion
def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", 
                {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):

        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})

#resolver listar familiares con clases
class ListarPersona(View):
    template_name = "ejemplo/lista_de_personas.html"

    def get(self, request):
        familiar = Familiar.objects.all()
        return render(request, self.template_name,{"familiar" : familiar})

#Carga de familiares
class CargarPersona(View):
    template_name = "ejemplo/carga_de_personas.html"
    form_class = PersonaForm
    initial = {"nombre": "", "direccion": "", "numero_pasaporte": ""}


    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{"form" : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)

        return render(request, self.template_name, {"form": form})

