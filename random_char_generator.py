import random
import string

def randomStringDigits(stringLength=10):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

for i in range(1000000):
    print(i, randomStringDigits())
