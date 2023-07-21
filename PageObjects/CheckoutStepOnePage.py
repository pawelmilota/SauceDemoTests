from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from PageObjects.AbstractMenu import Alerts, LeftBarManu


class CheckoutStepOnePage(BasePage):

    def __init__(self, driver):
        url = "checkout-step-one.html"
        super().__init__(driver, url)
        self.alerts = Alerts(driver, url)
        self.left_bar_menu = LeftBarManu(driver, url)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.cancel_button = (By.ID, "cancel")
        self.continue_button = (By.ID, "continue")

    def set_first_name(self, first_name):
        self.set_text_to_element(self.first_name_input, first_name)

    def set_last_name(self, last_name):
        self.set_text_to_element(self.last_name_input, last_name)

    def set_postal_code(self, postal_code):
        self.set_text_to_element(self.postal_code_input, postal_code)

    def continue_checkout(self):
        self.click_element(self.continue_button)

    def cancel_checkout(self):
        self.click_element(self.cancel_button)
