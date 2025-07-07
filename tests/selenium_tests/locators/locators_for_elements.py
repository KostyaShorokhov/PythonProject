from enum import Enum

from selenium.webdriver.common.by import By


class Locators(Enum):
    USER_NAME_INPUT = (By.ID, "user-name")
    USER_PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    CATALOG = (By.CSS_SELECTOR, "[data-test='title']")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
