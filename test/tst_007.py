from src.functions.Functions import Functions as Selenium
import unittest
import time


class Test_007(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.mercadolibre.com.ar/")

    def test_007(self):

        #opcional
        Selenium.new_window(self, "https://www.mercadolibre.com.ar/ofertas#nav-header")

        #preferible para abrir otra tab con palabra clave
        Selenium.switch_to_windows_name(self, "Ofertas")
        time.sleep(2)

        #vuelta a main tab
        Selenium.switch_to_windows_name(self, "Principal")
        time.sleep(2)

        #vuelta a ofertas
        Selenium.switch_to_windows_name(self, "Ofertas")
        time.sleep(2)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
