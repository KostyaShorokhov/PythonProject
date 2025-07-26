
from tests.selenium_tests.fixtures.base_actions import chrome, BasePage
from url_constants import TUSUR_PAGE

class TestSelenium:
    """Тест для примера"""
    def test_open_browser(self, chrome):
        base_page = BasePage(chrome)
        base_page.open_url(TUSUR_PAGE)
        assert "do.tusur.ru/qa-test2/" in base_page.get_current_url()