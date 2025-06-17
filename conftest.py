import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data import *
import time


@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения работы драйвера"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def start_from_main_page(driver):
    """Фикстура для начала теста с главной страницы с последующей авторизацией"""
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Кликаем по кнопке "Личный кабинет"
    driver.find_element(*MainPageLocators.personal_account_button).click()

    # Ждем появления кнопки входа и кликаем
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.login_button))

    # Авторизация
    driver.find_element(*LoginPageLocators.login_input).send_keys(Credential.email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
    driver.find_element(*LoginPageLocators.login_button).click()

    # Ждем перехода в личный кабинет
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.order_button))

    return driver

@pytest.fixture
def start_from_main_page_login(driver):
    """Фикстура для начала теста с главной страницы с последующей авторизацией"""
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Кликаем по кнопке "Войти в аккаунт"
    driver.find_element(*MainPageLocators.login_button).click()

    # Ждем появления кнопки входа и кликаем
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.login_button))

    # Авторизация
    driver.find_element(*LoginPageLocators.login_input).send_keys(Credential.email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
    driver.find_element(*LoginPageLocators.login_button).click()

    # Ждем перехода в личный кабинет
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.order_button))

    return driver


@pytest.fixture
def start_from_login_page(driver):
    """Фикстура для начала теста со страницы логина с авторизацией"""
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Авторизация
    driver.find_element(*LoginPageLocators.login_input).send_keys(Credential.email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
    driver.find_element(*LoginPageLocators.login_button).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.order_button))
    return driver


@pytest.fixture
def start_from_recovery_page(driver):
    """Фикстура для начала теста со страницы восстановления пароля с последующей авторизацией"""
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    # Кликаем по кнопке "Войти"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PasswordRecoveryPageLocators.login_link))
    driver.find_element(*PasswordRecoveryPageLocators.login_link).click()

    # Авторизация
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.login_button))
    driver.find_element(*LoginPageLocators.login_input).send_keys(Credential.email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
    driver.find_element(*LoginPageLocators.login_button).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.order_button))
    return driver


@pytest.fixture
def start_from_register_page(driver):
    """Фикстура для начала теста со страницы регистрации с последующей авторизацией"""
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Кликаем по кнопке "Войти"
    driver.find_element(*RegistrationPageLocators.login_link).click()

    # Авторизация
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.login_button))
    driver.find_element(*LoginPageLocators.login_input).send_keys(Credential.email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(Credential.password)
    driver.find_element(*LoginPageLocators.login_button).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.order_button))
    return driver


@pytest.fixture
def register_new_account(driver):
    """Фикстура для регистрации нового аккаунта"""
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.maximize_window()
    # Генерация тестовых данных
    test_data = {
        "name": "TestUser",
        "email": "test"+str(time.time()).replace('.','')+"@test.ru",
        "password": "123456"
    }

    # Заполнение формы регистрации
    driver.find_element(*RegistrationPageLocators.name_input).send_keys(test_data["name"])
    driver.find_element(*RegistrationPageLocators.email_input).send_keys(test_data["email"])
    driver.find_element(*RegistrationPageLocators.password_input).send_keys(test_data["password"])
    driver.find_element(*RegistrationPageLocators.register_button).click()

    # Ждем перехода после регистрации
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

    return driver, test_data["name"], test_data["email"], test_data["password"]


@pytest.fixture
def start_from_main_not_login(driver):
    """Фикстура для начала теста с главной страницы без авторизации"""
    driver.get("https://stellarburgers.nomoreparties.site/")
    return driver


