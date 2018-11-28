from django.shortcuts import render
from .models import Espacio
from django.views import generic

# Create your views here.

class IndexList(generic.ListView):
    template_name="registro/IndexList.html"
    model = Espacio

class Modificar(generic.UpdateView):
    template_name="registro/Modificar.html"
    model = Espacio
    fields = ["id_mat","nom_mat","id_int", "nom_int","id_vesp", "nom_vesp"]
    success_url= "/"

class Crear(generic.CreateView):
    template_name="registro/Crear.html"
    model = Espacio
    fields = ["identificacion"]
    success_url = "/"

class Borrar(generic.DeleteView):
    template_name="registro/Borrar.html"
    model=Espacio
    success_url="/"
