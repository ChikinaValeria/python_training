from model.group import Group
from model.entry import Entry
import random
from fixture.orm import ORMFixture
from generator.group import random_string

new_db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_delete_entry_from_group(app, db):
    if len(db.get_group_list()) == 0:
        name = random_string('test_group', 15)
        app.group.create(Group(name=name))
    if len(db.get_entry_list()) == 0:
        app.entry.create(Entry(firstname='test_name'))
    # ищем группу, в которую включен хотя бы один контакт
    groups = db.get_group_list()
    flag = False
    for g in groups:
        entries_in = new_db.get_entries_in_group(g)
        if len(entries_in) != 0:
            entry = random.choice(entries_in)
            id = entry.id
            selected_group = g
            flag = True
            break
        else:
            continue
    # если после перебора всех групп подходящая группа все еще не выбрана,
    # выбираем случайную группу, сохраняем имя
    if flag == False:
        groups = app.group.get_group_list()
        selected_group = random.choice(groups)
        group_id = selected_group.id
        # выбираем случайный контакт
        entries = db.get_entry_list()
        entry = random.choice(entries)
        id = entry.id
        #добавляем случайный контакт в новую группу
        app.entry.add_entry_into_group(id, selected_group.name)
    #удаляем контакт из группы
    app.entry.delete_entry_from_group(id, selected_group.name)
    assert entry not in new_db.get_entries_in_group(selected_group)

