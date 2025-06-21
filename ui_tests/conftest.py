import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui_tests.urls.url_constants import API_URL


@pytest.fixture
def chrome():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--incognito')
    options.add_argument('--disable-popup-blocking')
    driver = webdriver.Chrome(options)
    yield driver
    driver.quit()

# conftest.py

import pytest
import requests

@pytest.fixture(scope='session')
def session():
    """Настроенная сессия для всех тестов"""
    sess = requests.request().Session()
    sess.headers.update({
        'Content-Type': 'application/json'
    })
    return sess
