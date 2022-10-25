from django.shortcuts import render
from ejemplo.models import Familiar,Auto,Moto # importo las clases de models
from ejemplo.forms import Buscar, PersonaForm,AutoForm,MotoForm
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

# Defino las vistas de clases de las dos nuevas clases

#Listar Autos
class ListarAutos(View):
    template_name = "ejemplo/lista_de_autos.html"

    def get(self, request):
        auto = Auto.objects.all()
        return render(request, self.template_name,{"auto" : auto})

#Carga de autos
class CargarAutos(View):
    template_name = "ejemplo/carga_de_autos.html"
    form_class = AutoForm
    initial = {"patente": "", "marca": "", "kms": ""}


    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{"form" : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)

        return render(request, self.template_name, {"form": form})

#Defino las clases para moto

#resolver listar Motos con clases
class ListarMotos(View):
    template_name = "ejemplo/lista_de_motos.html"

    def get(self, request):
        moto = Moto.objects.all()
        return render(request, self.template_name,{"moto" : moto})

#Carga de motos
class CargarMotos(View):
    template_name = "ejemplo/carga_de_motos.html"
    form_class = MotoForm
    initial = {"patente": "", "marca": "", "cilindrada": ""}


    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{"form" : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)

        return render(request, self.template_name, {"form": form})