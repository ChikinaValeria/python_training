# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest
from selenium.webdriver.support.select import Select
from entry import Entry
class TestAddEntry(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def login(self, wd, password, username):
        wd.find_element('name', "user").click()
        wd.find_element('name', "user").clear()
        wd.find_element('name', "user").send_keys(username)
        wd.find_element('name', "pass").click()
        wd.find_element('name', "pass").clear()
        wd.find_element('name', "pass").send_keys(password)
        wd.find_element('xpath', "//input[@value='Login']").click()


    def create_entry(self, wd, entry):
        #init entry creation
        wd.find_element('link text', "add new").click()
        #fill entry form
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
        #submit entry creation
        wd.find_element('xpath', "//input[20]").click()

    def return_to_the_entry_list(self, wd):
        wd.find_element('id', "logo").click()

    def logout(self, wd):
        wd.find_element('link text', "Logout").click()

    def test_add_entry(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, password = "secret", username = "admin")
        self.create_entry(wd, Entry(firstname="Павел", lastname="Петровский", address="Russia, Saint-Petersburg",
                          home="1234578", mobile="8 921 921 92 92", email="pavel@gmail.com", email2="pavel1@gmail.com",
                          byear="1985", ayear="1985", bmonth="May", aday="16", bday="1", amonth="October"))
        self.return_to_the_entry_list(wd)
        self.logout(wd)


    def test_add_almost_empty_entry(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, password = "secret", username = "admin")
        self.create_entry(wd, Entry(firstname="", lastname="", address="",
                          home="", mobile="", email="", email2="",
                          byear="", ayear="", bmonth="-", aday="", bday="", amonth="-"))
        self.return_to_the_entry_list(wd)
        self.logout(wd)



    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
