# Implementar los metodos de la capa de negocio de socios.

from ejercicio_01 import Socio
from ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        buscado = self.datos.buscar_dni(dni_socio)
        if buscado is None:
            return None
        else:
            return buscado

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        #return []
        return self.datos.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_1(socio):
            if self.regla_2(socio):
                if self.regla_3():
                    try:
                        self.datos.alta(socio)
                    except:
                        return False
                    else:
                        return True

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            self.datos.baja(id_socio)
        except:
            return False
        else:
            return True

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_2(socio):
            try:
                self.datos.modificacion(socio)
            except:
                return False
            else:
                return True
        else:
            return False
            #raise

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        coso = self.datos.buscar_dni(socio.dni)
        if coso is None:
            return True
        else:
            raise DniRepetido

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if self.MAX_CARACTERES > len(socio.nombre) > self.MIN_CARACTERES:
            if self.MAX_CARACTERES > len(socio.apellido) > self.MIN_CARACTERES:
                return True
        raise LongitudInvalida

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if self.datos.contarSocios() < self.MAX_SOCIOS:
            return True
        else:
            raise MaximoAlcanzado
