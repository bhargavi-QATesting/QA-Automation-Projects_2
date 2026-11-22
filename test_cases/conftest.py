import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Browser must be either chrome or firefox or edge")
    return driver


#hook for adding environment info in html report
def pytest_configure(config):
    config.stash[metadata_key] ["Project Name"] = 'Ecommerce Project, OrangeHRM'
    config.stash[metadata_key]["Test Module Name"] = 'Admin Login'
    config.stash[metadata_key] ["Tester Name"] = 'Bhargavi'

#hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

#@pytest.fixture()
'''def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs",{"credentials_enable_service": False,"profile.password_manager_enabled": False})
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()'''

