from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class WrongWebdriverException(Exception):
    def __init__(self, driver_name):
        self.driver_name = driver_name
        self.message = f"The webdriver is wrongly passed, there is no webdriver with name <{driver_name}> defined."
        super().__init__(self.message)


class WrongURL(Exception):
    def __init__(self, url, current_url):
        self.url = url
        self.message = f"The current URL is <{current_url}> and it differs from <{url}> which was expected."
        super().__init__(self.message)


def install_webdriver(driver_name):
    if driver_name == 'Chrome':
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif driver_name == 'Firefox':
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise WrongWebdriverException(driver_name)
