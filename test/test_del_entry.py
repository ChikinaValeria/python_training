from model.entry import Entry

def test_delete_first_entry(app):
    if app.entry.count() == 0:
        app.entry.create(Entry(firstname='test'))
    app.entry.delete_first_entry()
