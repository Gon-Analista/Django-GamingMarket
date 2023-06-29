from django.urls import path
from . import views

urlpatterns = [
    path('base', views.base, name='base'),
    path('Productos/', views.Productos, name='Productos'),
    path('Productos_editar/<int:pk>', views.Productos_editar, name='Productos_editar'),
    path('Productos_eliminar/<int:pk>', views.Productos_eliminar, name='Productos_eliminar'),
    ]