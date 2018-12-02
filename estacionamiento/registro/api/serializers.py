from rest_framework import serializers
from registro.models import Espacio

class RegistroModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espacio
        fields =[
            "id",
            "identificacion",
            "id_mat",
            "nom_mat",
            "id_int",
            "nom_int",
            "id_vesp",
            "nom_vesp",
        ]
