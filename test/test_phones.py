
import re

def test_phones_on_home_page(app):
    entry_from_home_page = app.entry.get_entry_list()[0]
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(0)

    assert entry_from_home_page.home == clear(entry_from_edit_page.home)
    assert entry_from_home_page.mobile == clear(entry_from_edit_page.mobile)
    assert entry_from_home_page.work == clear(entry_from_edit_page.work)

def test_phones_on_entry_view_page(app):
    entry_from_view_page = app.entry.get_entry_from_view_page(0)
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(0)

    assert entry_from_view_page.home == entry_from_edit_page.home
    assert entry_from_view_page.mobile == entry_from_edit_page.mobile
    assert entry_from_view_page.work == entry_from_edit_page.work
def clear(s):
    return re.sub("[() -]", "", s)
