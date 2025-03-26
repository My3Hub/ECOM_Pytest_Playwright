import json
import pytest
from playwright.sync_api import expect
from pageObjects.home_page import HomePage



with open("Data/user_registration_data.json") as info:
    test_data = json.load(info)

@pytest.mark.parametrize('user_details', [test_data["user_details"]])
def test_login(page, user_details):
    home = HomePage(page)
    log_in = home.sign_in()
    my_account = log_in.valid_user(user_details)
    my_account.navigate_to_home()
    home.select_a_product()
    checkout = home.add_to_cart()
    checkout.proceed_to_checkout1()
    checkout.proceed_to_checkout2()

@pytest.mark.parametrize('user_details', [test_data["invalid_user"]])
def test_invalid_credentials(page, user_details):
    home = HomePage(page)
    log_in = home.sign_in()
    log_in.invalid_user(user_details)
    expect(page.locator(".help-block")).to_have_text('Invalid email or password')





