from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage


class Alerts(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.error_message_element = (By.CSS_SELECTOR, "div[class*='error'] h3[data-test='error']")

    def get_error_message(self):
        self.wait_for_element(self.error_message_element)
        return self.get_text_from_element(self.error_message_element)


class LeftBarManu(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.open_menu_button = (By.ID, "react-burger-menu-btn")
        self.close_menu_button = (By.ID, "react-burger-cross-btn")
        self.all_items_button = (By.ID, "inventory_sidebar_link")
        self.about_button = (By.ID, "about_sidebar_link")
        self.logout_button = (By.ID, "logout_sidebar_link")
        self.reset_button = (By.ID, "reset_sidebar_link")

    def open_menu(self):
        self.click_element(self.open_menu_button)

    def close_menu(self):
        self.click_element(self.close_menu_button)

    def open_inventory(self):
        self.click_element(self.all_items_button)

    def open_about(self):
        self.click_element(self.about_button)

    def logout(self):
        self.click_element(self.logout_button)

    def reset(self):
        self.click_element(self.reset_button)
