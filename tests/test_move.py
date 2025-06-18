import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestMovePersonalAccount:
    def test_personal_account_redirect(self,driver):
        #Проверка перехода в Личный кабинет
        # Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # Кликаем на кнопку "Личный кабинет"
        driver.find_element(*MainPageLocators.personal_account_button).click()

        # Ожидаем перехода на страницу входа (для неавторизованных пользователей)
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        # Проверяем URL и наличие формы входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        assert driver.find_element(*LoginPageLocators.login_button).is_displayed()



    def test_personal_account_redirect_to_personal_account(self,start_from_main_page):
        driver = start_from_main_page

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.personal_account_button)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

class TestMoveConstructor:
    def test_navigation_via_constructor(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*LoginPageLocators.constructor_button).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


    def test_navigation_via_constructor_personal_account(self,start_from_main_page):
        driver = start_from_main_page
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.personal_account_button)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        driver.find_element(*AccountPageLocators.constructor_link).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


class TestMoveLogo:
    def test_navigation_via_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*LoginPageLocators.logo).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


    def test_navigation_via_logo_personal_account(self, start_from_main_page):
        driver = start_from_main_page
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.personal_account_button)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        driver.find_element(*AccountPageLocators.logo).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


