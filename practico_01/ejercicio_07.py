"""Slicing."""
import math

def es_palindromo(palabra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si se lee igual al
    derecho y al revés.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    if len(palabra) > 1:
        aux = round(len(palabra) / 2)
        pal = palabra[:aux]
        bra = palabra[::-1]
        bra = bra[:aux]
        if pal == bra:
            return True
        else:
            return False
    else:
        return True
    pass # Completar


# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################


def mitad(palabra: str) -> str:
    """Toma un string y devuelve la mitad. Si la longitud es impar, redondear
    hacia arriba.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    if len(palabra) > 1:
        aux = math.ceil(len(palabra) / 2)
        pal = palabra[:aux]
        return pal
    else:
        return palabra
    pass # Completar


# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
