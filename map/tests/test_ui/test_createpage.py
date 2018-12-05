from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import os


class CreatePageDisplayTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER = os.path.join(PROJECT_ROOT, "chromedriver")
        cls.browser = webdriver.Chrome(executable_path=DRIVER)
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
