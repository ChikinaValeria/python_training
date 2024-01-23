from model.entry import Entry

def test_edit_entry(app):
    app.session.login(username = "admin", password = "secret")
    app.entry.edit(Entry (firstname="Николай", lastname="Павловский", address="Russia, Omsk",
                               home="987654321", mobile="8 921 921 92 92", email="Ppavel@gmail.com",
                               email2="Lpavel1@gmail.com", byear="1985", ayear="1985", bmonth="May",
                               aday="16", bday="1", amonth="October"))
    app.session.logout()
