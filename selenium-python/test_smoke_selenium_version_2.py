import unittest
import pytest
import allure
#from allure.constants import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




class SeleniumPythonDemoClass(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        #self.driver = webdriver.Remote(
        #    command_executor='http://127.0.0.1:4444/wd/hub',
        #    desired_capabilities=DesiredCapabilities.FIREFOX)

    @allure.story('Your Story here')
    @allure.feature('Your Feature here')
    @pytest.allure.step("Launch site")
    @allure.step('some operation')

    def test_search_SAP_in_Google(self):

        driver = self.driver
        driver.get("http://imsabap:1080/abapwiki ")
        self.assertIn("Welcome", driver.title)


    @pytest.allure.step("Launch site")
    def test_simple_availibility(self):
        driver = self.driver
        driver.get("http://imsabap:1080/abapwiki ")
        self.assertIn("Welcome", driver.title)

    @pytest.allure.step("Launch site")
    def test_best_practices_search(self):
        driver = self.driver
        driver.get("http://imsabap:1080/abapwiki ")
        self.assertIn("Welcome", driver.title)


    def tearDown(self):
        #self.driver.close()
        self.driver.quit()
        #self.driver.Dispose()



if __name__ == '__main__':
    unittest.main()