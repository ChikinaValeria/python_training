# -*- coding: utf-8 -*-
import pytest
from faker import Faker
fake = Faker("ru_RU")
from model.entry import Entry
#from data.entries import constant as testdata

# для загрузки данных из файла json
def test_add_entry(app, json_entries):
    entry = json_entries
    old_entries = app.entry.get_entry_list()
    app.entry.create(entry)
    #print(testdata)
    #print(entry)
    assert len(old_entries) + 1 == app.entry.count()
    new_entries = app.entry.get_entry_list()
    old_entries.append(entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)

"""@pytest.mark.parametrize("entry", testdata, ids=[str(x) for x in testdata])
def test_add_entry(app, entry):
    old_entries = app.entry.get_entry_list()
    app.entry.create(entry)
    #print(testdata)
    #print(entry)
    assert len(old_entries) + 1 == app.entry.count()
    new_entries = app.entry.get_entry_list()
    old_entries.append(entry)
    assert sorted(old_entries, key=Entry.id_or_max) == sorted(new_entries, key=Entry.id_or_max)"""





