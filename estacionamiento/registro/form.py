from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Espacio

class RegistroUForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email'
        ]
        labels = {
        'username': 'Nickname',
        'first_name': 'Nombre',
        'last_name': 'Apellidos',
        'email': 'Correo',
        }

class CreateEspacio(forms.ModelForm):
 	class Meta:

 		model=Espacio

 		fields=['identificacion']

 		label={"identificacion":"Identificacion: ",}

 		widgets={"identificacion":forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Identificacion'})

 		}

class ModificarForm(forms.ModelForm):
	class Meta:

		model=Espacio

		fields = ["id_mat","nom_mat","id_int", "nom_int","id_vesp", "nom_vesp"]

		widgets={"id_mat":forms.TextInput(attrs={'class':'form-control','placeholder':'Matricula'}),
		"nom_mat":forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
		"id_int":forms.TextInput(attrs={'class':'form-control','placeholder':'Matricula'}),
		"nom_int":forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
		"id_vesp":forms.TextInput(attrs={'class':'form-control','placeholder':'Matricula'}),
		"nom_vesp":forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
		}

class ModificarMatForm(forms.ModelForm):
	class Meta:

		model=Espacio

		fields = ["id_mat","nom_mat"]

		widgets={"id_mat":forms.TextInput(attrs={'class':'form-control','placeholder':'Matricula'}),
		"nom_mat":forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
		}

class ModificarIntForm(forms.ModelForm):
	class Meta:

		model=Espacio

		fields = ["id_int","nom_int"]

		widgets={"id_int":forms.TextInput(attrs={'class':'form-control','placeholder':'Matricula'}),
		"nom_int":forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
		}

class ModificarVespForm(forms.ModelForm):
	class Meta:

		model=Espacio

		fields = ["id_vesp","nom_vesp"]

		widgets={"id_vesp":forms.TextInput(attrs={'class':'form-control','placeholder':'Matricula'}),
		"nom_vesp":forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
		}
