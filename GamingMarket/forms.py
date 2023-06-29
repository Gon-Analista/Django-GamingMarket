from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Producto, Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GamingMarketForm(ModelForm):

    class Meta:

        model=Producto
        fields= '__all__'

class CreacionDeUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1","password2"]
