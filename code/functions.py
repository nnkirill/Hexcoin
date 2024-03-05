
import rsa
import random
import string
import psycopg2
import hashlib

keys = {}
number = 0
conn = psycopg2.connect(host = "localhost", dbname = 'hexcoin', user = 'postgres', password = 'admin', port = 5432)
cur = conn.cursor()


class User:
    
    passwords = {}
    def __init__(self):

           
        self.id = random_string()
        self.password = random_string()
        User.passwords.update([(self.id, self.password)])
        self.public_key = 0
        self.privet_key = 0
        
        flops = 5
        cooling = 1
        
        
        cur.execute("""CALL Create_user(%s, %s, %s, %s)""",(self.id, hashlib.sha224(self.password.encode()).hexdigest(), hashlib.sha256(self.password.encode()).hexdigest(), 1))


    def create_keys(self) -> rsa.key.PublicKey:
        if sign_in(self.id, self.password) == 1:
            (public_key, privet_key) = rsa.newkeys(512)
            keys.update([(id , (public_key, privet_key))])
            self.public_key = public_key
            self.privet_key = privet_key
            cur.execute("""CALL delete_key(%s)""", (self.id,))
            cur.execute("""CALL pub_key_value(%s, %s)""", (self.id, str(public_key)))
        else:
            print('wrong id or password')


    def send_money(self, message, recipient_id) -> bin:
        cur.execute("""SELECT transaction_id FROM temporary_registry""") 
        cur.fetchone()
        cur.execute("""CALL new_transaction(%s, %s, %s, %s, %s)""",(1 , message, self.id, recipient_id, str(rsa.sign(str(message).encode(), self.privet_key, 'SHA-256').hex())))

def random_string(a = 16) -> str:
    letters = string.ascii_letters
    letters += '1234567890'
    random_string = ''.join(random.choice(letters) for i in range(a))
    return random_string


def create_user() -> str(id):
    a = User()
    return a.passwords


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
        print(public_key)
        print(privet_key)
        cur.execute("""CALL delete_key(%s)""", (id,))
        cur.execute("""CALL pub_key_value(%s, %s)""", (id, str(public_key)))
        return privet_key
    else:
        print('wrong id or password')






def close_data():
    conn.commit()
    cur.close()
    conn.close()



        
