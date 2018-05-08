import unittest
import pytest
import allure
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

        #self.driver = webdriver.Remote(
        #    command_executor='http://127.0.0.1:4444/wd/hub',
        #    desired_capabilities=DesiredCapabilities.CHROME)

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)

    @allure.story('Your Story here')
    @allure.feature('Your Feature here')
    @pytest.allure.step("Launch site")
    def test_search_SAP_in_Google(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    @pytest.allure.step("Launch site")
    def test_simple_availibility(self):
        print("test2")
        self.driver.get("https://www.sap.com/index.html")
        assert "SAP" in self.driver.title
        assert "No results found." not in self.driver.page_source

    @pytest.allure.step("Launch site")
    def test_best_practices_search(self):
        self.driver.get("https://www.sap.com/index.html")
        #element =  self.driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/div/div/div/nav/ul/li[4]/a')
        #aelement.click()



    def tearDown(self):
        self.driver.close()
        #self.driver.Quit();
        #self.driver.Dispose()

if __name__ == '__main__':
    unittest.main()