import rsa
import random
import string


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

def transactions():
    address = str(input("Write address"))
    if address not in Account.ider:
        print('addres is not exist')
        transactions()


    


Account()
Account()
print(Account.selfer[0].id)
print(Account.selfer[1].id)

transactions()