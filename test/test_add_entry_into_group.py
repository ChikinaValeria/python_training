from model.group import Group
from model.entry import Entry
from fixture.orm import ORMFixture

new_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_entry_into_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test_group'))
    if len(db.get_entry_list()) == 0:
        app.entry.create(Entry(firstname='test_name'))
    #находим подходящую существующую группу или создаем новую
    entry, id, selected_group = app.group.find_or_create_group_not_containing_all_entries(db, new_db)
    #добавляем контакт в группу
    app.entry.add_entry_into_group(id, selected_group.name)
    assert entry in new_db.get_entries_in_group(selected_group)




    """edited_entry = Entry (firstname="Lilit", lastname=lastname, id=id)
    app.entry.edit_entry_by_id(id, edited_entry)
    #assert len(old_entries) == app.entry.count()
    new_entries = db.get_entry_list()
    for index in range(len(old_entries)):
        if old_entries[index].id == id:
            old_entries[index] = edited_entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)"""

