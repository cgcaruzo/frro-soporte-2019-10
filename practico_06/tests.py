# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, MaximoAlcanzado, DniRepetido


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
        socio1 = Socio(dni=22222222, nombre='Juan', apellido='Perez')
        self.ns.alta(socio1)
        socio2 = Socio(dni=22222222, nombre='Roberto', apellido='Sanchez')

        exito = self.ns.regla_1(socio2)
        self.assertTrue(exito)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juanrobertojosematiasermenegildo', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perezgomezbolanosdiaz')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        socio = Socio(dni=12345677, nombre="Roberto", apellido="Sanchez")
        self.ns.alta(socio)
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3())

    def test_baja(self):

        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        exito = self.ns.baja(socio.id)

        self.assertTrue(exito)

    def test_buscar(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        buscado = self.ns.buscar(socio.id)
        self.assertEqual(socio, buscado)

    def test_buscar_dni(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        buscado = self.ns.buscar_dni(socio.dni)
        self.assertEqual(socio, buscado)

    def test_todos(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        self.assertTrue(self.ns.todos() != None)

    def test_modificacion(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        socio.dni = 87654321
        socio.roberto = "Roberto"
        socio.apellido = "Sanchez"
        exito = self.ns.modificacion(socio)

        self.assertTrue(exito)
