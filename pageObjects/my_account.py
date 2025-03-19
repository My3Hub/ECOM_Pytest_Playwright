
class MyAccount:

    def __init__(self,page):
        self.page=page


    def navigate_to_home(self):
        self.page.get_by_role("link", name='Home').click()

