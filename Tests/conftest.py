import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os


# CLASS-BASED DRIVER FIXTURE
# Attaches driver to test class using request.cls.driver
# Used when tests inherit from BaseTest and access self.driver
@pytest.fixture(params=["chrome", "firefox", "edge"], scope='function')
def init_driver(request):

    if request.param == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service)
    elif request.param == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=service)
    elif request.param == 'edge':
        driver_path = os.path.abspath("Drivers/msedgedriver")
        service = EdgeService(driver_path)
        web_driver = webdriver.Edge(service=service)

    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)

    yield
    web_driver.quit()

# FUNCTION-BASED DRIVER FIXTURE
# Returns driver directly to test functions
# Used when tests accept driver as a parameter

@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    if request.param == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif request.param == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif request.param == 'edge':
        driver_path = os.path.abspath("Drivers/msedgedriver")
        service = EdgeService(driver_path)
        driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


