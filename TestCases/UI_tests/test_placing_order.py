import pytest
import random
import itertools
from selenium.common.exceptions import TimeoutException
from PageObjects.App import App
from TestData.Users import standard_user, locked_out_user, problem_user, performance_glitch_user, fake_user
from TestData.InventoryItems import inventory_items
from TestData.Texts import *


@pytest.mark.UI
class TestPlacingOrder:

    @pytest.fixture
    def app(self, request, driver):
        app = App(driver)
        app.login_page().login(request.param.username, request.param.password)
        yield app

    # @pytest.mark.parametrize('item1, item2', list(itertools.combinations(inventory_items, 2))) # <- alternative to parametrizing one line below - it's very extensive way of testing, it checks all possible combinations of inventory items
    @pytest.mark.parametrize('item1, item2', [tuple(random.choices(inventory_items, k=2))])
    @pytest.mark.parametrize('app', [standard_user, performance_glitch_user], indirect=True)
    @pytest.mark.parametrize('driver', ["Chrome", "Firefox"], indirect=True)
    def test_placing_order_success(self, driver, app, item1, item2):
        price1 = app.inventory_page().get_price_of_item(item1)
        price2 = app.inventory_page().get_price_of_item(item2)
        app.inventory_page().add_item_to_cart(item1)
        app.inventory_page().add_item_to_cart(item2)
        app.inventory_page().open_cart()
        app.cart_page().checkout()
        app.checkout_step_one_page().set_first_name("John")
        app.checkout_step_one_page().set_last_name("Smith")
        app.checkout_step_one_page().set_postal_code("00000")
        app.checkout_step_one_page().continue_checkout()
        assert item1, item2 in app.checkout_step_two_page().get_items_names()
        assert app.checkout_step_two_page().get_quantity_of_item(item1) == 1
        assert app.checkout_step_two_page().get_quantity_of_item(item2) == 1
        assert app.checkout_step_two_page().get_price_of_item(item1) == price1
        assert app.checkout_step_two_page().get_price_of_item(item2) == price2
        assert app.checkout_step_two_page().get_total_items_price() == round(price1 + price2, 2)
        app.checkout_step_two_page().finish_checkout()
        assert order_placed_successfully in app.checkout_complete_page().get_checkout_title()

    @pytest.mark.parametrize('item1, item2', [tuple(random.choices(inventory_items, k=2))])
    @pytest.mark.parametrize('app', [standard_user, performance_glitch_user], indirect=True)
    @pytest.mark.parametrize('driver', ["Chrome", "Firefox"], indirect=True)
    def test_placing_order_fail__empty_data(self, driver, app, item1, item2):
        app.inventory_page().add_item_to_cart(item1)
        app.inventory_page().add_item_to_cart(item2)
        app.inventory_page().open_cart()
        app.cart_page().checkout()
        app.checkout_step_one_page().continue_checkout()
        assert error_lack_of_first_name in app.checkout_step_one_page().alerts.get_error_message()
        app.checkout_step_one_page().set_first_name("John")
        app.checkout_step_one_page().continue_checkout()
        assert error_lack_of_last_name in app.checkout_step_one_page().alerts.get_error_message()
        app.checkout_step_one_page().set_last_name("Smith")
        app.checkout_step_one_page().continue_checkout()
        assert error_lack_of_postal_code in app.checkout_step_one_page().alerts.get_error_message()

    @pytest.mark.parametrize('user', [locked_out_user])
    @pytest.mark.parametrize('driver', ["Chrome", "Firefox"], indirect=True)
    def test_placing_order_fail__user_is_locked(self, driver, user):
        app = App(driver)
        app.login_page().login(user.username, user.password)
        assert error_login_user_locked in app.login_page().alerts.get_error_message()

    @pytest.mark.parametrize('user', [fake_user])
    @pytest.mark.parametrize('driver', ["Chrome", "Firefox"], indirect=True)
    def test_placing_order_fail__wrong_user(self, driver, user):
        app = App(driver)
        app.login_page().login(user.username, user.password)
        assert error_login_wrong_user_or_password in app.login_page().alerts.get_error_message()

    @pytest.mark.parametrize('item1, item2, item3', [(inventory_items[0], inventory_items[1], inventory_items[4])])
    @pytest.mark.parametrize('app', [problem_user], indirect=True)
    @pytest.mark.parametrize('driver', ["Chrome", "Firefox"], indirect=True)
    def test_placing_order_fail__some_items_cannot_be_unchecked(self, driver, app, item1, item2, item3):
        app.inventory_page().add_item_to_cart(item1)
        app.inventory_page().add_item_to_cart(item2)
        app.inventory_page().add_item_to_cart(item3)
        with pytest.raises(TimeoutException):
            app.inventory_page().remove_item_from_cart(item1)
        with pytest.raises(TimeoutException):
            app.inventory_page().remove_item_from_cart(item2)
        with pytest.raises(TimeoutException):
            app.inventory_page().remove_item_from_cart(item3)

    @pytest.mark.parametrize('item1, item2, item3', [(inventory_items[2], inventory_items[3], inventory_items[5])])
    @pytest.mark.parametrize('app', [problem_user], indirect=True)
    @pytest.mark.parametrize('driver', ["Chrome", "Firefox"], indirect=True)
    def test_placing_order_fail__some_items_cannot_be_checked(self, driver, app, item1, item2, item3):
        with pytest.raises(TimeoutException):
            app.inventory_page().add_item_to_cart(item1)
        with pytest.raises(TimeoutException):
            app.inventory_page().add_item_to_cart(item2)
        with pytest.raises(TimeoutException):
            app.inventory_page().add_item_to_cart(item3)

    @pytest.mark.parametrize('item1, item2', [(inventory_items[0], inventory_items[1])])
    @pytest.mark.parametrize('app', [problem_user], indirect=True)
    @pytest.mark.parametrize('driver', ["Chrome", "Firefox"], indirect=True)
    def test_placing_order_fail__last_name_cannot_be_filled(self, driver, app, item1, item2):
        app.inventory_page().add_item_to_cart(item1)
        app.inventory_page().add_item_to_cart(item2)
        app.inventory_page().open_cart()
        app.cart_page().checkout()
        app.checkout_step_one_page().set_first_name("John")
        app.checkout_step_one_page().set_last_name("Smith")
        app.checkout_step_one_page().set_postal_code("00000")
        app.checkout_step_one_page().continue_checkout()
        assert error_lack_of_last_name in app.checkout_step_one_page().alerts.get_error_message()

