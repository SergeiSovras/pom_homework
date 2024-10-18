from pages.base_page import BasePage
from pages.locators import login_locators as loc


class CustomerLogin(BasePage):
    page_url = '/customer/account/login'

    def fill_login_form(self, login, password):
        email_input = self.find(loc.email_input_locator)
        password_input = self.find(loc.password_input_locator)
        submit_button = self.find(loc.submit_button_locator)

        email_input.send_keys(login)
        password_input.send_keys(password)
        submit_button.click()

    def check_error_alert(self, text):
        error_alert = self.find(loc.error_alert_locator)
        assert error_alert.text == text
