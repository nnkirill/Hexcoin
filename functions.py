import rsa
import random
import string
import psycopg2


def random_string():
    letters = string.ascii_letters
    letters += '1234567890'
    random_string = ''.join(random.choice(letters) for i in range(16))
    return random_string