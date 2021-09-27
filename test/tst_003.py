from src.functions.Functions import Functions as Selenium
import unittest
import time


class Test_003(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.google.com/")

    def test_003(self):
        # ABRIR EL JSON
        Selenium.get_json_file(self, "Google")

        # ACCEDER AL KEY DESEADO (ENTITY) DENTRO DEL JSON

        Selenium.get_elements(self, 'txt_busqueda').send_keys('Lars Ulrich')
        Selenium.get_elements(self, 'btn_buscar').click()
        time.sleep(2)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
