from classVenta import Venta

venta = Venta()

venta.set_id_venta(1)
venta.set_fecha("15/10/2024")
venta.set_cliente("Michelle")

# Diccionario de productos con cantidad y precio unitario
productos = {
    "Producto A": {"cantidad": 2, "precio": 50.25},
    "Producto B": {"cantidad": 1, "precio": 30.00},
    "Producto C": {"cantidad": 3, "precio": 10.00}
}

venta.set_productos(productos)

# Muestra el detalle de la venta
venta.mostrar_detalle()
