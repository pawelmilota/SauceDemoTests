import pytest
from configuration import URL
from Utils.helpers import install_webdriver


@pytest.fixture()
def driver(request):
    driver = install_webdriver(request.param)
    driver.get(URL)
    yield driver
    driver.quit()
