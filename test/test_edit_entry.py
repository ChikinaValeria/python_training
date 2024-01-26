from model.entry import Entry

def test_edit_first_entry_all_fields(app):
    app.entry.edit_first_entry(Entry (firstname="Иммануил", lastname="Павловский", address="Russia, Nahodka",
                               home="987654321", mobile="8 921 921 92 92", email="Ppavel@gmail.com",
                               email2="Lpavel1@gmail.com", byear="1985", ayear="1985", bmonth="May",
                               aday="16", bday="1", amonth="October"))


def test_edit_first_entry_firstname(app):
    app.entry.edit_first_entry(Entry (firstname="Афанасий"))

def test_edit_first_entry_home(app):
    app.entry.edit_first_entry(Entry (home="1111111"))

def test_edit_first_entry_bmonth(app):
    app.entry.edit_first_entry(Entry (bmonth="April"))

