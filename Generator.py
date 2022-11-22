import string
import random


def gen(len_pass):
    digits = string.digits
    letter = string.ascii_uppercase
    letters = string.ascii_lowercase
    sibo = string.punctuation

    passwd = digits + letter + letters + sibo
    p = ' '
    for i in range(len_pass):
        p = p + random.choice(passwd)
    yield p


print(next(gen(8)))
print(next(gen(9)))
print(next(gen(10)))

