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
    fields = ["nom_mat", "nom_int", "nom_vesp"]
    success_url= "/"
