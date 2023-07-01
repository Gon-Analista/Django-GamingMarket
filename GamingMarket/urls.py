from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('registro', views.Registro, name='registro'),
    path('Gameboy_Advance', views.Gameboy_Advance, name='Gameboy_Advance'),
    path('Nintendo_64', views.Nintendo_64, name='Nintendo_64'),
    path('Ps1', views.Ps1, name='PS1'),
    path('Ps2', views.Ps2, name='PS2'),
    path('Super_Nintendo', views.Super_Nintendo, name='Super_Nintendo'),
    path('carrito', views.carrito_html, name='carrito'),
    path('agregar/<int:producto_id>', views.agregar_producto, name='Add'),
    path('eliminar/<int:pedido_id>', views.pedido_eliminar, name='pedido_eliminar'),
    path('sumar_producto/<int:producto_id>', views.sumar_producto, name='sumar'),
    path('forma_pago', views.forma_pago, name='forma_pago'),
    path('finalizar_pago', views.finalizar_pago, name='finalizar_pago'),

]
