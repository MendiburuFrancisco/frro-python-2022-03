"""Propiedades"""


class Auto:
    """La clase auto tiene dos propiedades, precio y marca. La marca se define
    obligatoriamente al construir la clase y siempre que se devuelve, se 
    devuelve con la primer letra en mayúscula y no se puede modificar. El precio
    puede modificarse pero cuando se muestra, se redondea a 2 decimales
    
    Restricción: Usar Properties
    
    Referencia: https://docs.python.org/3/library/functions.html#property"""
    def __init__(self, marca, precio):
        self._precio = precio
        self._nombre = marca

    def getprecio(self):
        return round(self._precio, 2)

    def setprecio(self, v):
        self._precio = v

    def getnombre(self):
        return self._nombre[0].upper() + self._nombre[1:]

    nombre = property(getnombre)
    precio = property(getprecio, setprecio)

    # Completar


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)

print(auto.nombre)
assert auto.nombre == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Auto:
    _nombre: str = ""
    _precio: float = 0

    def getprecio(self):
        return round(self._precio, 2)

    def setprecio(self, v):
        self._precio = v

    def getnombre(self):
        return self._nombre[0].upper() + self._nombre[1:]

    nombre = property(getnombre)
    precio = property(getprecio, setprecio)
    """Re-Escribir utilizando DataClasses"""

    # Completar


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)

assert auto.nombre == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN
