import time

from pageObjects.login_page import LoginPage



class HomePage:
    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto("https://practicesoftwaretesting.com/")


    def sign_in(self):

        self.navigate()
        self.page.get_by_role("link",name="Sign in").click()
        return LoginPage(self.page)

    def select_a_product(self):

        self.page.locator(".card-title").nth(0).click()
        self.page.locator("[data-test='product-name']").filter(has_text=" Combination Pliers ").click()

    def add_to_cart(self):
        self.page.locator("#btn-add-to-cart").wait_for()  # Wait for the button to be available
        self.page.locator("#btn-add-to-cart").click()  # Click the Add to Cart button
        success_message = self.page.locator("[aria-label='Product added to shopping cart.']")
        success_message.wait_for(state="visible")
        success_message.wait_for(state="hidden")
        self.page.locator("[aria-label='cart']").click()




