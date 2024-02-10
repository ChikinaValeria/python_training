# -*- coding: utf-8 -*-

from model.entry import Entry



def test_add_entry(app):
    old_entries = app.entry.get_entry_list()
    entry = Entry(firstname="Иван", lastname="Цветков", address="Russia, Saint-Petersburg",
                           home="1234578", mobile="8 921 921 92 92", work ="987456", email="pavel@gmail.com",
                           email2="pavel1@gmail.com", byear="1985", ayear="1985", bmonth="May",
                           aday="16", bday="1", amonth="October")
    app.entry.create(entry)
    assert len(old_entries) + 1 == app.entry.count()
    new_entries = app.entry.get_entry_list()
    old_entries.append(entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)


"""def test_add_almost_empty_entry(app):
    old_entries = app.entry.get_entry_list()
    entry = Entry(firstname="", lastname= "", address="",
                           home="", mobile="", work="", email="", email2="",
                           byear="", ayear="", bmonth="-", aday="",
                           bday="", amonth="-")
    app.entry.create(entry)
    assert len(old_entries) + 1 == app.entry.count()
    new_entries = app.entry.get_entry_list()
    old_entries.append(entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)"""




