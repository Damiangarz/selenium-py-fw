from selenium.webdriver.common.by import By
from page_objects.ResultsPage import ResultsPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    textbox = (By.ID, "twotabsearchtextbox")
    search_btn = (By.CLASS_NAME, "nav-input")
    cart_icon = (By.ID, "nav-cart-count")

    def textbox_item(self):
        return self.driver.find_element(*HomePage.textbox)

    def click_on_search_btn_item(self):
        self.driver.find_element(*HomePage.search_btn).click()
        results_page = ResultsPage(self.driver)
        return results_page


    def cart_icon_item(self):
        return self.driver.find_element(*HomePage.cart_icon)
