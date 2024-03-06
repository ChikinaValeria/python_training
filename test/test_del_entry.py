from model.entry import Entry
import random
def test_delete_some_entry(app, db, check_ui):
    if len(db.get_entry_list()) == 0:
        app.entry.create(Entry(firstname='test'))
    old_entries = db.get_entry_list()
    entry = random.choice(old_entries)
    app.entry.delete_entry_by_id(entry.id)
    new_entries = db.get_entry_list()
    assert len(old_entries) - 1 == app.entry.count()
    old_entries.remove(entry)
    assert old_entries == new_entries
    if check_ui:
        assert sorted(new_entries, key=Entry.id_or_max) == sorted(app.entry.get_entry_list(), key=Entry.id_or_max)


