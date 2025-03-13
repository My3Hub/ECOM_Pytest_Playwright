import json
import os
import time

import pytest
from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import browser, context

with open("Data/user_registration_data.json") as info:
    test_data = json.load(info)  # converting json file into python object
    user_data = test_data['user_details']

#Filled user details using different get_by_* and css for practice
@pytest.mark.parametrize('user_details',user_data)
def test_user_registration(playwright: Playwright,user_details):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_role("link", name="Register your account").click()
    page.get_by_label("First name").fill(user_details["first_name"])
    page.get_by_placeholder("Your last name *").fill(user_details["last_name"])
    page.get_by_placeholder("Your Date of birth *").click()
    page.get_by_placeholder("Your Date of birth *").fill(user_details["dob"])
    # page.locator("[data-test='dob']").fill("1993-07-03")
    page.get_by_placeholder("Your Street *").fill(user_details["street"])
    page.locator("[data-test='postal_code']").fill(user_details["postal_code"])
    page.get_by_label("City").fill(user_details["city"])
    page.get_by_placeholder("Your State *").fill(user_details["state"])
    page.get_by_role("combobox").select_option(user_details["country"])
    page.get_by_placeholder("Your phone *").fill(user_details["phone"])
    page.get_by_label("Email address").fill(user_details["email"])
    page.get_by_placeholder("Your password").fill(user_details["password"])
    page.get_by_role("button",name="Register").click()
    time.sleep(10)

