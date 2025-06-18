import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestConstructorNavigation:
    def test_switch_to_buns_section(self,driver):
        """Проверка перехода в раздел 'Булки'"""
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Переключаемся на другой раздел (например, Соусы), чтобы убедиться, что переключение работает
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.sauces_section)).click()
        WebDriverWait(driver, 15).until(lambda d: d.find_element(*MainPageLocators.active_section).text == "Соусы")
        # Кликаем на раздел "Булки"
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.buns_section)).click()
        # Проверяем, что раздел активен
        WebDriverWait(driver, 15).until(lambda d: d.find_element(*MainPageLocators.active_section).text == "Булки")
        active_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.active_section))

        assert active_section.text == "Булки", "Раздел 'Булки' не стал активным"

    def test_switch_to_sauces_section(self,driver):
        """Проверка перехода в раздел 'Соусы'"""
        driver.get("https://stellarburgers.nomoreparties.site/")


        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.fillings_section)).click()
        WebDriverWait(driver, 15).until(lambda d: d.find_element(*MainPageLocators.active_section).text == "Начинки")

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.sauces_section)).click()

        WebDriverWait(driver, 15).until(lambda d: d.find_element(*MainPageLocators.active_section).text == "Соусы")
        active_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.active_section))

        assert active_section.text == "Соусы", "Раздел 'Соусы' не стал активным"

    def test_switch_to_fillings_section(self, driver):
        """Проверка перехода в раздел 'Начинки'"""
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.sauces_section)).click()
        WebDriverWait(driver, 15).until(lambda d: d.find_element(*MainPageLocators.active_section).text == "Соусы")

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.fillings_section)).click()

        WebDriverWait(driver, 20).until(lambda d: d.find_element(*MainPageLocators.active_section).text == "Начинки")
        active_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.active_section))

        assert active_section.text == "Начинки", "Раздел 'Начинки' не стал активным"
