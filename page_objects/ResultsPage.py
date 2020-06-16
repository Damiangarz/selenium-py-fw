from selenium.webdriver.common.by import By
from page_objects.ItemPage import ItemPage


class ResultsPage:
    def __init__(self, driver):
        self.driver = driver

    priceList = (By.CLASS_NAME, "a-price-whole")

    def click_on_price_list_item(self):
        self.driver.find_elements(*ResultsPage.priceList)[0].click()
        item_page = ItemPage(self.driver)
        return item_page
