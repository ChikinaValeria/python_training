from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from model.entry import Entry
class Entry_helper:

    def __init__(self, app):
        self.app = app

    def open_the_entry_list(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements('name', 'add')) > 0):
            wd.find_element('link text', "home").click()

    def return_to_the_entry_list(self):
        wd = self.app.wd
        # wd.find_element('id', "logo").click()
        wd.find_element('link text', "home page").click()

    def create(self, entry):
        wd = self.app.wd
        self.open_the_entry_list()
        # init entry creation
        wd.find_element('link text', "add new").click()
        self.fill_entry_form(entry)
        # submit entry creation
        wd.find_element('xpath', "//input[20]").click()
        self.return_to_the_entry_list()
        self.entry_cache = None

    def fill_entry_form(self, entry):
        wd = self.app.wd
        self.change_field("firstname", entry.firstname)
        self.change_field("lastname", entry.lastname)
        self.change_field("address", entry.address)
        self.change_field("home", entry.home)
        self.change_field("mobile", entry.mobile)
        self.change_field("email", entry.email)
        self.change_field("email2", entry.email2)
        self.change_drop_list_option("bday", entry.bday)
        self.change_drop_list_option("bmonth", entry.bmonth)
        self.change_field("byear", entry.byear)
        self.change_drop_list_option("aday", entry.aday)
        self.change_drop_list_option("amonth", entry.amonth)
        self.change_field("ayear", entry.ayear)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element('name', field_name).click()
            wd.find_element('name', field_name).clear()
            wd.find_element('name', field_name).send_keys(text)

    def change_drop_list_option(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element('name', field_name).click()
            Select(wd.find_element('name', field_name)).select_by_visible_text(text)


    def delete_first_entry(self):
        wd = self.app.wd
        self.open_the_entry_list()
        # select first entry
        self.select_first_entry()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        time.sleep(3)
        self.entry_cache = None

    def edit_first_entry(self, new_entry_data):
        wd = self.app.wd
        self.open_the_entry_list()
        # select first entry
        self.select_first_entry()
        wd.find_element(By.XPATH, "// img[ @ alt = 'Edit']").click()
        self.fill_entry_form(new_entry_data)
        wd.find_element('name', "update").click()
        self.return_to_the_entry_list()
        self.entry_cache = None

    def select_first_entry(self):
        wd = self.app.wd
        wd.find_element('name', "selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_the_entry_list()
        return len(wd.find_elements('name', "selected[]"))

    entry_cache = None

    def get_entry_list(self):
        if self.entry_cache is None:
            wd = self.app.wd
            self.open_the_entry_list()
            self.entry_cache = []
            for element in wd.find_elements('name', "entry"):
                firstname = element.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
                lastname = element.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                id = element.find_element('name', "selected[]").get_attribute("value")
                self.entry_cache.append(Entry(firstname = firstname, lastname=lastname, id=id))
        #print(self.entry_cache)
        return list(self.entry_cache)