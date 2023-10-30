import rsa
import random
import hashlib
import psycopg2
import functions

conn = psycopg2.connect(host = "localhost", dbname = 'hexcoin', user = 'postgres', password = 'admin', port = 5432)
cur = conn.cursor()

class Users:
    def __init__(self):
        self.id = functions.random_string()
        self.password = functions.random_string()



        cur.execute("""CALL Insert_user(%s, %s)""",(self.id, hashlib.sha256(self.password.encode()).hexdigest()))






a = Users()

conn.commit()
cur.close()
conn.close()