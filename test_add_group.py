# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.firefox.webdriver import WebDriver

import unittest, time, re

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    
    def test_add_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element('name',"user").clear()
        wd.find_element('name',"user").send_keys("admin")
        wd.find_element('name',"pass").click()
        wd.find_element('name',"pass").clear()
        wd.find_element('name',"pass").send_keys("secret")
        wd.find_element('xpath', "//input[@value='Login']").click()
        wd.find_element('link text',"groups").click()
        wd.find_element('name',"new").click()
        wd.find_element('name',"group_name").click()
        wd.find_element('name',"group_name").clear()
        wd.find_element('name',"group_name").send_keys("Моя первая группа")
        wd.find_element('name',"group_header").click()
        wd.find_element('name',"group_header").clear()
        wd.find_element('name',"group_header").send_keys("Хорошая группа")
        wd.find_element('name',"group_footer").click()
        wd.find_element('name',"group_footer").clear()
        wd.find_element('name',"group_footer").send_keys("Нужная группа")
        wd.find_element('name',"submit").click()
        wd.find_element('link text',"group page").click()
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