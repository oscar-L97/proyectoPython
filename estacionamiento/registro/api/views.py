from rest_framework import generics
from registro.api.serializers import RegistroModelSerializer
from registro.models import Espacio

class ListRegistroAPIView(generics.ListAPIView):
    serializer_class = RegistroModelSerializer

    def get_queryset(self, *args, **kwargs):
        return Espacio.objects.all()
