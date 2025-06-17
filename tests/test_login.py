import pytest
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data import *

class TestLogin:

    @pytest.mark.usefixtures("start_from_main_page")
    def test_login_from_main_page_personal(self,start_from_main_page):
        """Тест вход через кнопку «Личный кабинет»"""
        driver = start_from_main_page

        assert driver.find_element(*MainPageLocators.order_button).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается на странице"

    @pytest.mark.usefixtures("start_from_main_page_login")
    def test_login_from_main_page_login(self, start_from_main_page_login):
        """Тест вход по кнопке «Войти в аккаунт» на главной"""
        driver = start_from_main_page_login

        assert driver.find_element(*MainPageLocators.order_button).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается на странице"

    @pytest.mark.usefixtures("start_from_register_page")
    def test_login_from_register_page(self, start_from_register_page):
        """Тест вход через кнопку в форме регистрации"""
        driver = start_from_register_page

        assert driver.find_element(*MainPageLocators.order_button).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается на странице"

    @pytest.mark.usefixtures("start_from_recovery_page")
    def test_login_from_recovery_page(self, start_from_recovery_page):
        """Тест вход через кнопку в форме восстановления пароля"""
        driver = start_from_recovery_page

        assert driver.find_element(*MainPageLocators.order_button).is_displayed(), \
            "Кнопка 'Оформить заказ' не отображается на странице"