from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from PageObjects.BasePage import BasePage
from PageObjects.AbstractMenu import LeftBarManu


class InventoryPage(BasePage):

    def __init__(self, driver):
        url = "inventory.html"
        super().__init__(driver, url)
        self.left_bar_menu = LeftBarManu(driver, url)
        self.shopping_cart_link = (By.CSS_SELECTOR, "a[class='shopping_cart_link']")
        self.shopping_cart_badge = (By.CSS_SELECTOR, "span[class='shopping_cart_badge']")
        self.error_message_element = (By.CSS_SELECTOR, "div[class*='error'] h3[data-test='error']")

    def get_number_of_items_in_cart(self):
        try:
            self.get_text_from_element(self.shopping_cart_badge)
        except (NoSuchElementException, StaleElementReferenceException):
            return 0
        else:
            return int(self.get_text_from_element(self.shopping_cart_badge))

    def add_item_to_cart(self, item_name):
        items_in_cart = self.get_number_of_items_in_cart()
        item_locator = (By.XPATH, f"//div[@class='inventory_item']//div[contains(text(), '{item_name}')]/../../following-sibling::div/button[contains(@id, 'add-to-cart')]")
        self.click_element(item_locator)
        items_in_cart += 1
        self.wait_for_element_with_text(self.shopping_cart_badge, str(items_in_cart))

    def remove_item_from_cart(self, item_name):
        items_in_cart = self.get_number_of_items_in_cart()
        item_locator = (By.XPATH, f"//div[@class='inventory_item']//div[contains(text(), '{item_name}')]/../../following-sibling::div/button[contains(@id, 'remove')]")
        self.click_element(item_locator)
        items_in_cart -= 1
        if items_in_cart > 0:
            self.wait_for_element_with_text(self.shopping_cart_badge, str(items_in_cart))
        else:
            self.wait_for_lack_of_element(self.shopping_cart_badge)

    def open_cart(self):
        self.click_element(self.shopping_cart_link)

    def get_price_of_item(self, item):
        price_element = (By.XPATH, f"//div[@class='inventory_item']//div[contains(text(), '{item}')]/../../following-sibling::div/div[@class='inventory_item_price']")
        return float(self.get_text_from_element(price_element).lstrip('$'))


