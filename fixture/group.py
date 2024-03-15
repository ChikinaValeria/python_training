from selenium.webdriver.common.by import By
from model.group import Group

class Group_helper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements('name', 'new')) > 0):
            wd.find_element('link text', "groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element('link text', "group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element('name', "new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element('name', "submit").click()
        self.return_to_groups_page()
        # сброс кэша, который стал невалиден после создания нового объекта
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element('name', field_name).click()
            wd.find_element('name', field_name).clear()
            wd.find_element('name', field_name).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_first_group_oldstyle(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element('name', "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements('name', "selected[]")[index].click()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #submit deletion
        wd.find_element('name', "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        #submit deletion
        wd.find_element('name', "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self):
        wd = self.app.wd
        self.edit_group_by_index(0)


    def edit_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        wd.find_element('name', "edit").click()
        # refill group form
        self.fill_group_form(new_group_data)
        # submit edition
        wd.find_element('name', "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element('name', "edit").click()
        # refill group form
        self.fill_group_form(new_group_data)
        # submit edition
        wd.find_element('name', "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element('name', "selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements('name', "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache =[]
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                #text = element.find_element('name', "selected[]").get_attribute("title")
                text = element.text
                id = element.find_element('name', "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))

        #print(self.group_cache)
        return list(self.group_cache)

    def get_id_by_name(self, name):
        wd = self.app.wd
        self.open_groups_page()
        for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
            text = element.text
            if text == name:
                id = element.find_element('name', "selected[]").get_attribute("value")

        return id



