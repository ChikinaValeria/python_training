from faker import Faker
fake = Faker("ru_RU")
from model.entry import Entry
import random
import string

constant = [Entry(firstname="Alex", lastname= "Ivanov", nickname= "Aliosha", address="Moscow",
                           home="(812)74125896", mobile="+7-921-111-22-33", work=" 2385269", email="moy@mail.ru", email2="moy2@mail.ru", email3="",
                           byear="", ayear="", bmonth="-", aday="",
                           bday="", amonth="-"),
Entry(firstname="Julia", lastname= "Ivanova", nickname= "Ulechka", address="London",
                           home="7 (741) 9852475 3", mobile="", work="", email="", email2="", email3="",
                           byear="", ayear="", bmonth="-", aday="",
                           bday="", amonth="-")
]

def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return random.choice(months)


testdata = [Entry(firstname="", lastname= "", nickname= "", address="",
                           home="", mobile="", work="", email="", email2="", email3="",
                           byear="", ayear="", bmonth="-", aday="",
                           bday="", amonth="-")] + [Entry(firstname=fake.first_name_female(), lastname=fake.last_name_female(),
                           nickname = random_string(12) , address=fake.address(), home=fake.phone_number(), mobile=fake.phone_number(),
                           work =fake.phone_number(), email=fake.ascii_free_email(), email2=fake.ascii_free_email(),
                           email3=fake.ascii_free_email(), byear=str(random.randint(1930, 2010)),
                           ayear=str(random.randint(1930, 2010)), bmonth=random_month(),
                           aday=str(random.randint(1, 31)), bday=str(random.randint(1, 31)), amonth=random_month()) for i in range(5)]