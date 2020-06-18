from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    price_cart_page = (By.CLASS_NAME, "sc-product-price")
    delete_btn = (By.CSS_SELECTOR, "input[value=Eliminar]")
    price_subtotal = (By.ID, "sc-subtotal-amount-activecart")

    def get_price_cart_page(self):
        return self.driver.find_element(*CartPage.price_cart_page).text

    # def delete_btn_item(self):
    #     return self.driver.find_element(*CartPage.delete_btn)

    def delete_btn_item(self):
        return self.driver.find_elements(*CartPage.delete_btn)

    def get_price_subtotal(self):
        return self.driver.find_element(*CartPage.price_subtotal).text
