from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для главной страницы"""
    login_button = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    personal_account_button = (By.XPATH, "//a[@href='/account']")  # Кнопка "Личный кабинет" в шапке
    constructor_button = (By.XPATH, "//a[@href='/']")  # Кнопка "Конструктор" в шапке
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers
    buns_section = (By.XPATH, "//span[text()='Булки']/parent::div")  # Раздел "Булки" в конструкторе
    sauces_section = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Раздел "Соусы" в конструкторе
    fillings_section = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Раздел "Начинки" в конструкторе
    active_section = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")  # Активный раздел конструктора
    order_button = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # Кнопка подтверждающая успешный вход

class LoginPageLocators:
    """Локаторы для страницы входа"""
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    constructor_button = (By.XPATH, "//a[@href='/']")  # Кнопка "Конструктор" в шапке
    login_label = (By.XPATH, "//h2[text()='Вход']")  # Заголовок "Вход" на странице
    login_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода email
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле ввода пароля
    login_button = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    registration_link = (By.XPATH, "//a[@href='/register']")  # Ссылка "Зарегистрироваться"
    restore_password_link = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка "Восстановить пароль"


class RegistrationPageLocators:
    """Локаторы для страницы регистрации"""
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле ввода имени
    email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода email
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле ввода пароля
    register_button = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    login_link = (By.XPATH, "//a[@href='/login']")  # Ссылка "Войти" (для тех, кто уже зарегистрирован)
    password_error = (By.XPATH, "//p[contains(@class, 'input__error')]")  # Сообщение об ошибке пароля
    registration_error = (By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'уже существует')]")



class AccountPageLocators:
    """Локаторы для личного кабинета"""
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле с именем пользователя
    login_input = (By.XPATH, "//label[text()='Логин']/following-sibling::input")  # Поле с логином (email)
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле с паролем
    logout_button = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"
    constructor_link = (By.XPATH, "//a[@href='/']")  # Ссылка "Конструктор" в личном кабинете
    profile_section = (By.XPATH, "//section[contains(@class, 'Profile_profile')]")#Профиль


class PasswordRecoveryPageLocators:
    """Локаторы для страницы восстановления пароля"""
    email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода email
    recover_button = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка "Восстановить"
    login_link = (By.XPATH, "//a[@href='/login']")  # Ссылка "Войти" (для тех, кто вспомнил пароль)