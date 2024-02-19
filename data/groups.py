from model.group import Group
import random
import string


testdata = [
    Group(name="name1-Alexey", header="header1", footer="footer1"),
    Group(name="name2-Julia", header="header2", footer="footer2")
]

"""constant = [
    Group(name="name1-Salehard", header="header1", footer="footer1"),
    Group(name="name2-Navalny", header="header2", footer="footer2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])"""


"""testdata = [Group (name ="", header ="", footer ="")] +  [Group (name =random_string("name", 10), header = random_string("header", 20),
                            footer = random_string("footer", 20)) for i in range(2)]"""

"""testdata = [Group (name =name, header =header, footer =footer)
           for name in ["", random_string("name", 10)]
           for header in ["", random_string("header", 20)]
           for footer in ["", random_string("footer", 20)]
                ]"""