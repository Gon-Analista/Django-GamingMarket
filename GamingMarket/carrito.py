from GamingMarket.models import Producto, Pedido
import datetime


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito


    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True


    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def agregar(self, producto):
        
        id = str(producto.id_producto)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "id_producto": producto.id_producto,
                "nombre": producto.nombre_producto,
                "acomulado": producto.precio_producto,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acomulado"] += producto.precio_producto
        self.guardar_carrito()

    

    def crear_pedido(self, cliente):
        for item in self.carrito.values():
            pedido = Pedido(
                id_cliente=cliente,
                id_producto=Producto.objects.get(id_producto=item["id_producto"]),
                fecha_pedido=datetime.date.today(),
                estado_pedido="Pendiente",
                cantidad_producto=item["cantidad"],
            )
            pedido.save()
        self.limpiar()


        