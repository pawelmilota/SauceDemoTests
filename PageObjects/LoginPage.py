from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from PageObjects.AbstractMenu import Alerts


class LoginPage(BasePage):

    def __init__(self, driver):
        url = ""
        super().__init__(driver, url)
        self.alerts = Alerts(driver, url)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, user, password):
        self.set_text_to_element(self.username_input, user)
        self.set_text_to_element(self.password_input, password)
        self.click_element(self.login_button)
