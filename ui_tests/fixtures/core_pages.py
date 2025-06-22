import allure
import pytest
import requests
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--incognito')
    options.add_argument('--disable-popup-blocking')
    driver = webdriver.Chrome(options)
    yield driver
    driver.quit()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        with allure.step(f"Переходим на страницу {url}"): self.driver.get(url)

    def get_current_page_title(self):
        return self.driver.title

    def find_element(self, locator, timeout=10):
        with allure.step(f"Находим элемент по локатору {locator}"): return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))

    def click_element(self, locator):
        strategy, value = locator.value
        with allure.step(f"Кликаем по элементу"): self.driver.find_element(strategy, value).click()

    def input_text(self, locator, text):
        strategy, value = locator.value
        element = self.driver.find_element(strategy, value)
        element.clear()
        with allure.step(f"Вводим значение '{text}'"): element.send_keys(text)

    def is_visible(self, locator, timeout=10):
        try:
            with allure.step(f"Проверяем видимость элемента по локатору {locator}"): WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_displayed(self, locator):
        strategy, value = locator.value
        element = self.driver.find_element(strategy, value)
        with allure.step(f"Проверяем отображение элемента"): return element.is_displayed()


@pytest.fixture(scope='session')
def session():
    """Настроенная сессия для всех тестов"""
    sess = requests.request().Session()
    sess.headers.update({
        'Content-Type': 'application/json'
    })
    return sess
