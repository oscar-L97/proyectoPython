from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Espacio
from django.views import generic
from .form import CreateEspacio, ModificarForm, ModificarMatForm,ModificarIntForm,ModificarVespForm, RegistroUForm

# Create your views here.

class RegistroUForm(generic.CreateView):
    model = User
    template_name = "registro.html"
    form_class = RegistroUForm
    success_url = "/"

class IndexList(generic.ListView):
    template_name="registro/IndexList.html"
    model = Espacio

class ListMat(generic.ListView):
    template_name="registro/ListMat.html"
    model = Espacio

class ListInt(generic.ListView):
    template_name="registro/ListInt.html"
    model = Espacio

class ListVesp(generic.ListView):
    template_name="registro/ListVesp.html"
    model = Espacio

class Modificar(generic.UpdateView):
    template_name="registro/Modificar.html"
    model = Espacio
    #fields = ["id_mat","nom_mat","id_int", "nom_int","id_vesp", "nom_vesp"]
    form_class=ModificarForm
    success_url= "/"

class Mod_Mat(generic.UpdateView):
    template_name="registro/Mod_Mat.html"
    model = Espacio
    form_class=ModificarMatForm
    #fields = ["id_mat","nom_mat"]
    success_url = "/list_mat/"

class Mod_Int(generic.UpdateView):
    template_name="registro/Mod_Int.html"
    model = Espacio
    form_class=ModificarIntForm
    #fields = ["id_int","nom_int"]
    success_url = "/list_int/"

class Mod_Vesp(generic.UpdateView):
    template_name="registro/Mod_Vesp.html"
    model = Espacio
    #fields = ["id_vesp","nom_vesp"]
    form_class=ModificarVespForm
    success_url = "/list_vesp/"

class Crear(generic.CreateView):
    template_name="registro/Crear.html"
    model = Espacio
    form_class=CreateEspacio
    #fields = ["identificacion"]
    success_url = "/"

class Crear_mat(generic.CreateView):
    template_name="registro/Crear.html"
    model = Espacio
    form_class=CreateEspacio
    #fields = ["identificacion"]
    success_url = "/list_mat/"

class Crear_int(generic.CreateView):
    template_name="registro/Crear.html"
    model = Espacio
    form_class=CreateEspacio
    #fields = ["identificacion"]
    success_url = "/list_int/"

class Crear_vesp(generic.CreateView):
    template_name="registro/Crear.html"
    model = Espacio
    form_class=CreateEspacio
    #fields = ["identificacion"]
    success_url = "/list_vesp/"

class Borrar(generic.DeleteView):
    template_name="registro/Borrar.html"
    model=Espacio
    success_url="/"
