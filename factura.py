class Factura():

    __numero_factura = 0

    def __init__(self, cliente):
        Factura.__numero_factura += 1
        self.numero = Factura.__numero_factura
        self.__lineas = []
        self.__cliente = cliente
        self.__precio = 0

    def cliente(self):
        return self.__cliente

    def anyadir_linea(self, linea):
        self.__lineas.append(linea)
        self.__precio += linea.precio()

    def eliminar_ultima_linea(self):
        self.__precio -= self.__lineas[-1].precio()
        self.__lineas.pop()

class Linea():

    def __init__(self, producto, precio):
        self.__producto = producto
        self.__precio = precio

    def producto(self):
        return self.__producto

    def precio(self):
        return self.__precio
