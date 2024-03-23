from model.group import Group
from model.entry import Entry
import random
from fixture.orm import ORMFixture
from generator.group import random_string
from fixture.entry import Entry_helper

new_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_delete_entry_from_group(app, db):
    if len(db.get_group_list()) == 0:
        name = random_string('test_group', 15)
        app.group.create(Group(name=name))
    if len(db.get_entry_list()) == 0:
        app.entry.create(Entry(firstname='test_name'))
    # ищем группу, в которую включен хотя бы один контакт или создаем такую
    id, entry, selected_group = app.group.find_or_create_group_with_atleast_one_contact(db, new_db, app)
    #удаляем контакт из группы
    app.entry.delete_entry_from_group(id, selected_group.id)
    assert entry not in new_db.get_entries_in_group(selected_group)

