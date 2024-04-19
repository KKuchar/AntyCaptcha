import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def initialize_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://antycaptcha.amberteam.pl/general_exercises/")
    yield driver
    driver.quit()


def open_exercise(driver, number):
    driver.find_element(By.XPATH, f'//a[contains(text(), "Exercise {number}")]').click()
