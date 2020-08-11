import time
from pages.basePage import BasePage


class LoginPage(BasePage):

    user_email_field = '[placeholder="Email"]'
    user_password_field = '[placeholder="Password"]'
    login_btn = '[type="Submit"]'

    def fill_required_fields(self, user_data):
        open_sign_in = self.find_element_by_text('Sign in', 'a')
        open_sign_in.click()

        user_email_field = self.find_element(self.user_email_field)
        user_email_field.send_keys(user_data['email'])

        user_password_field = self.find_element(self.user_password_field)
        user_password_field.send_keys(user_data['password'])

    def login_as_registered_user(self, user_data):
        self.fill_required_fields(user_data)

        login_btn = self.find_element(self.login_btn)
        login_btn.click()

        time.sleep(1)
