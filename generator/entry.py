from faker import Faker
fake = Faker()
from model.entry import Entry
import random
import string
import os.path
import json

# генератор рандомной строки
def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# генератор рандомного месяца
def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return random.choice(months)

# создание тестовых данных в цикле
# может использоваться без файлов подстановкой testdata в тест
testdata = [Entry(firstname="", lastname= "", nickname= "", address="",
                           home="", mobile="", work="", email="", email2="", email3="",
                           byear="", ayear="", bmonth="-", aday="",
                           bday="", amonth="-")] + [Entry(firstname=fake.first_name_female(), lastname=fake.last_name_female(),
                           nickname = random_string(12) , address=fake.address(), home=fake.phone_number(), mobile=fake.phone_number(),
                           work =fake.phone_number(), email=fake.ascii_free_email(), email2=fake.ascii_free_email(),
                           email3=fake.ascii_free_email(), byear=str(random.randint(1930, 2010)),
                           ayear=str(random.randint(1930, 2010)), bmonth=random_month(),
                           aday=str(random.randint(1, 31)), bday=str(random.randint(1, 31)), amonth=random_month()) for i in range(3)]

# путь к файлу, в который запишем созданные данные
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/entries.json")

# открываем файл и записываем сгенерированные тестовые данные в формате json
with open(file, "w") as f:
    # default превращает данные в словарь
    # indent форматирует файл
    f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))