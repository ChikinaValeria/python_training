from pony.orm import *
from datetime import datetime
from model.group import Group
from model.entry import Entry


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column ='group_id')
        name = Optional(str, column = 'group_name')
        header = Optional(str, column = 'group_header')
        footer = Optional(str, column = 'group_footer')
        entries = Set(lambda: ORMFixture.ORMEntry, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMEntry(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column = 'id')
        firstname = Optional(str, column = 'firstname')
        lastname = Optional(str, column = 'lastname')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        work = Optional(str, column='work')
        mobile = Optional(str, column='mobile')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        #deprecated = Optional(datetime, column = 'deprecated')
        groups= Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="entries", lazy=True)


    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))


    @db_session
    def get_entry_list(self):
        return self.convert_entries_to_model(select(c for c in ORMFixture.ORMEntry))

    def convert_entries_to_model(self, entries):
        def convert(entry):
            return Entry(id=str(entry.id), firstname=entry.firstname, lastname=entry.lastname, address=entry.address,
                         home=entry.home, work=entry.work, mobile=entry.mobile,
                         email=entry.email, email2=entry.email2, email3=entry.email3
                         )
        return list(map(convert, entries))


    @db_session
    def get_entries_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_entries_to_model(orm_group.entries)

    @db_session
    def get_entries_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_entries_to_model(
        select(c for c in ORMFixture.ORMEntry if orm_group not in c.groups))

