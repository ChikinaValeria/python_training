
def test_phones_on_home_page(app):
    entry_from_home_page = app.entry.get_entry_list[0]
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(0)
    assert entry_from_home_page.home == entry_from_edit_page.home
    assert entry_from_home_page.mobile == entry_from_edit_page.mobile
    assert entry_from_home_page.work == entry_from_edit_page.work
