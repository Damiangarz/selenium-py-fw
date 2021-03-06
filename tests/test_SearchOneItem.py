from page_objects.HomePage import HomePage
from test_data.SearchItemTestData import SearchItemTestData
from utilities.BaseClass import BaseClass
import pytest


class TestSearchOneItem(BaseClass):
    @pytest.fixture(params=SearchItemTestData.get_excel_data('TC1'), scope='session')
    def get_data(self, request):
        return request.param

    @pytest.mark.one
    def test_search_one_item(self, get_data):
        # Selenium Steps
        log = self.get_logger()
        log.debug('Starting Test Search One Item')
        home_page = HomePage(self.driver)
        home_page.textbox_item().send_keys(get_data['first_item'])
        results_page = home_page.click_on_search_btn_item()
        item_page = results_page.click_on_price_list_item()
        price_item_page = item_page.get_price_item_page()
        go_to_cart_page = item_page.click_on_add_to_cart_button()
        cart_page = go_to_cart_page.click_on_go_to_cart_item()
        price_cart_page = cart_page.get_price_cart_page()
        # utilities
        log.info('%s %s %s %s', 'Prices to be compared before formatting:', price_cart_page, 'And:',  price_item_page)
        price_item_page = BaseClass.remove_char(price_item_page)
        price_cart_page = BaseClass.remove_char(price_cart_page)
        log.info('%s %s %s %s', 'Prices with chars removed:',  price_cart_page, 'To be compared with:', price_item_page)
        cart_page.delete_btn_item()[0].click()
        # Validations
        assert BaseClass.remove_dot(price_cart_page) in BaseClass.remove_dot(price_item_page)
        assert '0' == home_page.cart_icon_item().text
        log.debug('Completed Test Search One Item')
