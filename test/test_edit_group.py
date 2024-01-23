from model.group import Group

def test_edit_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.edit(Group (name ="Отредактированная группа", header ="Отредактированный заголовок", footer ="Дополненный комментарий"))
    app.session.logout()


