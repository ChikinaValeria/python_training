from model.entry import Entry
import random

"""def test_edit_first_entry_all_fields(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = app.entry.get_entry_list()
    app.entry.edit_first_entry(Entry (firstname="Иммануил", lastname="Павловский", address="Russia, Nahodka",
                               home="987654321", mobile="8 921 921 92 92", work="721 92 92", email="Ppavel@gmail.com",
                               email2="Lpavel1@gmail.com", byear="1985", ayear="1985", bmonth="May",
                               aday="16", bday="1", amonth="October"))
    assert len(old_entries) == app.entry.count()
    new_entries = app.entry.get_entry_list()"""


def test_edit_firstname_by_id(app, db, check_ui):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = db.get_entry_list()
    #print('Old entries ', old_entries)
    entry = random.choice(old_entries)
    id = entry.id
    lastname = entry.lastname
    edited_entry = Entry (firstname="Lilit", lastname=lastname, id=id)
    app.entry.edit_entry_by_id(id, edited_entry)
    #assert len(old_entries) == app.entry.count()
    new_entries = db.get_entry_list()
    for index in range(len(old_entries)):
        if old_entries[index].id == id:
            old_entries[index] = edited_entry
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)
    if check_ui:
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_entry_list(), key=Entry.id_or_max)





"""def test_edit_first_entry_home(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = app.entry.get_entry_list()
    app.entry.edit_first_entry(Entry (home="1111111"))
    assert len(old_entries) == app.entry.count()
    new_entries = app.entry.get_entry_list()

def test_edit_first_entry_bmonth(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = app.entry.get_entry_list()
    app.entry.edit_first_entry(Entry (bmonth="April"))
    assert len(old_entries) == app.entry.count()
    new_entries = app.entry.get_entry_list()"""


