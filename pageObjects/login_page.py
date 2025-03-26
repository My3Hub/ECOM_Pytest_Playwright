from playwright.sync_api import expect
from pageObjects.user_registration import UserRegistration
from pageObjects.my_account import MyAccount

class LoginPage:
    def __init__(self, page):
        self.page = page

    def _fill_login_form(self, email, password):
        self.page.get_by_placeholder("Your email").fill(email)
        self.page.get_by_placeholder("Your password").fill(password)
        self.page.get_by_role("button", name='Login').click()

    def valid_user(self, user_details):
        self._fill_login_form(user_details["email"], user_details["password"])
        self.page.wait_for_load_state("networkidle")

        # If login fails, create account and then log in again
        if self.page.locator(".help-block").is_visible():
            self._create_account(user_details)
            self._fill_login_form(user_details["email"], user_details["password"])

        return MyAccount(self.page)

    def _create_account(self, user_details):
        sign_up = UserRegistration(self.page)
        sign_up.create_account(user_details)

    def invalid_user(self, user_details):
        self._fill_login_form(user_details["email"], user_details["password"])


