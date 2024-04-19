from selenium.webdriver.common.by import By
from conftest import open_exercise
from general_resources import GeneralActions


def test_input_text_into_correct_field(initialize_browser):
    open_exercise(initialize_browser, "2")
    text = initialize_browser.find_element(By.XPATH, '(//td[contains(text(), "Enter text")]/code)[1]').text
    GeneralActions.input_text(initialize_browser, '//input[@type="text"]', text)
    GeneralActions.click_by_xpath(initialize_browser, '//button[@id="btnButton1"]')
    GeneralActions.solution_confirmation(initialize_browser)
