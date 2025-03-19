from conftest import user_details



class UserRegistration:
    def __init__(self,page):
        self.page=page


    def create_account(self,user_details):

        self.page.get_by_role("link", name="Register your account").click()
        self.page.get_by_label("First name").fill(user_details["first_name"])
        self.page.get_by_placeholder("Your last name *").fill(user_details["last_name"])
        self.page.get_by_placeholder("Your Date of birth *").click()
        self.page.get_by_placeholder("Your Date of birth *").fill(user_details["dob"])
        # self.page.locator("[data-test='dob']").fill("1993-07-03")
        self.page.get_by_placeholder("Your Street *").fill(user_details["street"])
        self.page.locator("[data-test='postal_code']").fill(user_details["postal_code"])
        self.page.get_by_label("City").fill(user_details["city"])
        self.page.get_by_placeholder("Your State *").fill(user_details["state"])
        self.page.get_by_role("combobox").select_option(user_details["country"])
        self.page.get_by_placeholder("Your phone *").fill(user_details["phone"])
        self.page.get_by_label("Email address").fill(user_details["email"])
        self.page.get_by_placeholder("Your password").fill(user_details["password"])
        self.page.get_by_role("button", name="Register").click()

