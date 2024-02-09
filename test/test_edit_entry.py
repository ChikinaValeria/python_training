from model.entry import Entry
from random import randrange

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


def test_edit_firstname_by_index(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = app.entry.get_entry_list()
    #print('Old entries ', old_entries)
    index = randrange(len(old_entries))
    #print(index)
    print(old_entries[index])
    entry = Entry (firstname="Олег")
    entry.id = old_entries[index].id
    entry.lastname = old_entries[index].lastname
    #print(entry)
    app.entry.edit_entry_by_index(index, entry)
    assert len(old_entries) == app.entry.count()
    new_entries = app.entry.get_entry_list()
    #print(new_entries)
    old_entries[index] = entry
    #print('Old entries ', old_entries)
    #print('Old entries sorted', sorted(old_entries, key=Entry.id_or_max))
    #print('New entries ', new_entries)
    #print('New entries sorted ', sorted(new_entries, key=Entry.id_or_max))
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)


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


