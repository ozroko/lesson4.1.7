
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .locators import BasketPageLocators

import math


class BasePage():
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def go_to_site(self):
        return self.driver.get(self.url)

    def open_the_cart(self):
        basket = self.driver.find_element(*BasketPageLocators.CART_LINK)
        basket.click()

    def should_be_a_link_for_the_cart(self):
        assert self.is_element_present(*BasketPageLocators.CART_LINK), \
            "Basket link is not presented"

    def go_to_login_page(self):
        link = self.driver.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except InvalidArgumentException:
            print("error InvalidArgumentException")
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def comparison(self, how, what, how1, what2):
        try:
            self.driver.find_element(how, what).text == self.driver.find_element(how1, what2).text
        except  AttributeError:
            return False
        except InvalidArgumentException:
            print("error InvalidArgumentException")
        except NoSuchElementException:
            print("error NoSuchElementException")
            return False
        return True

    def waiting_text_that_the_cart_is_empty(self, how, what, time=4):
        language = self.driver.execute_script("return window.navigator.userLanguage || window.navigator.language")
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en-US": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
        }
        try:
            WebDriverWait(self.driver, time) \
                .until(EC.text_to_be_present_in_element((how, what), f'{languages[language]}'))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
