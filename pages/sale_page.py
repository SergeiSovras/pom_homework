from selenium.webdriver.common.by import By
from pages.base_page import BasePage


header_title_locator = (By.TAG_NAME, 'h1')


class SalePage(BasePage):
    page_url = '/sale.html'
    header_title_locator = (By.TAG_NAME, 'h1')

    def check_page_header_is(self, text):
        header_title = self.find(header_title_locator)
        assert header_title.text == text
