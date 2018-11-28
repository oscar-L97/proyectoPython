from django.contrib import admin
from django.urls import path

from registro import views

app_name="registro"

urlpatterns = [
    path('',views.IndexList.as_view(), name="index_list"),
    path('modificar/<int:pk>', views.Modificar.as_view(), name="modificar"),
    path('crear/', views.Crear.as_view(), name="crear"),
    path('borrar/<int:pk>', views.Borrar.as_view(), name="borrar"),
    path('list_mat/',views.ListMat.as_view(), name="list_mat"),
    path('list_int/',views.ListInt.as_view(), name="list_int"),
    path('list_vesp/',views.ListVesp.as_view(), name="list_vesp"),

]
