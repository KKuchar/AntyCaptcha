from selenium.webdriver.common.by import By
from conftest import open_exercise
from general_resources import GeneralActions
from three_buttons_resource import Locators


def test_three_buttons(initialize_browser):
    open_exercise(initialize_browser, "1")
    assert Locators.title == initialize_browser.title
    trial_set = initialize_browser.find_element(By.XPATH, '//td[contains(text(), "Trail set to: ")]//code').text.upper()
    elements = [trial_set[0:2], trial_set[2:4], trial_set[4:6]]
    for element in elements:
        GeneralActions.click_by_xpath(initialize_browser, '//button[contains(text(), "' + element + '")]')
    GeneralActions.solution_confirmation(initialize_browser)
