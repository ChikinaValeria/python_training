from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from model.entry import Entry
import re
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
        self.change_field("nickname", entry.nickname)
        self.change_field("address", entry.address)
        self.change_field("home", entry.home)
        self.change_field("mobile", entry.mobile)
        self.change_field("work", entry.work)
        self.change_field("email", entry.email)
        self.change_field("email2", entry.email2)
        self.change_field("email3", entry.email3)
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


    def delete_first_entry_oldstyle(self):
        wd = self.app.wd
        self.open_the_entry_list()
        # select first entry
        self.select_first_entry()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        time.sleep(3)
        self.entry_cache = None

    def delete_first_entry(self):
        wd = self.app.wd
        self.delete_entry_by_index(0)

    def delete_entry_by_index(self,index):
        wd = self.app.wd
        self.open_the_entry_list()
        # select first entry
        self.select_entry_by_index(index)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        time.sleep(3)
        self.entry_cache = None

    def delete_entry_by_id(self,id):
        wd = self.app.wd
        self.open_the_entry_list()
        # select first entry
        self.select_entry_by_id(id)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        time.sleep(3)
        self.entry_cache = None

    def edit_first_entry(self, new_entry_data):
        wd = self.app.wd
        self.edit_entry_by_index(0)

    def edit_entry_by_id(self, id, new_entry_data):
        wd = self.app.wd
        self.open_the_entry_list()
        # select first entry
        self.select_entry_by_id(id)
        wd.find_element(By.XPATH, "// img[ @ alt = 'Edit']").click()
        self.fill_entry_form(new_entry_data)
        wd.find_element('name', "update").click()
        self.return_to_the_entry_list()
        self.entry_cache = None

    def edit_entry_by_index(self, index, new_entry_data):
        wd = self.app.wd
        self.open_the_entry_list()
        # select first entry
        self.select_entry_by_index(index)
        wd.find_elements(By.XPATH, "// img[ @ alt = 'Edit']")[index].click()
        self.fill_entry_form(new_entry_data)
        wd.find_element('name', "update").click()
        self.return_to_the_entry_list()
        self.entry_cache = None


    def edit_first_entry_oldstyle(self, new_entry_data):
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
        wd.find_elements('name', "selected[]")[0].click()

    def select_entry_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_entry_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[id='%s']" % id).click()

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
            for row in wd.find_elements('name', "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                address = cells[3].text
                #firstname = element.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
                #lastname = element.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
                #id = element.find_element('name', "selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.entry_cache.append(Entry(firstname = firstname, lastname=lastname, id=id, address = address,
                                              all_phones_from_home_page = all_phones, all_emails_from_home_page = all_emails))

        #print(self.entry_cache)
        return list(self.entry_cache)

    def open_entry_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_the_entry_list()
        row = wd.find_elements('name', "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_entry_view_by_index(self, index):
        wd = self.app.wd
        self.open_the_entry_list()
        row = wd.find_elements('name', "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_entry_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_entry_to_edit_by_index(index)
        firstname = wd.find_element('name', "firstname").get_attribute("value")
        lastname = wd.find_element('name', "lastname").get_attribute("value")
        address = wd.find_element('name', "address").get_attribute("value")
        id = wd.find_element('name', "id").get_attribute("value")
        home = wd.find_element('name', "home").get_attribute("value").replace(' ', '')
        mobile = wd.find_element('name', "mobile").get_attribute("value").replace(' ', '')
        work = wd.find_element('name', "work").get_attribute("value").replace(' ', '')
        email = wd.find_element('name', "email").get_attribute("value")
        email2 = wd.find_element('name', "email2").get_attribute("value")
        email3 = wd.find_element('name', "email3").get_attribute("value")
        return Entry(firstname=firstname, lastname=lastname, address= address, id=id,
                     home=home, mobile=mobile, work=work, email=email, email2=email2, email3=email3)


    def get_entry_from_view_page(self, index):
        wd = self.app.wd
        self.open_entry_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home = re.search("H: (.*)", text).group(1).replace(' ', '')
        mobile = re.search("M: (.*)", text).group(1).replace(' ', '')
        work = re.search("W: (.*)", text).group(1).replace(' ', '')
        return Entry(home=home, mobile=mobile, work=work)

