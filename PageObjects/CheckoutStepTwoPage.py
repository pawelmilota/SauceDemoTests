import re
from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from PageObjects.AbstractMenu import LeftBarManu


class CheckoutStepTwoPage(BasePage):

    def __init__(self, driver):
        url = "checkout-step-two.html"
        super().__init__(driver, url)
        self.left_bar_menu = LeftBarManu(driver, url)
        self.cancel_button = (By.ID, "cancel")
        self.finish_button = (By.ID, "finish")
        self.items_names = (By.CSS_SELECTOR, "div[class='inventory_item_name']")
        self.subtotal_price = (By.CSS_SELECTOR, "div[class='summary_info'] div[class*='subtotal']")

    def finish_checkout(self):
        self.click_element(self.finish_button)

    def cancel_checkout(self):
        self.click_element(self.cancel_button)

    def get_items_names(self):
        return self.get_text_from_elements(self.items_names)

    def get_quantity_of_item(self, item):
        quantity_locator = (By.XPATH, f"//div[@class='inventory_item_name' and contains(text(), '{item}')]/../../preceding-sibling::div")
        return int(self.get_text_from_element(quantity_locator))

    def get_price_of_item(self, item):
        price_locator = (By.XPATH, f"//div[@class='inventory_item_name' and contains(text(), '{item}')]/../following-sibling::div/div[@class='inventory_item_price']")
        return float(self.get_text_from_element(price_locator).lstrip('$'))

    def get_total_items_price(self):
        result_tmp = self.get_text_from_element(self.subtotal_price)
        result = round(float(re.sub("[^0-9.]", "", result_tmp, 0)), 2)
        return result
