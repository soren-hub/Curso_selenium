import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



executable_path = r'D:/conda/envs/curso_selenium/chromedriver/chromedriver.exe'
location = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

class HelloWorld(unittest.TestCase):

    @classmethod  # para que abra las pestañas en una misma ventana
    def setUpClass(cls):
        options = Options()
        options.binary_location = location
        cls.driver = webdriver.Chrome(executable_path=executable_path , options=options)
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        """
        modulo de prueba, debe tener test para que sea reconocido 
        por test runner 
        - Aca se escribiran las acciones para autimatizar.
        """

        self.driver.get('https://platzi.com/')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.getonbrd.com/')

    @classmethod  # decorador para que no se cierre la ventana después de la primera prueba
    def tearDownClass(cls):
        # cierra el navegador para evitar consumo de recursos
        cls.driver.quit()


if __name__ == "__main__":
    # validacion del metodo main
    # test runner genera los reportes correspondientes
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output="reportes", report_name="hello-world-report"))
