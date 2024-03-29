from sys import maxsize
class Entry:
    def __init__(self, firstname=None, lastname=None, nickname = None, address=None, home=None, mobile=None, work=None,
                 all_phones_from_home_page = None, all_emails_from_home_page = None,
                 email=None, email2=None, email3 = None, bday=None, bmonth=None, byear=None, aday=None,
                 amonth=None, ayear=None, id = None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id


    def __repr__(self):
        return "Entry(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (self.firstname, self.lastname, self.nickname, self.id, self.address, self.home, self.mobile,
                                                  self.work, self.email, self.email2, self.email3, self.bday, self.bmonth, self.byear, self.aday, self.amonth, self.ayear,
                                                  self.all_phones_from_home_page, self.all_emails_from_home_page)

    def __eq__(self, other):
        return (self.firstname == other.firstname and self.lastname == other.lastname and
                (self.id is None or other.id is None or self.id == other.id)
                and self.address == other.address)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize