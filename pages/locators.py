from selenium.webdriver.common.by import By


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    CART_LINK = (By.CLASS_NAME, "btn-group")
    BASKET_MESSAGE = (By.TAG_NAME,"p")
    ITEMS_IN_THE_BASKET = (By.CSS_SELECTOR,"#basket_formset")




class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    CLEARANCE_BUTTON = (By.CLASS_NAME, "btn.btn-info")
    BOOK_NAME = (By.TAG_NAME, "h1")
    NEM_BOOK_ADDED_TO_CART = (
        By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.btnbtn-info")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)")
