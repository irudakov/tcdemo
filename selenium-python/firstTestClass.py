import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        self.driver.get("http://www.google.com")
        input_element = self.driver.find_element_by_name("q")
        input_element.send_keys("SAP")
        input_element.submit()

        RESULTS_LOCATOR = '//*[@id="rhs_block"]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div/div[1]/span[1]'

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))

        page1_results = self.driver.find_elements(By.XPATH, RESULTS_LOCATOR)

        for item in page1_results:
            print(item.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()