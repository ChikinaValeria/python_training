# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest
from selenium.webdriver.support.select import Select

class TestAddEntry(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def login(self, wd):
        wd.find_element('name', "user").click()
        wd.find_element('name', "user").clear()
        wd.find_element('name', "user").send_keys("admin")
        wd.find_element('name', "pass").click()
        wd.find_element('name', "pass").clear()
        wd.find_element('name', "pass").send_keys("secret")
        wd.find_element('xpath', "//input[@value='Login']").click()

    def test_add_entry(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        wd.find_element('link text', "add new").click()
        wd.find_element('name',"firstname").click()
        wd.find_element('name',"firstname").clear()
        wd.find_element('name',"firstname").send_keys(u"Павел")
        wd.find_element('name',"middlename").click()
        wd.find_element('name',"middlename").clear()
        wd.find_element('name',"middlename").send_keys(u"Арсений")
        wd.find_element('name',"lastname").click()
        wd.find_element('name',"lastname").clear()
        wd.find_element('name',"lastname").send_keys(u"Петровский")
        wd.find_element('name', "title").click()
        wd.find_element('name', "title").clear()
        wd.find_element('name', "title").send_keys("QA engineer")
        wd.find_element('name', "company").click()
        wd.find_element('name', "company").clear()
        wd.find_element('name', "company").send_keys("Epam")
        wd.find_element('name', "address").click()
        wd.find_element('name', "address").clear()
        wd.find_element('name', "address").send_keys("Russia, Saint-Petersburg")
        wd.find_element('name', "home").click()
        wd.find_element('name', "home").clear()
        wd.find_element('name', "home").send_keys("1234578")
        wd.find_element('name', "mobile").click()
        wd.find_element('name', "mobile").clear()
        wd.find_element('name', "mobile").send_keys("8 921 921 92 92")
        wd.find_element('name', "email").click()
        wd.find_element('name', "email").clear()
        wd.find_element('name', "email").send_keys("pavel@gmail.com")
        wd.find_element('name', "homepage").click()
        wd.find_element('name', "homepage").clear()
        wd.find_element('name', "homepage").send_keys("pavel.com")
        wd.find_element('name', "email2").click()
        wd.find_element('name', "email2").clear()
        wd.find_element('name', "email2").send_keys("pavel1@gmail.com")
        wd.find_element('name', "bday").click()
        Select(wd.find_element('name', "bday")).select_by_visible_text("1")
        wd.find_element('xpath', "//option[@value='1']").click()
        wd.find_element('name', "bmonth").click()
        wd.find_element('xpath', "//option[@value='-']").click()
        wd.find_element('name', "bmonth").click()
        Select(wd.find_element('name', "bmonth")).select_by_visible_text("May")
        wd.find_element('xpath', "//option[@value='May']").click()
        wd.find_element('name', "byear").click()
        wd.find_element('name', "byear").clear()
        wd.find_element('name', "byear").send_keys("1985")
        wd.find_element('name', "aday").click()
        Select(wd.find_element('name', "aday")).select_by_visible_text("16")
        wd.find_element('xpath', "//div[@id='content']/form/select[3]/option[18]").click()
        wd.find_element('name', "amonth").click()
        Select(wd.find_element('name', "amonth")).select_by_visible_text("October")
        wd.find_element('xpath', "//div[@id='content']/form/select[4]/option[11]").click()
        wd.find_element('name', "ayear").click()
        wd.find_element('name', "ayear").clear()
        wd.find_element('name', "ayear").send_keys("1985")
        wd.find_element('xpath', "//input[20]").click()
        wd.find_element('id', "logo").click()
        wd.find_element('link text', "Logout").click()



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
