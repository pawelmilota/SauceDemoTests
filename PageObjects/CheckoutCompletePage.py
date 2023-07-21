from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from PageObjects.AbstractMenu import LeftBarManu


class CheckoutCompletePage(BasePage):

    def __init__(self, driver):
        url = "checkout-complete.html"
        super().__init__(driver, url)
        self.left_bar_menu = LeftBarManu(driver, url)
        self.back_to_inventory_button = (By.ID, "back-to-products")
        self.checkout_title = (By.CSS_SELECTOR, "#checkout_complete_container h2[class*='complete']")

    def back_to_inventory(self):
        self.click_element(self.back_to_inventory_button)

    def get_checkout_title(self):
        return self.get_text_from_element(self.checkout_title)
