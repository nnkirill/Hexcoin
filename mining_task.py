import hashlib
import random
import functions

k=3
a = functions.random_string(k)
s = (hashlib.sha256(str(a).encode())).hexdigest()

ans = 0


while True:
    ans+= 1
    s1 = hashlib.sha256(str(functions.random_string(k)).encode()).hexdigest()
    print(s1)
    if s1 == s:
        print(ans)
        break