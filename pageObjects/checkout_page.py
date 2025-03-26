class CheckoutPage:
    def __init__(self,page):
        self.page=page

    def proceed_to_checkout1(self):
        self.page.get_by_role("button",name="Proceed to checkout").click()

    def proceed_to_checkout2(self):
        self.page.locator("[data-test='proceed-2']").click()