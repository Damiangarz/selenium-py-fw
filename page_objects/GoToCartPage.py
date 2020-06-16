from selenium.webdriver.common.by import By
from page_objects.CartPage import CartPage


class GoToCartPage:
    def __init__(self, driver):
        self.driver = driver

    go_to_cart = (By.LINK_TEXT, "Carrito")

    def click_on_go_to_cart_item(self):
        self.driver.find_element(*GoToCartPage.go_to_cart).click()
        cart_page = CartPage(self.driver)
        return cart_page

