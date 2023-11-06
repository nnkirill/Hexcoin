
import rsa
import random
import string
import psycopg2
import hashlib

keys = {}

conn = psycopg2.connect(host = "localhost", dbname = 'hexcoin', user = 'postgres', password = 'admin', port = 5432)
cur = conn.cursor()


class Create_User:
    
    passwords = {}
    def __init__(self):

           
        self.id = random_string()
        self.password = random_string()
        Create_User.passwords.update([(self.id, self.password)])
        
        conn = psycopg2.connect(host = "localhost", dbname = 'hexcoin', user = 'postgres', password = 'admin', port = 5432)
        
        cur.execute("""CALL Create_user(%s, %s, %s, %s)""",(self.id, hashlib.sha224(self.password.encode()).hexdigest(), hashlib.sha256(self.password.encode()).hexdigest(), 0))



def random_string(a = 16) -> str:
    letters = string.ascii_letters
    letters += '1234567890'
    random_string = ''.join(random.choice(letters) for i in range(a))
    return random_string


def create_user() -> str(id):
    a = Create_User()
    return a.id



def sign_in(id, password) -> bin:
    pas = []
    try:
        cur.execute("""SELECT password_hash_sha224 FROM users WHERE id = %s """, (id,))
        pas.append([(hashlib.sha224(password.encode())).hexdigest()])
        pas.append(list(cur.fetchone()))
        cur.execute("""SELECT password_hash_sha256 FROM users WHERE id = %s """, (id,))
        pas.append([(hashlib.sha256(password.encode())).hexdigest()])
        pas.append(list(cur.fetchone()))
        if pas[0] == pas[1]:
            if pas[2] == pas[3]:
                return 1
    except:
        print("No such id") 
        return 0


def create_keys(id, password) -> rsa.key.PublicKey:
    if sign_in(id, password) == 1:
        (public_key, privet_key) = rsa.newkeys(512)
        keys.update([(id , (public_key, privet_key))])
        
        print(type(public_key))
        cur.execute("""CALL delete_key(%s)""", (id,))
        cur.execute("""CALL pub_key_value(%s, %s)""", (id, str(public_key)))
        return public_key
    else:
        print('wrong id or password')



def send_money(amount, recipient_id, id) -> bin:
    if sign_in(id, str(input('пароль:'))) == 1:
        (public_key, privet_key) = rsa.newkeys(512)
        amount_c = rsa.encrypt(str(amount).encode(), public_key)
        print(amount_c)
        print(rsa.decrypt(amount_c, privet_key))
        amount_c += b'1'
        print(rsa.decrypt(amount_c, privet_key))

    
    else:
        print(0)
    



a = Create_User()
print(Create_User.passwords)
send_money(5,'kknn', str(input()))







        
conn.commit()
cur.close()
conn.close()
