class Articulo():
    def __init__(self, codigo, denominacion, precio):
        self.__codigo = codigo
        self.__denominacion = denominacion
        self.__precio = precio

    def codigo(self):
        return self.__codigo

    def denominacion(self):
        return self.__denominacion

    def precio(self):
        return self.__precio
