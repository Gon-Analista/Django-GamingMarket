from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('registro', views.Registro, name='registro'),
    path('Gameboy_Advance', views.Gameboy_Advance, name='Gameboy_Advance'),
    path('Nintendo_64', views.Nintendo_64, name='Nintendo_64'),
    path('Ps1', views.Ps1, name='Ps1'),
    path('Ps2', views.Ps2, name='Ps2'),
    path('Super_Nintendo', views.Super_Nintendo, name='Super_Nintendo'),

]