# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd):
        wd.find_element('name', "user").clear()
        wd.find_element('name', "user").send_keys("admin")
        wd.find_element('name', "pass").click()
        wd.find_element('name', "pass").clear()
        wd.find_element('name', "pass").send_keys("secret")
        wd.find_element('xpath', "//input[@value='Login']").click()

    def open_groups_page(self, wd):
        wd.find_element('link text', "groups").click()

    def create_group(self, wd):
        # init group creation
        wd.find_element('name', "new").click()
        # fill group form
        wd.find_element('name', "group_name").click()
        wd.find_element('name', "group_name").clear()
        wd.find_element('name', "group_name").send_keys("Моя первая группа")
        wd.find_element('name', "group_header").click()
        wd.find_element('name', "group_header").clear()
        wd.find_element('name', "group_header").send_keys("Хорошая группа")
        wd.find_element('name', "group_footer").click()
        wd.find_element('name', "group_footer").clear()
        wd.find_element('name', "group_footer").send_keys("Нужная группа")
        # submit group creation
        wd.find_element('name', "submit").click()

    def return_to_groups_page(self, wd):
        wd.find_element('link text', "group page").click()

    def logout(self, wd):
        wd.find_element('link text', "Logout").click()

    def test_add_group(self):
        #success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)
        #self.assertTrue(success)

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
