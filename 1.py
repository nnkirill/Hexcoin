import rsa
import random
import string
# бугалтерская двойная запись

def registry_reading(operation, id): #фуекция возвращяет все транзакции одного пользователя или все имеющиеся в реестре адреса
    user_registry = []
    file = open('registry.txt', 'r')
    line = file.readline()

    if operation == 'existing addresses':
        while line:
            line = tuple(line.split())
            user_registry.append(line[0])
            line = file.readline() 

        user_registry = set(user_registry)
        return user_registry
        

    elif id == 'opend entrances':
        pass


    elif operation == 'user_registry':
        while line:
            line = tuple(line.split())
            if line[0] == id:
                    user_registry.append(line)
            line = file.readline()  
        file.close()

        return user_registry


def random_string():
    letters = string.ascii_letters
    letters += '1234567890'
    random_string = ''.join(random.choice(letters) for i in range(16))
    return random_string


class Account:
    
    selfer = []
    ider = []

    def __init__(self):
        (self.public_key, self.privet_key) = rsa.newkeys(512)
        self.id = random_string()
        
        file = open('registry.txt', 'a')
        file.write(f'{self.id} + 0 \n')
        file.close()
        

        Account.selfer.append(self)
        Account.ider.append(self.id) #написать фукцию для чтения реестра


def transaction():
    address_sender = str(input("Write sender address"))
    if address_sender not in registry_reading('existing addresses', 0):
        print("addres doesn't exist")
        transaction()
    address_recipient = str(input("Write recipient address"))
    if address_recipient not in registry_reading('existing addresses', 0):
        print("addres doesn't exist")
        transaction()
    

    print('write sum')
    summ = int(input())
    print(registry_reading('user_registry', address_sender))







print(registry_reading('existing addresses', 0))
transaction()
