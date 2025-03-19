from conftest import user_details
from pageObjects.my_account import MyAccount
from pageObjects.user_registration import UserRegistration


class LoginPage:
    def __init__(self ,page):
        self.page = page

    def user_login(self, user_details):
        self.page.get_by_placeholder("Your email").fill(user_details["email"])
        self.page.get_by_placeholder("Your password").fill(user_details["password"])
        self.page.get_by_role("button", name='Login').click()

        if self.page.locator(".help-block").is_visible():
            sign_up = UserRegistration(self.page)
            sign_up.create_account(user_details)


            return self.user_login(user_details)

        return MyAccount(self.page)