from cliente import Cliente
from articulo import Articulo
from factura import Factura

cliente1 = Cliente("12345678A", "Rosa", "Gonzalez")
televisor = Articulo(0, "Televisor Sumsang", 399)
tgrafica = Articulo(1, "Tarjeta Grafica Envidia", 239)
factura1 = Factura(cliente1)
factura1.anyadir_linea(televisor, 2)
factura1.anyadir_linea(televisor, 1)
factura1.eliminar_ultima_linea()
factura1.anyadir_linea(tgrafica, 1)
factura1.imprimir_factura()
