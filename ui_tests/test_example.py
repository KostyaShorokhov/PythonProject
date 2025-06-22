import allure

from ui_tests.fixtures.core_pages import chrome, BasePage
from ui_tests.locators.locators_for_elements import Locators
from ui_tests.urls.url_constants import MAIN_PAGE


@allure.title("Тест открытия браузера")
def test_open_browser(chrome):
    base_page = BasePage(chrome)
    base_page.open_url(MAIN_PAGE)
    assert "Swag Labs" in base_page.get_current_page_title()


@allure.title("Тест авторизации")
def test_auth(chrome):
    base_page = BasePage(chrome)

    base_page.open_url(MAIN_PAGE)
    base_page.input_text(Locators.USER_NAME_INPUT, 'standard_user')
    base_page.input_text(Locators.USER_PASSWORD_INPUT, 'standard_user')
    base_page.click_element(Locators.LOGIN_BUTTON)

    assert base_page.is_element_displayed(Locators.CATALOG), f"Каталог {Locators.CATALOG} продуктов отображается"
