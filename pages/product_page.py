from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def pressing_buttons(self):
        button_clicl = self.driver.find_element(*ProductPageLocators.BUTTON)
        button_clicl.click()

    def mathematical_equation(self):
        return self.solve_quiz_and_get_code()

    def checking_if_an_item_is_in_the_cart(self):
        if self.is_element_present(*ProductPageLocators.NEM_BOOK_ADDED_TO_CART) and self.is_element_present(
                *ProductPageLocators.BOOK_PRICE):
            # Поиск сообщения об добавлении книги в корзину
            print("Товар была добавлена к корзину!!!!")
        if self.comparison(*ProductPageLocators.NEM_BOOK_ADDED_TO_CART, *ProductPageLocators.BOOK_NAME):
            # Сравнение названия товара и товара добавленого в корзину
            print("Названия товаров схожи!!!")
        if self.comparison(*ProductPageLocators.BOOK_PRICE, *ProductPageLocators.BASKET_PRICE):
            # Сравнение цены товара и корзины
            print(f"Цена корзины {self.driver.find_element(*ProductPageLocators.BASKET_PRICE).text}")
            print("Цена товара и цена корзины схожи!!!")

    def product_name(self):
        print(f"Название товара {self.driver.find_element(*ProductPageLocators.BOOK_NAME).text} !!!")

    def the_price_of_the_product(self):
        print(f"Цена товара {self.driver.find_element(*ProductPageLocators.BOOK_PRICE).text} !!!")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе отображается, но не должно"

    def no_success_message_with(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе отображается, но не должно"

