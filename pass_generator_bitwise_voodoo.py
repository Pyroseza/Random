from random import choice, randint
from string import ascii_letters, digits

def random_pwd():
    while True:
        r, t, ranges = 0, 0, [(48, 57), (65, 90), (97,122)]
        pw = ''.join([chr(randint(*choice(ranges))) for _ in range(8)])
        for s in pw:
            for i, l in enumerate(ranges):
                x = 1<<i
                t = t | x
                r = (r | x) if ord(s) in range(*l) else r
        if r ^ t == 0:
            return pw

for _ in range(20):
    print(random_pwd())
