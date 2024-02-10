from sys import maxsize
class Entry:
    def __init__(self, firstname=None, lastname=None, address=None, home=None, mobile=None, work=None,
                 email=None, email2=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, id = None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.email = email
        self.email2 = email2
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id


    def __repr__(self):
        return "Entry(%s, %s, %s, %s, %s, %s)" % (self.firstname, self.lastname, self.id, self.home, self.mobile, self.work)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize