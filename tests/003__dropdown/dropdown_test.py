from selenium.webdriver.common.by import By
from general_resources import GeneralActions
from conftest import open_exercise


def test_dropdown(initialize_browser):
    open_exercise(initialize_browser, 3)
    text_to_choose = initialize_browser.find_element(By.XPATH, '//td[contains(text(), "In the following dropdown choose ")]/code').text
    GeneralActions.click_by_xpath(initialize_browser, '//option[contains(text(), "' + text_to_choose + '")]')
    GeneralActions.solution_confirmation(initialize_browser)
