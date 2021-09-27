from src.functions.Functions import Functions as Selenium
import unittest
import time


class Test_008(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.amazon.es/")

    def test_008(self):
        Selenium.get_json_file(self, "amazon")
        Selenium.scroll_to(self, "Sobre Amazon")
        Selenium.esperar(3)
        Selenium.js_clic(self, "Sobre Amazon")

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
