

def test_delete_first_entry(app):
    app.session.login(password="secret", username="admin")
    app.entry.delete_first_entry()
    app.session.logout()