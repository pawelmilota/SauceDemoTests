from PageObjects.LoginPage import LoginPage
from PageObjects.InventoryPage import InventoryPage
from PageObjects.CartPage import CartPage
from PageObjects.CheckoutStepOnePage import CheckoutStepOnePage
from PageObjects.CheckoutStepTwoPage import CheckoutStepTwoPage
from PageObjects.CheckoutCompletePage import CheckoutCompletePage


class App:

    def __init__(self, driver):
        self.driver = driver

    def login_page(self):
        return LoginPage(self.driver)

    def inventory_page(self):
        return InventoryPage(self.driver)

    def cart_page(self):
        return CartPage(self.driver)

    def checkout_step_one_page(self):
        return CheckoutStepOnePage(self.driver)

    def checkout_step_two_page(self):
        return CheckoutStepTwoPage(self.driver)

    def checkout_complete_page(self):
        return CheckoutCompletePage(self.driver)
