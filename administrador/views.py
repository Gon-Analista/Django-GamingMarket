from django.shortcuts import render
from GamingMarket.models import Producto,Pedido
from GamingMarket.forms import GamingMarketForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def base(request):
    context={}
    return render(request,'administrador/base.html',context)

@login_required
def Productos(request):
    productos = Producto.objects.all().order_by('stock_producto')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 8)
        productos = paginator.page(page)
    except:
        raise Http404

    context={
        'form': GamingMarketForm(),
        'entity' : productos,
        'paginator': paginator,
        }
    if request.method=='POST':
        formulario=GamingMarketForm(request.POST, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'El producto se ha guardado correctamente!')
            return redirect('Productos')
    return render(request,'administrador/Productos.html',context)

@login_required
def Productos_editar(request, pk):
    productos = Producto.objects.filter(id_producto=pk)
    context = {
        'form': GamingMarketForm(instance=productos.first()),
        'entity': productos,
    }
    if request.method == 'POST':
        formulario = GamingMarketForm(request.POST, files=request.FILES, instance=productos.first())
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'El producto se ha actualizado correctamente.')
            return redirect('Productos')
    return render(request, 'administrador/Productos_editar.html', context)

@login_required
def Productos_eliminar(request, pk):
    productos = Producto.objects.filter(id_producto=pk)
    productos.delete()
    return redirect(to='Productos')
