# -*- coding: utf-8 -*-

from model.entry import Entry



def test_add_entry(app):
    app.entry.create(Entry(firstname="Павел", lastname="Петровский", address="Russia, Saint-Petersburg",
                           home="1234578", mobile="8 921 921 92 92", email="pavel@gmail.com",
                           email2="pavel1@gmail.com", byear="1985", ayear="1985", bmonth="May",
                           aday="16", bday="1", amonth="October"))



def test_add_almost_empty_entry(app):
    app.entry.create(Entry(firstname="", lastname="", address="",
                           home="", mobile="", email="", email2="",
                           byear="", ayear="", bmonth="-", aday="",
                           bday="", amonth="-"))




