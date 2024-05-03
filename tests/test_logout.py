from data import Data, UrList
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:
    # выход по кнопке «Выйти» в лк
    def test_logout(self, driver):
        driver.get(UrList.MAIN_PAGE_URL)
        driver.find_element(*Locators.main_login_button).click()
        driver.find_element(*Locators.input_field_email).send_keys(Data.EMAIL)
        driver.find_element(*Locators.input_field_password).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.profile_link))

        driver.find_element(*Locators.logout_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.login_button_login_page))

        assert driver.find_element(*Locators.login_button_login_page)
