
import re
import random

"""def test_phones_on_home_page(app):
    entry_from_home_page = app.entry.get_entry_list()[0]
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(0)

    assert entry_from_home_page.home == clear(entry_from_edit_page.home)
    assert entry_from_home_page.mobile == clear(entry_from_edit_page.mobile)
    assert entry_from_home_page.work == clear(entry_from_edit_page.work)"""

"""def test_phones_on_home_page(app):
    entry_from_home_page = app.entry.get_entry_list()[0]
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(0)

    assert entry_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(entry_from_edit_page)"""

def test_random_entry_on_home_page(app):
    random_entry = random.randrange(0, len(app.entry.get_entry_list()))
    entry_from_home_page = app.entry.get_entry_list()[random_entry]
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(random_entry)

    assert entry_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(entry_from_edit_page)
    assert entry_from_home_page.firstname == entry_from_edit_page.firstname
    assert entry_from_home_page.lastname == entry_from_edit_page.lastname
    assert entry_from_home_page.address == entry_from_edit_page.address
    assert entry_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(entry_from_edit_page)



"""def test_phones_on_entry_view_page(app):
    entry_from_view_page = app.entry.get_entry_from_view_page(0)
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(0)

    assert entry_from_view_page.home == entry_from_edit_page.home
    assert entry_from_view_page.mobile == entry_from_edit_page.mobile
    assert entry_from_view_page.work == entry_from_edit_page.work"""

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(entry):
    # удаляем из списка все None
    # используем ламбда-выражение, чтобы не применять clear ко всем элементам списка поотдельности
    # избавляемся от пустых строк с помощью filter
    return "\n".join(filter (lambda x : x != "", (map (lambda x: clear(x),filter (lambda x: x is not None,
                                                                                  [entry.home, entry.mobile, entry.work])))))
