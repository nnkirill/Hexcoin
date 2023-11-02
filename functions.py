import rsa
import random
import string
import psycopg2
import hashlib


conn = psycopg2.connect(host = "localhost", dbname = 'hexcoin1', user = 'postgres', password = 'admin', port = 5432)
cur = conn.cursor()


class Create_User:
    
    passwords = {}
    def __init__(self):

           
        self.id = random_string()
        self.password = random_string()
        Create_User.passwords.update([(self.id, self.password)])
        
        conn = psycopg2.connect(host = "localhost", dbname = 'hexcoin1', user = 'postgres', password = 'admin', port = 5432)
        cur = conn.cursor()

        cur.execute("""CALL Create_user(%s, %s, %s, %s)""",(self.id, hashlib.sha224(self.password.encode()).hexdigest(), hashlib.sha256(self.password.encode()).hexdigest(), 0))



def random_string() -> str:
    letters = string.ascii_letters
    letters += '1234567890'
    random_string = ''.join(random.choice(letters) for i in range(16))
    return random_string


def create_user() -> str(id):
    a = Create_User()
    return a.id



def sign_in(id, password) -> bin:
    pas = []
    try:
        cur.execute("""SELECT password_hash_sha224 FROM Users WHERE id = %s """, (id,))
        pas.append([(hashlib.sha224(password.encode())).hexdigest()])
        pas.append(list(cur.fetchone()))
        cur.execute("""SELECT password_hash_sha256 FROM Users WHERE id = %s """, (id,))
        pas.append([(hashlib.sha256(password.encode())).hexdigest()])
        pas.append(list(cur.fetchone()))
        if pas[0] == pas[1]:
            if pas[2] == pas[3]:
                return 1
    except:
        print("No such id") 
        return 0






conn.commit()
cur.close()
conn.close()
