from data import Data, UrList
import pytest
from locators import Locators
from conftest import driver
import functions_for_help
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    # проверка успешной регистрации
    def test_registration_with_all_date(self, driver):
        driver.get(UrList.REGISTRATION_PAGE_URL)
        driver.find_element(*Locators.input_field_name).send_keys(functions_for_help.random_name())
        driver.find_element(*Locators.input_field_email).send_keys(functions_for_help.random_email())
        driver.find_element(*Locators.input_field_password).send_keys(functions_for_help.random_password())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located(Locators.login_button_login_page))

        assert driver.find_element(*Locators.login_button_login_page)

    # проверка регистрации без ввода имени пользователя
    def test_registration_without_name(self, driver):
        driver.get(UrList.REGISTRATION_PAGE_URL)
        driver.find_element(*Locators.input_field_email).send_keys(functions_for_help.random_email())
        driver.find_element(*Locators.input_field_password).send_keys(functions_for_help.random_password())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.registration_button))

        assert driver.find_element(*Locators.registration_button).text == 'Зарегистрироваться'

    # проверка регистрации без ввода почты
    def test_registration_without_email(self, driver):
        driver.get(UrList.REGISTRATION_PAGE_URL)
        driver.find_element(*Locators.input_field_name).send_keys(functions_for_help.random_name())
        driver.find_element(*Locators.input_field_password).send_keys(functions_for_help.random_password())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.registration_button))

        assert driver.find_element(*Locators.registration_button).text == 'Зарегистрироваться'

        # проверка регистрации без ввода пароля
    def test_registration_without_password(self, driver):
        driver.get(UrList.REGISTRATION_PAGE_URL)
        driver.find_element(*Locators.input_field_name).send_keys(functions_for_help.random_name())
        driver.find_element(*Locators.input_field_email).send_keys(functions_for_help.random_email())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.registration_button))

        assert driver.find_element(*Locators.registration_button).text == 'Зарегистрироваться'

   # проверка регистрации с паролем содержащим <6 символов
    def test_registration_with_password_less_6_symbols(self, driver):
        driver.get(UrList.REGISTRATION_PAGE_URL)
        driver.find_element(*Locators.input_field_name).send_keys(functions_for_help.random_name())
        driver.find_element(*Locators.input_field_email).send_keys(functions_for_help.random_email())
        driver.find_element(*Locators.input_field_password).send_keys(functions_for_help.random_incorrect_password())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(
           expected_conditions.visibility_of_element_located(Locators.incorrect_password_message))

        assert driver.find_element(*Locators.incorrect_password_message).text == 'Некорректный пароль'

    # проверка регистрации с почтой без домена
    def test_registration_with_incorrect_email(self, driver):
        driver.get(UrList.REGISTRATION_PAGE_URL)
        driver.find_element(*Locators.input_field_name).send_keys(functions_for_help.random_name())
        driver.find_element(*Locators.input_field_email).send_keys(functions_for_help.mail_without_domen())
        driver.find_element(*Locators.input_field_password).send_keys(functions_for_help.random_password())
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 5).until(
           expected_conditions.visibility_of_element_located(Locators.user_exists_message))

        assert driver.find_element(*Locators.user_exists_message).text == 'Такой пользователь уже существует'

        # проверка регистрации уже существующего пользователя
    def test_registration_with_exist_user(self, driver):
        driver.get(UrList.REGISTRATION_PAGE_URL)
        driver.find_element(*Locators.input_field_name).send_keys(Data.NAME)
        driver.find_element(*Locators.input_field_email).send_keys(Data.EMAIL)
        driver.find_element(*Locators.input_field_password).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.user_exists_message))

        assert driver.find_element(*Locators.user_exists_message).text == 'Такой пользователь уже существует'

