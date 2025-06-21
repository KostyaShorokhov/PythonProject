from selenium.webdriver.common.by import By

from ui_tests.locators.locators_for_elements import USER_NAME_INPUT, USER_PASSWORD_INPUT, LOGIN_BUTTON, CATALOG
from ui_tests.urls.url_constants import MAIN_PAGE


def test_open_browser(chrome):
    chrome.get(MAIN_PAGE)
    assert "Swag Labs" in chrome.title


def test_auth(chrome):
    chrome.get(MAIN_PAGE)
    chrome.find_element(By.ID, USER_NAME_INPUT).send_keys('standard_user')
    chrome.find_element(By.ID, USER_PASSWORD_INPUT).send_keys('secret_sauce')
    chrome.find_element(By.ID, LOGIN_BUTTON).click()
    assert chrome.find_element(By.CSS_SELECTOR, CATALOG).is_displayed(), f"Каталог {CATALOG} продуктов отображается"
