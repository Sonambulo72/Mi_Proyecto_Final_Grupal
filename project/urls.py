"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from ejemplo.views import ( ListarPersona, monstrar_familiares, BuscarFamiliar,CargarPersona,
                    CargarAutos,ListarAutos,CargarMotos,ListarMotos) 
#from blog.views import index as blog_index # import de URL Blog
from ejemplo.models import Familiar, Auto, Moto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-familia/', monstrar_familiares), # import de mi-familia
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/listar',ListarPersona.as_view()),
    path('mi-familia/cargar',CargarPersona.as_view()),
    path('mi-auto/listarautos',ListarAutos.as_view()),
    path('mi-auto/cargarautos',CargarAutos.as_view()),
    path('mi-moto/listarmotos',ListarMotos.as_view()),
    path('mi-moto/cargarmotos',CargarMotos.as_view()),
    path('panel-familia/', include ('panel_familia.urls')),
    path('blog/', include('blog.urls')),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
