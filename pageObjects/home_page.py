from pageObjects.checkout_page import CheckoutPage
from pageObjects.login_page import LoginPage


class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://practicesoftwaretesting.com/")

    def sign_in(self):
        """Navigates to sign-in page."""
        self.navigate()
        self.page.get_by_role("link", name="Sign in").click()
        return LoginPage(self.page)

    def select_a_product(self):
        self.page.locator(".card-title").nth(0).click()
        self.page.locator("[data-test='product-name']").filter(has_text=" Combination Pliers ").click()

    def add_to_cart(self):
        self.page.locator("#btn-add-to-cart").wait_for()
        self.page.locator("#btn-add-to-cart").click()
        self.page.locator("[aria-label='Product added to shopping cart.']").wait_for(state="hidden")
        self.page.locator("[aria-label='cart']").click()
        return CheckoutPage(self.page)
