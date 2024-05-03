from data import Data, UrList
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

class TestConstructorTransition:
    # переход по клику на «Конструктор»
   def test_transition_to_constructor_from_account(self, driver):
        driver.get(UrList.LOGIN_PAGE_URL)
        driver.find_element(*Locators.input_field_email).send_keys(Data.EMAIL)
        driver.find_element(*Locators.input_field_password).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.profile_link))

        driver.find_element(*Locators.constructor_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.make_burger_tag_h1))

        assert driver.find_element(*Locators.make_burger_tag_h1).is_displayed()

    # переход по клику на логотип
   def test_transition_to_constructor_from_logo(self,driver):
        driver.get(UrList.MAIN_PAGE_URL)
        driver.find_element(*Locators.logo_burgers).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        driver.find_element(*Locators.constructor_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.make_burger_tag_h1))

        assert driver.find_element(*Locators.make_burger_tag_h1).is_displayed()

