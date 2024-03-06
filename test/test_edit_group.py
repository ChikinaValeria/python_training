from model.group import Group
import random

"""def test_edit_first_group_all_fields(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))

    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group (name ="Отредактированная группа", header ="Отредактированный заголовок", footer ="Дополненный комментарий"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()"""


def test_edit_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    id = group.id
    edited_group = Group (name ="New name", id=id)
    #group.id = old_groups[index].id
    app.group.edit_group_by_id(id, edited_group)
    #assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    for index in range(len(old_groups)):
        if old_groups[index].id == id:
            old_groups[index] = edited_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



"""def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group (header ="New header"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()



def test_edit_first_group_all_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group (footer ="New footer"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()"""


