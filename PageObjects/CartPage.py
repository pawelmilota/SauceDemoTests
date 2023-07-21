from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from PageObjects.AbstractMenu import LeftBarManu


class CartPage(BasePage):

    def __init__(self, driver):
        url = "cart.html"
        super().__init__(driver, url)
        self.left_bar_menu = LeftBarManu(driver, url)
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.checkout_button = (By.ID, "checkout")

    def back_to_inventory(self):
        self.click_element(self.continue_shopping_button)

    def checkout(self):
        self.click_element(self.checkout_button)
