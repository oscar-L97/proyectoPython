from django.urls import path
from registro.api import views

app_name="api_registro"

urlpatterns = [
    path('list_registro/', views.ListRegistroAPIView.as_view(), name ="listAPIView"),
]
