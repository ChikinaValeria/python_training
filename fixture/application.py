from selenium import webdriver
from selenium.webdriver.support.select import Select

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element('name', "user").clear()
        wd.find_element('name', "user").send_keys(username)
        wd.find_element('name', "pass").click()
        wd.find_element('name', "pass").clear()
        wd.find_element('name', "pass").send_keys(password)
        wd.find_element('xpath', "//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element('link text', "groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element('name', "new").click()
        # fill group form
        wd.find_element('name', "group_name").click()
        wd.find_element('name', "group_name").clear()
        wd.find_element('name', "group_name").send_keys(group.name)
        wd.find_element('name', "group_header").click()
        wd.find_element('name', "group_header").clear()
        wd.find_element('name', "group_header").send_keys(group.header)
        wd.find_element('name', "group_footer").click()
        wd.find_element('name', "group_footer").clear()
        wd.find_element('name', "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element('name', "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element('link text', "group page").click()


    def create_entry(self, entry):
        wd = self.wd
        # init entry creation
        wd.find_element('link text', "add new").click()
        # fill entry form
        wd.find_element('name', "firstname").click()
        wd.find_element('name', "firstname").clear()
        wd.find_element('name', "firstname").send_keys(entry.firstname)
        wd.find_element('name', "lastname").click()
        wd.find_element('name', "lastname").clear()
        wd.find_element('name', "lastname").send_keys(entry.lastname)
        wd.find_element('name', "address").click()
        wd.find_element('name', "address").clear()
        wd.find_element('name', "address").send_keys(entry.address)
        wd.find_element('name', "home").click()
        wd.find_element('name', "home").clear()
        wd.find_element('name', "home").send_keys(entry.home)
        wd.find_element('name', "mobile").click()
        wd.find_element('name', "mobile").clear()
        wd.find_element('name', "mobile").send_keys(entry.mobile)
        wd.find_element('name', "email").click()
        wd.find_element('name', "email").clear()
        wd.find_element('name', "email").send_keys(entry.email)
        wd.find_element('name', "email2").click()
        wd.find_element('name', "email2").clear()
        wd.find_element('name', "email2").send_keys(entry.email2)
        wd.find_element('name', "bday").click()
        Select(wd.find_element('name', "bday")).select_by_visible_text(entry.bday)
        wd.find_element('name', "bmonth").click()
        wd.find_element('name', "bmonth").click()
        Select(wd.find_element('name', "bmonth")).select_by_visible_text(entry.bmonth)
        wd.find_element('name', "byear").click()
        wd.find_element('name', "byear").clear()
        wd.find_element('name', "byear").send_keys(entry.byear)
        wd.find_element('name', "aday").click()
        Select(wd.find_element('name', "aday")).select_by_visible_text(entry.aday)
        wd.find_element('name', "amonth").click()
        Select(wd.find_element('name', "amonth")).select_by_visible_text(entry.amonth)
        wd.find_element('name', "ayear").click()
        wd.find_element('name', "ayear").clear()
        wd.find_element('name', "ayear").send_keys(entry.ayear)
        # submit entry creation
        wd.find_element('xpath', "//input[20]").click()
        self.return_to_the_entry_list()

    def return_to_the_entry_list(self):
        wd = self.wd
        wd.find_element('id', "logo").click()

    def logout(self):
        wd = self.wd
        wd.find_element('link text', "Logout").click()

    def destroy(self):
        self.wd.quit()
