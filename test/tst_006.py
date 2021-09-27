from src.functions.Functions import Functions as Selenium
import unittest
import time


class Test_006(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "http://chercher.tech/practice/frames-example-selenium-webdriver")

    def test_006(self):

        Selenium.get_json_file(self, "frames")

        Selenium.switch_to_iframe(self, "Frame2")
        Selenium.get_select_elements(self, "Frame2 Select").select_by_visible_text("Avatar")
        Selenium.switch_to_parentFrame(self)

        Selenium.switch_to_iframe(self, "Frame1")
        Selenium.send_key_text(self, "Frame1 input", "Big dogs")

        Selenium.switch_to_iframe(self, "Frame3")
        Selenium.get_elements(self, "Frame3 input").click()


        time.sleep(2)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
