import re
import random
from model.entry import Entry


"""def test_phones_on_home_page(app):
    entry_from_home_page = app.entry.get_entry_list()[0]
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(0)

    assert entry_from_home_page.home == clear(entry_from_edit_page.home)
    assert entry_from_home_page.mobile == clear(entry_from_edit_page.mobile)
    assert entry_from_home_page.work == clear(entry_from_edit_page.work)"""

def test_phones_on_home_page(app):
    entry_from_home_page = app.entry.get_entry_list()[0]
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(0)

    assert entry_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(entry_from_edit_page)

def test_phones_on_entry_view_page(app):
    entry_from_view_page = app.entry.get_entry_from_view_page(0)
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(0)

    assert entry_from_view_page.home == entry_from_edit_page.home
    assert entry_from_view_page.mobile == entry_from_edit_page.mobile
    assert entry_from_view_page.work == entry_from_edit_page.work

def test_random_entry_on_home_page(app):
    random_entry = random.randrange(0, len(app.entry.get_entry_list()))
    entry_from_home_page = app.entry.get_entry_list()[random_entry]
    entry_from_edit_page = app.entry.get_entry_info_from_edit_page(random_entry)
    print("entry_home", entry_from_home_page)
    print("entry_from_home_page -emails:", entry_from_home_page.all_emails_from_home_page)
    print("entry_edit", entry_from_edit_page)
    print("entry_from_edit_page_merged - emails", merge_emails_like_on_home_page(entry_from_edit_page))


    assert entry_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(entry_from_edit_page)
    assert entry_from_home_page.firstname == entry_from_edit_page.firstname
    assert entry_from_home_page.lastname == entry_from_edit_page.lastname
    assert entry_from_home_page.address == entry_from_edit_page.address
    assert entry_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(entry_from_edit_page)

#сравниваем все контакты с главной страницы с контактами в базе
def test_compare_all_entries_on_home_page_with_db(app, db):
    entries_home = sorted(app.entry.get_entry_list(), key=Entry.id_or_max)
    entries_db = sorted(db.get_entry_list(), key=Entry.id_or_max)
    assert entries_home == entries_db
    #print("Entry_home!!!:", entries_home)
    #print("Entry_db!!!:", entries_db)

    for i in range(len(entries_home)):
        assert entries_home[i].all_phones_from_home_page == merge_phones_like_on_home_page(entries_db[i])
        #print(f'Entry_home_allphines!!! #{i} {entries_home[i].all_phones_from_home_page}')
        #print(f'Entry_db_allphones!!! #{i} {merge_phones_like_on_home_page(entries_db[i])}')
        assert entries_home[i].all_emails_from_home_page == merge_emails_like_on_home_page(entries_db[i])
        #print(f'Entry_home_allphines!!! #{i} {entries_home[i].all_emails_from_home_page}')
        #print(f'Entry_db_allphones!!! #{i} {merge_emails_like_on_home_page(entries_db[i])}')




def merge_phones_like_on_home_page(entry):
    # удаляем из списка все None
    # используем лямбда-выражение, чтобы не применять clear ко всем элементам списка поотдельности
    # избавляемся от пустых строк с помощью filter
    return "\n".join(filter(lambda x: x != "", (map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                                   [entry.home, entry.mobile,
                                                                                    entry.work])))))


def merge_emails_like_on_home_page(entry):
    # удаляем из списка все None
    # используем лямбда-выражение, чтобы не применять clear ко всем элементам списка поотдельности
    # избавляемся от пустых строк с помощью filter
    return "\n".join(filter (lambda x: x != "", (map(lambda x: clear_emails(x), filter(lambda x: x is not None,
                                                                                  [entry.email, entry.email2, entry.email3])))))
def clear_emails(s):
    s = s.strip()
    return re.sub("  ", " ", s)

def clear(s):
    return re.sub("[() -]", "", s)



