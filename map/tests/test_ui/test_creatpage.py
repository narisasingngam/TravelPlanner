from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class CreatePageDisplayTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)
        cls.browser.get('https://travelplanner-app.herokuapp.com/#/planner/new')

    def test_createplan_topic_displayed(self):
        topic = self.browser.find_element(By.XPATH, '//*[@id="topic"]')
        self.assertTrue(topic.is_displayed())

    def test_createplan_btn_displayed(self):
        create_btn = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/form/div[4]/div/button')
        self.assertTrue(create_btn.is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()


if __name__ == "__main__":
    unittest.main()
