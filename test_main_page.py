import time

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    open_page = BasketPage(browser, link)
    open_page.go_to_site()
    open_page.open_the_cart()
    open_page.there_should_be_no_item_in_the_cart()
    open_page.there_should_be_an_empty_cart_message()
@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали
        self.product.delete()
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = ProductPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.go_to_site()  # открываем страницу
        page.go_to_login_page()
        page.should_be_login_link()
