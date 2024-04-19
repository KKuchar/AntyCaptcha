from selenium.webdriver.common.by import By
from conftest import open_exercise
from general_resources import GeneralActions
from radio_buttons_resource import names


def test_radio_buttons(initialize_browser):
    open_exercise(initialize_browser, 4)
    for i in range(0, 4):
        choose = initialize_browser.find_element(By.XPATH, '//td[contains(text(), "In the group ' + str(i) + ' choose ")]/code').text
        GeneralActions.click_by_xpath(initialize_browser, '//input[@value="v' + str(names.get(choose)) + str(i) + '"]')
    GeneralActions.solution_confirmation(initialize_browser)
