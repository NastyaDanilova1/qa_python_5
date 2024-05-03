from selenium.webdriver.common.by import By
from data import UrList
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTabsSwitching:
    # переход к вкладке "соусы"
    def test_go_to_sauces(self, driver):
        driver.get(UrList.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.span_sauses)))
        driver.find_element(By.XPATH, Locators.span_sauses).click()
        assert driver.find_element(By.XPATH, Locators.tab_select_in_constructor).text == 'Соусы'

    # переход к вкладке "начинки"
    def test_go_to_stuffing(self, driver):
        driver.get(UrList.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.span_stuffing)))
        driver.find_element(By.XPATH, Locators.span_stuffing).click()
        assert driver.find_element(By.XPATH, Locators.tab_select_in_constructor).text == 'Начинки'

    # переход к вкладке "булки" через вкладку "начинки", потому, что вкладка «булки» при открытии выбран по умолчанию
    def test_go_to_buns(self, driver):
        driver.get(UrList.MAIN_PAGE_URL)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.span_buns)))
        driver.find_element(By.XPATH, Locators.span_buns)
        assert driver.find_element(By.XPATH, Locators.tab_select_in_constructor).text == 'Булки'