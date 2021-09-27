# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest


class Test_012(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.mercadolibre.com.ar/registration")
        Selenium.get_json_file(self, "mercadolibre_ar")

    def test_012(self):
        Selenium.save_variable_scenary(self, "DNI", "DNI") # Texto vacio
        Selenium.save_variable_scenary(self, "titulo", "titulo")

        Selenium.new_window(self, "https://www.google.com/")
        Selenium.get_json_file(self, "Google")
        Selenium.switch_to_windows_name(self, "Google")

        texto = Selenium.get_variable_scenary(self, "titulo")
        Selenium.get_elements(self, "txt_busqueda").send_keys(texto)
        Selenium.esperar(3)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
