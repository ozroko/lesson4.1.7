link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    button = browser.find_element_by_class_name("btn.btn-primary.btn-block")
    button.scrool(-10)
    button.click()

