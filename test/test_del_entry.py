from model.entry import Entry

def test_delete_first_entry(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = app.entry.get_entry_list()
    app.entry.delete_first_entry()
    new_entries = app.entry.get_entry_list()
    assert len(old_entries) - 1 == len(new_entries)
    old_entries[0:1] = []
    assert old_entries == new_entries
