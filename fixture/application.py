from selenium import webdriver
from fixture.session import Session_helper
from fixture.group import Group_helper
from fixture.entry import Entry_helper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        #self.wd.implicitly_wait(60)
        self.session = Session_helper(self)
        self.group = Group_helper(self)
        self.entry = Entry_helper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()
