from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from Utils.helpers import WrongURL
from configuration import URL


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.full_url = URL + url
        self.wait_for_url(self.full_url)

    def wait_for_url(self, url, timeout=2, poll_frequency=0.01):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(ec.url_to_be(url))
        except TimeoutException:
            current_url = str(self.driver.current_url)
            raise WrongURL(url, current_url)

    def wait_for_element(self, element, timeout=2, poll_frequency=0.01):
        WebDriverWait(self.driver, timeout, poll_frequency).until(ec.visibility_of_element_located(element))

    def wait_for_lack_of_element(self, element, timeout=2, poll_frequency=0.01):
        WebDriverWait(self.driver, timeout, poll_frequency).until_not(ec.presence_of_element_located(element))

    def wait_for_element_with_text(self, element, text, timeout=2, poll_frequency=0.01):
        WebDriverWait(self.driver, timeout, poll_frequency).until(ec.text_to_be_present_in_element(element, text))

    def click_element(self, element):
        self.driver.find_element(*element).click()

    def set_text_to_element(self, element, text):
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(text)

    def get_text_from_element(self, element):
        return self.driver.find_element(*element).text

    def get_text_from_elements(self, locator):
        result = []
        elements = self.driver.find_elements(*locator)
        for element in elements:
            result.append(element.text)
        return result
