from pony.orm import *
from datetime import datetime
from model.group import Group
from model.entry import Entry
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column ='group_id')
        name = Optional(str, column = 'group_name')
        header = Optional(str, column = 'group_header')
        footer = Optional(str, column = 'group_footer')

    class ORMEntry(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column = 'id')
        firstname = Optional(str, column = 'firstname')
        lastname = Optional(str, column = 'lastname')
        #deprecated = Optional(datetime, column = 'deprecated')


    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
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
            return Entry(id=str(entry.id), firstname=entry.firstname, lastname=entry.lastname)
        return list(map(convert, entries))
