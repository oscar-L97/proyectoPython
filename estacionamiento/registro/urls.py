from django.contrib import admin
from django.urls import path

from registro import views

app_name="registro"

urlpatterns = [
    path('',views.IndexList.as_view(), name="index_list"),
    path('modificar/<int:pk>', views.Modificar.as_view(), name="modificar"),
    path('crear/', views.Crear.as_view(), name="crear"),
    path('crear_mat/', views.Crear_mat.as_view(), name="crear_mat"),
    path('crear_int/', views.Crear_int.as_view(), name="crear_int"),
    path('crear_vesp/', views.Crear_vesp.as_view(), name="crear_vesp"),
    path('borrar/<int:pk>', views.Borrar.as_view(), name="borrar"),
    path('list_mat/',views.ListMat.as_view(), name="list_mat"),
    path('list_int/',views.ListInt.as_view(), name="list_int"),
    path('list_vesp/',views.ListVesp.as_view(), name="list_vesp"),
    path('mod_mat/<int:pk>', views.Mod_Mat.as_view(), name="mod_mat"),
    path('mod_int/<int:pk>', views.Mod_Int.as_view(), name="mod_int"),
    path('mod_vesp/<int:pk>', views.Mod_Vesp.as_view(), name="mod_vesp")

]
