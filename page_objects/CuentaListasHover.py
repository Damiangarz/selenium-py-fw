from selenium.webdriver import ActionChains

from page_objects.HomePage import HomePage


def test_e2e(self):
    action = ActionChains(self.driver)

    action.move_to_element(self.driver.find_element_by_id("nav-link-accountList")).perform()
    action.move_to_element(self.driver.find_element_by_css_selector(".nav-action-inner")).click().perform()