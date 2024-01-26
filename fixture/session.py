import time
from selenium.webdriver.common.by import By

class Session_helper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element('name', "user").clear()
        wd.find_element('name', "user").send_keys(username)
        wd.find_element('name', "pass").click()
        wd.find_element('name', "pass").clear()
        wd.find_element('name', "pass").send_keys(password)
        wd.find_element('xpath', "//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        time.sleep(5)
        wd.find_element('link text', "Logout").click()
        time.sleep(5)

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements('link text', "Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//div/div[1]/form/b").text == "("+username+")"