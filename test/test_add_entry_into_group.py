from model.group import Group
from model.entry import Entry
import random




def test_add_entry_into_group(app, db):
    #убеждаемся, что есть контакт и группа
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    if len(db.get_group_list()) == 0:
            app.group.create(Group(name='test'))


    #выбираем случайный контакт и сохраняем ид
    entries = app.entry.get_entry_list()
    entry = random.choice(entries)
    print(entry)
    id = str(entry.id)
    print(id)
    #выбираем случайную группу и сохраняем имя и ид
    groups = app.group.get_group_list()
    group = random.choice(groups)
    group_name = group.name
    print(group_name)
    group_id = group.id
    print(group_id)
    #добавляем контакт в группу
    app.entry.open_the_entry_list()
    app.entry.select_entry_by_id(id)
    app.entry.add_into_group(group_name)
    #print(db.get_entries_in_group(group_id))
    #assert id in db.get_entries_in_group(group_id)
    print(db.get_entry_in_group(group))
    assert id == db.get_entry_in_group(group)
    #не могу получить доступ к орм
    #assert entry in app.orm.get_entries_in_group(group)




    """edited_entry = Entry (firstname="Lilit", lastname=lastname, id=id)
    app.entry.edit_entry_by_id(id, edited_entry)
    #assert len(old_entries) == app.entry.count()
    new_entries = db.get_entry_list()
    for index in range(len(old_entries)):
        if old_entries[index].id == id:
            old_entries[index] = edited_entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)"""

