import json
import time

import pytest

from pageObjects.home_page import HomePage
from pageObjects.login_page import LoginPage
from pageObjects.user_registration import UserRegistration

with open("Data/user_registration_data.json") as info:
    test_data = json.load(info)  # converting json file into python object
    user_data = test_data['user_details']


@pytest.mark.parametrize('user_details', user_data)
def test_login(page, user_details):
    home=HomePage(page)
    log_in=home.sign_in()
    my_account=log_in.user_login(user_details)
    my_account.navigate_to_home()
    home.select_a_product()
    home.add_to_cart()



