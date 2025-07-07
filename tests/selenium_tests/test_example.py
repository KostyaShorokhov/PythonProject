import allure

from tests.selenium_tests.fixtures.base_actions import chrome, BasePage
from tests.selenium_tests.locators.locators_for_elements import Locators
from url_constants import MAIN_PAGE


@allure.title("Тест открытия браузера")
def test_open_browser(chrome):
    base_page = BasePage(chrome)
    from url_constants import TUSUR_PAGE
    base_page.open_url(TUSUR_PAGE)
    assert "do.tusur.ru/qa-test2/" in base_page.get_current_url()


@allure.title("Тест авторизации")
def test_auth_success(chrome):
    base_page = BasePage(chrome)

    base_page.open_url(MAIN_PAGE)
    base_page.input_text(Locators.USER_NAME_INPUT, 'standard_user')
    base_page.input_text(Locators.USER_PASSWORD_INPUT, 'secret_sauce')
    base_page.click_element(Locators.LOGIN_BUTTON)

    assert base_page.is_element_displayed(Locators.CATALOG), f"Каталог {Locators.CATALOG} продуктов отображается"

@allure.title("Тест неудачной авторизации")
def test_auth_failed(chrome):
    base_page = BasePage(chrome)
    base_page.open_url(MAIN_PAGE)
    base_page.input_text(Locators.USER_NAME_INPUT, 'invalid_user')
    base_page.input_text(Locators.USER_PASSWORD_INPUT, 'wrong_password')
    base_page.click_element(Locators.LOGIN_BUTTON)

    error_message = base_page.get_text_element(Locators.ERROR)
    assert "Epic sadface:" in error_message, "Сообщение об ошибке отсутствует"

