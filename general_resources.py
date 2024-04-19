from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GeneralActions:
    def click_by_xpath(driver, locator):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, f'{locator}'))).click()

    def input_text(driver, locator, text):
        input_field = driver.find_element(By.XPATH, f'{locator}')
        input_field.clear()
        input_field.send_keys(text)

    def solution_confirmation(driver):
        GeneralActions.click_by_xpath(driver, '//button[@id="solution"]')
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, '//code[@class="wrap"]'), "OK. Good answer"))
        assert "OK. Good answer" == driver.find_element(By.XPATH, '//pre[@id="trail"]').text
