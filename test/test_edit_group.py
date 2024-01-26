from model.group import Group

def test_edit_first_group_all_fields(app):
    app.group.edit_first_group(Group (name ="Отредактированная группа", header ="Отредактированный заголовок", footer ="Дополненный комментарий"))



def test_edit_first_group_name(app):
    app.group.edit_first_group(Group (name ="New name"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group (header ="New header"))



def test_edit_first_group_all_footer(app):
    app.group.edit_first_group(Group (footer ="New footer"))


