from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
class Entry_helper:

    def __init__(self, app):
        self.app = app

    def create(self, entry):
        wd = self.app.wd
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
        wd = self.app.wd
        # wd.find_element('id', "logo").click()
        wd.find_element('link text', "home page").click()

    def delete_first_entry(self):
        wd = self.app.wd
        # select first entry
        wd.find_element('name', "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        time.sleep(3)

    def edit(self, entry):
        wd = self.app.wd
        # select first entry
        wd.find_element('name', "selected[]").click()
        wd.find_element(By.XPATH, "// img[ @ alt = 'Edit']").click()
        # refill entry form
        wd.find_element('name', "firstname").click()
        wd.find_element('name', "firstname").clear()
        wd.find_element('name', "firstname").send_keys(entry.firstname)
        #wd.find_element('name', "lastname").click()
        ##wd.find_element('name', "lastname").clear()
        #wd.find_element('name', "lastname").send_keys(entry.lastname)
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
        #wd.find_element('name', "bday").click()
        #Select(wd.find_element('name', "bday")).select_by_visible_text(entry.bday)
        #wd.find_element('name', "bmonth").click()
        #wd.find_element('name', "bmonth").click()
        #Select(wd.find_element('name', "bmonth")).select_by_visible_text(entry.bmonth)
        #wd.find_element('name', "byear").click()
        #wd.find_element('name', "byear").clear()
        #wd.find_element('name', "byear").send_keys(entry.byear)
        #wd.find_element('name', "aday").click()
        #Select(wd.find_element('name', "aday")).select_by_visible_text(entry.aday)
        #wd.find_element('name', "amonth").click()
        #Select(wd.find_element('name', "amonth")).select_by_visible_text(entry.amonth)
        #wd.find_element('name', "ayear").click()
        #wd.find_element('name', "ayear").clear()
        #wd.find_element('name', "ayear").send_keys(entry.ayear)
        # submit edition
        wd.find_element('name', "update").click()
        self.return_to_the_entry_list()

