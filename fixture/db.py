import pymysql.cursors
from model.group import Group
from model.entry import Entry

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # autocommit=True для сброса кэша после каждого запроса
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()


    def get_entry_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select firstname, lastname, id, address, home, mobile, work, email, email2, email3 from addressbook where deprecated is NULL")
            for row in cursor:
                (firstname, lastname, id, address, home, mobile, work, email, email2, email3) = row
                list.append(Entry(firstname=firstname, lastname=lastname, id=str(id), address = address,
                                  home = home, mobile=mobile, work=work, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_entry_in_group(self, chosen_group_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id from address_in_groups where group_id = chosen_group_id")


        finally:
            cursor.close()
        return str(id)

    def get_entries_in_group(self, id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id from address_in_groups where group_id = id")
            for row in cursor:
                (id) = row
                list.append(Entry(id=str(id)))
                print(list)
        finally:
            cursor.close()
        return list


    """def get_entries_in_group(self, id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id from address_in_groups where group_id = id")
            for row in cursor:
                id = row
                list.append(id)
                print(list)
        finally:
            cursor.close()
        return list"""

