"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union
import functools


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    listaNumeros = []
    listaStr = []
    for elemento in lista:
        if type(elemento) == str:
            listaStr.append(elemento)
        else:
            listaNumeros.append(elemento)
    return listaStr + listaNumeros
    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    listaNumeros = [x for x in lista if type(x) == int]
    listaStr = [x for x in lista if type(x) == str]
    return listaStr + listaNumeros
    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    def funcion_comparativa(a, b):
        if type(a) == type(b):
            return 0
        elif type(a) == int and type(b) == str:
            return 1
        else:
            return -1

    return sorted(lista, key=functools.cmp_to_key(funcion_comparativa))
    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    def fun_comparativa(a):
        return type(a) == str

    def fun_com_int(a):
        return type(a) == int

    listar = [x for x in filter(fun_comparativa, lista)]
    listar = listar + [x for x in filter(fun_com_int, lista)]
    print(listar)
    return listar
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
