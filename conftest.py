import pytest
from selenium import webdriver

@pytest.fixture
def selenium():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()