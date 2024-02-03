from model.entry import Entry

def test_edit_first_entry_all_fields(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = app.entry.get_entry_list()
    app.entry.edit_first_entry(Entry (firstname="Иммануил", lastname="Павловский", address="Russia, Nahodka",
                               home="987654321", mobile="8 921 921 92 92", email="Ppavel@gmail.com",
                               email2="Lpavel1@gmail.com", byear="1985", ayear="1985", bmonth="May",
                               aday="16", bday="1", amonth="October"))
    new_entries = app.entry.get_entry_list()
    assert len(old_entries) == len(new_entries)


def test_edit_first_entry_firstname(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = app.entry.get_entry_list()
    app.entry.edit_first_entry(Entry (firstname="Афанасий"))
    new_entries = app.entry.get_entry_list()
    assert len(old_entries) == len(new_entries)

def test_edit_first_entry_home(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = app.entry.get_entry_list()
    app.entry.edit_first_entry(Entry (home="1111111"))
    new_entries = app.entry.get_entry_list()
    assert len(old_entries) == len(new_entries)

def test_edit_first_entry_bmonth(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = app.entry.get_entry_list()
    app.entry.edit_first_entry(Entry (bmonth="April"))
    new_entries = app.entry.get_entry_list()
    assert len(old_entries) == len(new_entries)


