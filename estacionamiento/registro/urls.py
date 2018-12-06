from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import views as auth_views
from registro import views

app_name="registro"

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name="login_view"),
    path('logout/', logout_then_login, name = "logout"),
    path('',login_required(views.IndexList.as_view()), name="index_list"),
    path('modificar/<int:pk>', login_required(views.Modificar.as_view()), name="modificar"),
    path('crear/', login_required(views.Crear.as_view()), name="crear"),
    path('crear_mat/', login_required(views.Crear_mat.as_view()), name="crear_mat"),
    path('crear_int/', login_required(views.Crear_int.as_view()), name="crear_int"),
    path('crear_vesp/', login_required(views.Crear_vesp.as_view()), name="crear_vesp"),
    path('borrar/<int:pk>', login_required(views.Borrar.as_view()), name="borrar"),
    path('list_mat/',login_required(views.ListMat.as_view()), name="list_mat"),
    path('list_int/',login_required(views.ListInt.as_view()), name="list_int"),
    path('list_vesp/',login_required(views.ListVesp.as_view()), name="list_vesp"),
    path('mod_mat/<int:pk>', login_required(views.Mod_Mat.as_view()), name="mod_mat"),
    path('mod_int/<int:pk>', login_required(views.Mod_Int.as_view()), name="mod_int"),
    path('mod_vesp/<int:pk>', login_required(views.Mod_Vesp.as_view()), name="mod_vesp")

]
