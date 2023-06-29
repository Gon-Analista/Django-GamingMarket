from django.db import models

# Create your models here.


class Producto(models.Model):
    PLATAFORMA_CHOICES = [
        ('Super_Nintendo', 'Super Nintendo'),
        ('Gameboy_Advance', 'Gameboy Advance'),
        ('Nintendo_64', 'Nintendo 64'),
        ('PS1', 'PS1'),
        ('PS2', 'PS2'),
    ]
    ESTADO_CHOICES = [
        ('Juego Nuevo', 'Juego Nuevo'),
        ('Ya en catalogo', 'Ya en catalogo'),
    ]
    
    id_producto = models.AutoField(db_column='idProducto', primary_key=True) 
    nombre_producto = models.CharField(max_length=30,  null=False)
    precio_producto = models.IntegerField(blank=False, null=False)
    genero_producto = models.CharField(max_length=20, null=False)
    stock_producto = models.IntegerField(null=False)
    plataforma_producto = models.CharField(max_length=20, choices=PLATAFORMA_CHOICES, null=False)
    novedad_producto = models.CharField(max_length=20, choices=ESTADO_CHOICES, null=False)
    imagen_producto = models.ImageField(upload_to="Producto", null=True)
    
    def __str__(self):
        return f"{self.nombre_producto} | Stock: {self.stock_producto}"


class Pedido(models.Model):
    id_pedido           = models.AutoField(db_column='idPedido', primary_key=True) 
    id_cliente          = models.ForeignKey('Cliente',on_delete=models.CASCADE, db_column='id_cliente')
    id_producto         = models.ForeignKey('Producto',on_delete=models.CASCADE, db_column='id_producto')
    fecha_pedido        = models.DateField(null=False) 
    estado_pedido       = models.CharField(max_length=20, null=False)
    cantidad_producto   = models.IntegerField(null=False)
    
    def __str__(self):
        return "Usuario: "+str(self.id_cliente)+" | Producto: "+str(self.id_producto.nombre_producto)+" | Cantidad: "+str(self.cantidad_producto)

class Cliente(models.Model):
    id_cliente         = models.AutoField(db_column='idCliente', primary_key=True) 
    nombre_usuario     = models.CharField(max_length=20, blank=False, null=False)
    alias_usuario      = models.CharField(max_length=20, blank=False, null=False)
    email              = models.EmailField(unique=True, max_length=100, blank=False, null=False)
    celular            = models.CharField(max_length=45, blank=True, null=True)
    direccion          = models.CharField(max_length=50, blank=False, null=False)
    activo             = models.IntegerField()

    def __str__(self):
        return str(self.alias_usuario)  