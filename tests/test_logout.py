import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestLogout:
    def test_personal_account_logout(self, start_from_main_page):
        driver = start_from_main_page

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.personal_account_button)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        driver.find_element(*AccountPageLocators.logout_button).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
