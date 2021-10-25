from .locators import BasketPageLocators
from .base_page import BasePage


# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import InvalidArgumentException


class BasketPage(BasePage):
    def there_should_be_no_item_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_THE_BASKET),\
            "Товар был найден в корзине"

    def there_should_be_an_empty_cart_message(self):
        assert self.waiting_text_that_the_cart_is_empty(*BasketPageLocators.BASKET_MESSAGE),\
            "В корзине есть товар"
