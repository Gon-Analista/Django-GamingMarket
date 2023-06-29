from django.shortcuts import render
from .models import Producto, Cliente, Pedido
from .forms import  CreacionDeUsuario
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

# Create your views here.

class CustomLoginView(LoginView):
    def get_success_url(self):
        if self.request.user.is_staff:
            return '/administrador/base'  # Redirige a la URL de administrador para el staff
        else:
            return '/GamingMarket/index'  # Redirige al índice de la página principal para otros usuarios

def index(request):
    productos = Producto.objects.all() #es lo mismo que hacer un 'Select * From Productos'
    context={
        'productos' : productos,
    }
    return render(request,'GamingMarket/index.html',context)


def Super_Nintendo(request):
    productos = Producto.objects.all() #es lo mismo que hacer un 'Select * From Productos'
    context={
        'productos' : productos,
    }
    return render(request,'GamingMarket/Super_Nintendo.html',context)

def Gameboy_Advance(request):
    productos = Producto.objects.all() #es lo mismo que hacer un 'Select * From Productos'
    context={
        'productos' : productos,
    }
    return render(request,'GamingMarket/Gameboy_Advance.html',context)

def Nintendo_64(request):
    productos = Producto.objects.all() #es lo mismo que hacer un 'Select * From Productos'
    context={
        'productos' : productos,
    }
    return render(request,'GamingMarket/Nintendo_64.html',context)

def Ps1(request):
    productos = Producto.objects.all() #es lo mismo que hacer un 'Select * From Productos'
    context={
        'productos' : productos,
    }
    return render(request,'GamingMarket/Ps1.html',context)

def Ps2(request):
    productos = Producto.objects.all() #es lo mismo que hacer un 'Select * From Productos'
    context={
        'productos' : productos,
    }
    return render(request,'GamingMarket/Ps2.html',context)


def Registro(request):
    data={
        'form': CreacionDeUsuario()
    }

    if request.method == 'POST':
        formulario = CreacionDeUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, 'Te has registrado correctamente!')
            return redirect('index')
        data["form"] = formulario
    
    return render(request,'registration/registro.html',data)

