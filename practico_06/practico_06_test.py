# Implementar los casos de prueba descritos.

import unittest

from ejercicio_01 import Socio
from capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.alta(valido))

        # dni repetido
        invalido = Socio(dni=12345678, nombre='Manuel', apellido='Messi')
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)
        pass

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)
        pass

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='JuanPerezManuelMessi', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)
        pass

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Joe')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)
        pass

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='JuanPerezManuelMessi')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)
        pass

    def test_regla_3(self):
        # valida regla
        socio_1 = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_3())
        socio_2 = Socio(dni=23456789, nombre='Manuel', apellido='Messi')
        self.assertTrue(self.ns.regla_3())

        # Cargo MAX_SOCIOS socios (para testear modifique el numero a 2)
        self.assertTrue(self.ns.alta(socio_1))
        self.assertTrue(self.ns.alta(socio_2))

        # Intengo cargar
        invalido = Socio(dni=12334567, nombre='Juan', apellido='Rupi')
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)
        self.assertRaises(MaximoAlcanzado, self.ns.alta, invalido)
        pass

    def test_baja(self):
        # pre-condiciones: Un socio registrado
        self.assertEqual(len(self.ns.todos()), 0)
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.alta(socio))

        # Logica borrar
        self.assertTrue(self.ns.baja(1))

        # post-condiciones: ningun socio registrado
        self.assertEqual(len(self.ns.todos()), 0)
        pass

    def test_buscar(self):
        # pre-condiciones: Un socio registrado
        self.assertEqual(len(self.ns.todos()), 0)
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.alta(socio))

        # Logica buscar
        self.assertIsNotNone(self.ns.buscar(1))
        self.assertIsNone(self.ns.buscar(2))
        pass

    def test_buscar_dni(self):
        # pre-condiciones: Un socio registrado
        self.assertEqual(len(self.ns.todos()), 0)
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.alta(socio))

        # Logica buscar
        self.assertIsNotNone(self.ns.buscar_dni(12345678))
        self.assertIsNone(self.ns.buscar_dni(99999999))
        pass

    def test_todos(self):
        # pre-condiciones: Dos socios registrados
        self.assertEqual(len(self.ns.todos()), 0)
        socio_1 = Socio(dni=11111111, nombre='Juan', apellido='Perez')
        socio_2 = Socio(dni=22222222, nombre='Manuel', apellido='Messi')
        self.assertTrue(self.ns.alta(socio_1))
        self.assertTrue(self.ns.alta(socio_2))

        # Logica buscar
        self.assertIsInstance(self.ns.todos(), list)

        pass

    def test_modificacion(self):
        # pre-condiciones: Un socio registrado
        self.assertEqual(len(self.ns.todos()), 0)
        socio = Socio(dni=11111111, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.alta(socio))

        # Logica Modificar
        modificar = Socio(id_socio=1, dni=22222222, nombre='Manuel', apellido='Messi')
        self.assertTrue(self.ns.modificacion, modificar)

        pass
