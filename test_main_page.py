import time

from .pages.basket_page import BasketPage


# def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     open_page = BasketPage(browser, link)
#     open_page.go_to_site()
#     open_page.open_the_cart()
#     open_page.there_should_be_no_item_in_the_cart()
#     open_page.there_should_be_an_empty_cart_message()
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    open_page = BasketPage(browser, link)
    open_page.go_to_site()
    open_page.open_the_cart()
    open_page.there_should_be_no_item_in_the_cart()
    open_page.there_should_be_an_empty_cart_message()


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()# открываем страницу
#     page.go_to_login_page()
#     page.should_be_login_link()
