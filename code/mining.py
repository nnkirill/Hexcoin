import threading
import func
import string
from random import randint, choice
import time

a = list(string.ascii_lowercase)
for i in range(len(a)):
    a[i] = func.User(0)
    a[i].create_keys()


def choice_winner():
    h = func.User.selfer
    ans = []
    for i in h:
        for j in range(i.stonks):
            ans.append(i)

    print(ans)
    winner = choice(ans)
    winner.balance += 70 * winner.stonks / 2
    print(winner.balance, winner.id, ans)
    func.plus_money(70, winner.id)


def mining():
    global a
    while True:
        for i in a:
            h = choice(a)
            z = choice(a)
            if h != z:
                s = randint(5, 10)
                if h.balance - s > 80:
                    h.send_money(s, z.id)

        time.sleep(choice[17, 18, 19, 20, 21])
        for i in func.User.selfer:
            func.plus_money((i.cooling * 3 + i.stonks * 6 ) * -1, i.id)
            i.balance -= i.cooling * 3 + i.stonks * 6
        choice_winner()
        func.update_regisrty()






t1 = threading.Thread(target = mining)

