from src.functions.Functions import Functions as Selenium
from src.pages.create_google_acct import Register
import unittest
import time


class Test_002(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_002(self):
        assert Selenium.xpath_element(self, Register.lbl_title_xpath).text == "Create your Google Account"
        Selenium.xpath_element(self, Register.txt_name_xpath).send_keys('Gerardo')
        Selenium.xpath_element(self, Register.txt_lastname_xpath).send_keys('Romero')
        Selenium._name_element(self, Register.txt_password_name).send_keys('gegegege')
        Selenium._xpath_element(self, Register.btn_next_xpath).click()
        time.sleep(2)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
