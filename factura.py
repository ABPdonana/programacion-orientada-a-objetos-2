from articulo import Articulo

class Factura():

    __numero_factura = 0

    def __init__(self, cliente):
        Factura.__numero_factura += 1
        self.numero = Factura.__numero_factura
        self.__lineas = []
        self.__cliente = cliente

    def cliente(self):
        return self.__cliente

    def anyadir_linea(self, articulo, cantidad):
        self.__lineas.append([articulo, cantidad])

    def __precio(self):
        self.__precio = 0
        for i in self.__lineas:
            self.__precio = i[0].precio() * i[1]
        return self.__precio

    def eliminar_ultima_linea(self):
        self.__precio -= self.__lineas[-1].precio()
        self.__lineas.pop()

    def imprimir_factura(self):
        for i in self.__lineas:
            print(f'{i[1]} {i[0].denominacion()}')
        print(self.__precio())
