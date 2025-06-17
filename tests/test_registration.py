import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegistrationPageLocators
from data import *

class TestRegistration:

    @pytest.mark.usefixtures("register_new_account")
    def test_successful_registration(self, register_new_account):
        """Тест успешной регистрации с валидными данными"""
        driver, name, email, password = register_new_account
        # Проверяем что мы на странице входа
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_registration_with_invalid_password(self, driver):
        """Тест регистрации с некорректным паролем (менее 6 символов)"""
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.maximize_window()

        # Заполняем форму с некорректным паролем
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(Credential.name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(Credential.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(Credential.short_password)
        driver.find_element(*RegistrationPageLocators.register_button).click()

        # Проверяем сообщение об ошибке
        error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.password_error)).text

        assert error_message == "Некорректный пароль", "Не отображается сообщение об ошибке для короткого пароля"
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register", \
            "Произошел переход при невалидных данных"

    def test_existing_account_registration(self, driver):
        """Тест попытки регистрации с уже существующим email"""
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.maximize_window()

        # Заполняем форму данными уже зарегистрированного пользователя
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(Credential.name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(Credential.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(Credential.password)
        driver.find_element(*RegistrationPageLocators.register_button).click()

        # Ожидаем появления сообщения об ошибке
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationPageLocators.registration_error)
        ).text

        # Проверяем что остались на странице регистрации
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register", \
            "Произошел переход при попытке регистрации существующего аккаунта"

        # Проверяем текст ошибки
        assert error_message == "Такой пользователь уже существует", \
            "Неверное сообщение об ошибке для существующего пользователя"