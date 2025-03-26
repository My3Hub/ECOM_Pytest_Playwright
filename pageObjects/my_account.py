from asyncio import wait_for

class MyAccount:

    def __init__(self,page):
        self.page=page


    def navigate_to_home(self):
        user_account=self.page.locator("#menu")
        user_account.wait_for(state="visible")
        self.page.get_by_role("link", name='Home').click()

