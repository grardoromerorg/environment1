# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium, Scenario
import unittest


class Test_016(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.mercadolibre.com.ar/registration")
        Selenium.get_json_file(self, "mercadolibre_ar")

    def test_016(self):
        path = Selenium.create_path(self)
        Selenium.capturar_pantalla(self)
        print(path)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
