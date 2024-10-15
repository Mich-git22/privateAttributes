class Venta:
    __id_venta = None
    __fecha = None
    __cliente = None
    __productos = None  # Diccionario de productos vendidos
    __total = 0.0

    # Getters para acceder a los atributos privados
    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    # Setters para modificar los atributos privados
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_productos(self, productos):
        # Validar que solo se puedan agregar los productos permitidos (A, B, C)
        self.__productos = {}
        for producto, detalles in productos.items():
            if producto in ["Producto A", "Producto B", "Producto C"]:
                self.__productos[producto] = detalles
            else:
                print(
                    f"El producto {producto} no está permitido. Solo se permiten Producto A, Producto B y Producto C.")

        # Calcular el total basado en el precio unitario y la cantidad
        self.__total = sum(detalles['cantidad'] * detalles['precio'] for detalles in self.__productos.values())

    def set_total(self, total):
        self.__total = total

    # Método para mostrar los detalles de la venta
    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print("Productos:")

        # Mostrar detalles de cada producto y su total
        for producto, detalles in self.__productos.items():
            total_producto = detalles['cantidad'] * detalles['precio']
            print(
                f"- {producto}: Cantidad: {detalles['cantidad']}, Precio unitario: {detalles['precio']:.2f}, Total: {total_producto:.2f}")

        # Mostrar el total general de la venta
        print(f"Total de la venta: ${self.__total:.2f}")
