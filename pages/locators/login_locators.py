from selenium.webdriver.common.by import By


email_input_locator = (By.ID, 'email')
password_input_locator = (By.ID, 'pass')
submit_button_locator = (By.ID, 'send2')
error_alert_locator = (
            By.CSS_SELECTOR,
            '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')