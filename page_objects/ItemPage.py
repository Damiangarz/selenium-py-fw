from selenium.webdriver.common.by import By
from page_objects.GoToCartPage import GoToCartPage


class ItemPage:
    def __init__(self, driver):
        self.driver = driver

    price_item_page = (By.ID, "priceblock_ourprice")
    add_to_cart_btn = (By.ID, "add-to-cart-button")

    def get_price_item_page(self):
        return self.driver.find_element(*ItemPage.price_item_page).text


    def click_on_add_to_cart_button(self):
        self.driver.find_element(*ItemPage.add_to_cart_btn).click()
        go_to_cart_page = GoToCartPage(self.driver)
        return go_to_cart_page
