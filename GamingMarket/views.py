from django.shortcuts import render
from .models import Producto, Pedido
from .forms import  CreacionDeUsuario
from GamingMarket.carrito import Carrito
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404



class CustomLoginView(LoginView):
    def get_success_url(self):
        if self.request.user.is_staff:
            messages.success(self.request, 'Has ingresado correctamente!')
            return '/administrador/base'  # Redirige a la URL de administrador para el staff
        else:
            messages.success(self.request, 'Has ingresado correctamente!')
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

@login_required
def carrito_html(request):
    carrito = Carrito(request)
    pedidos = Pedido.objects.filter(id_cliente=request.user)
    total_carrito = sum(pedido.id_producto.precio_producto * pedido.cantidad_producto for pedido in pedidos)
    context = {
        'pedidos': pedidos,
        'total_carrito': total_carrito,
    }
    return render(request, 'GamingMarket/carrito.html', context)

@login_required
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.agregar(producto)
    carrito.crear_pedido(request.user)
    plataforma = producto.plataforma_producto
    return redirect(plataforma)

@login_required
def sumar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.agregar(producto)
    carrito.crear_pedido(request.user)
    plataforma = producto.plataforma_producto
    return redirect('carrito')



def pedido_eliminar(request, pedido_id):
    pedido = Pedido.objects.filter(id_pedido=pedido_id)
    pedido.delete()
    return redirect(to='carrito')


@login_required
def forma_pago(request):
    return render(request, 'GamingMarket/forma_pago.html')



def finalizar_pago(request):
    messages.success(request, 'Su compra se ha realizado correctamente.')
    Pedido.objects.all().delete()
    return redirect(to='index') 
