from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest


class HomePageViewRedirectTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Safari()
        cls.browser.get('http://travelplanner-app.herokuapp.com/#/')

    def test_view_planners_redirect(self):
        view_planners = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/nav/div/div[3]/a[1]')
        get_view_url = view_planners.get_attribute("href")
        self.assertEqual('http://travelplanner-app.herokuapp.com/#/planners', get_view_url)

    def test_create_planner_redirect(self):
        create_plan = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/nav/div/div[3]/a[2]')
        get_create_url = create_plan.get_attribute('href')
        self.assertEqual('http://travelplanner-app.herokuapp.com/#/planner/new', get_create_url)

    def test_log_in_redirect(self):
        log_in = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/nav/div/div[3]/a[3]')
        get_login_url = log_in.get_attribute('href')
        self.assertEqual('http://travelplanner-app.herokuapp.com/#/account', get_login_url)

    def test_explore_plans_redirect(self):
        explore_plans = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div[1]/a')
        get_explore_url = explore_plans.get_attribute('href')
        self.assertEqual('http://travelplanner-app.herokuapp.com/#/planners', get_explore_url)

    def test_organize_plan(self):
        organize_plan = self.browser.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div[2]/a')
        get_organize_url = organize_plan.get_attribute('href')
        self.assertEqual('http://travelplanner-app.herokuapp.com/#/planner/new', get_organize_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()


if __name__ == "__main__":
    unittest.main()
