from random import choice, randint
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def random_pwd(size):
    es = [
        [*ascii_lowercase],
        [*ascii_uppercase],
        [*digits],
        #[*punctuation]
        [*"!#$%&()*+-:;<=>?@[]^_{|}~"]
    ]
    if size<len(es):
        m = '7085677532797070327765846933'
        r = ''.join([chr(int(m[_:_+2])) for _ in range(0, len(m), 2)])
        return r, 0
    tries = 0
    while True:
        tries += 1
        r, t = 0, 0
        pw = ''.join([choice(choice(es)) for _ in range(size)])
        for c in pw:
            for i, l in enumerate(es):
                x = 1<<i
                t = t | x
                r = (r | x) if c in l else r
        if r ^ t == 0:
            return pw, tries

for _ in range(20):
    print("PW: {}, attempts {}".format(*random_pwd(20)))
