from data import Data, UrList
import functions_for_help
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
    # вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_from_main_page(self, driver):
        driver.get(UrList.MAIN_PAGE_URL)
        driver.find_element(*Locators.main_login_button).click()
        driver.find_element(*Locators.input_field_email).send_keys(Data.EMAIL)
        driver.find_element(*Locators.input_field_password).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver.find_element(*Locators.order_button).is_displayed()

        # вход по кнопке «Личный кабинет»
    def test_login_from_account(self, driver):
        driver.get(UrList.MAIN_PAGE_URL)
        driver.find_element(*Locators.personal_account_button).click()
        driver.find_element(*Locators.input_field_email).send_keys(Data.EMAIL)
        driver.find_element(*Locators.input_field_password).send_keys(Data.PASSWORD)
        driver.find_element(*Locators. login_button_login_page).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver.find_element(*Locators.order_button).is_displayed()

        # вход по кнопке в форме регистрации
    def test_login_after_registration(self, driver):
        driver.get(UrList.REGISTRATION_PAGE_URL)
        driver.find_element(*Locators.input_field_name).send_keys(functions_for_help.random_name())
        driver.find_element(*Locators.input_field_email).send_keys(functions_for_help.random_email())
        driver.find_element(*Locators.input_field_password).send_keys(functions_for_help.random_password())
        driver.find_element(*Locators.registration_button).click()

        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.login_button_login_page))

        driver.find_element(*Locators.input_field_email).send_keys(Data.EMAIL)
        driver.find_element(*Locators.input_field_password).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver.find_element(*Locators.order_button).is_displayed()

        # вход по кнопке в форме восстановления пароля
    def test_login_from_recovery_pass(self, driver):
        driver.get(UrList.LOGIN_PAGE_URL)
        driver.find_element(*Locators.recovery_pass_link).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.recovery_pass_button))

        driver.find_element(*Locators.link_login_from_recovery_pass).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.login_button_login_page))

        driver.find_element(*Locators.input_field_email).send_keys(Data.EMAIL)
        driver.find_element(*Locators.input_field_password).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver.find_element(*Locators.order_button).is_displayed()