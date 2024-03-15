from model.group import Group
from model.entry import Entry
import random
from fixture.orm import ORMFixture
from generator.group import random_string

new_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_entry_into_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test_group'))
    if len(db.get_entry_list()) == 0:
        app.entry.create(Entry(firstname='test_name'))
    #ищем группу, в которую включены не все контакты
    groups = db.get_group_list()
    flag = False
    for g in groups:
        entries_out = new_db.get_entries_not_in_group(g)
        if len(entries_out) != 0:
            entry = random.choice(entries_out)
            id = entry.id
            selected_group = g
            flag = True
            break
        else:
            continue
    #если после перебора всех групп подходящая группа все еще не выбрана,
    #создаем новую группу и запоминаем ее
    if flag == False:
        name = random_string('test_group', 15)
        selected_group = Group(name=name)
        app.group.create(selected_group)
        selected_group.id = app.group.get_id_by_name(name)
        # выбираем случайный контакт и сохраняем ид
        entries = db.get_entry_list()
        entry = random.choice(entries)
        id= entry.id
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

