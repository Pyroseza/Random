
#let's make some PEPPER



import random

for i in range(10):
    #random.seed(666)
    pepper = ''.join(f'{random.randrange(256):02X}' for i in range(16))
    print(pepper)


# salt over here
#salt = ''.join(random.choice('0123456789abcdef') for n in range(32))
#print(salt)

# a little faster
#import binascii
# salt = binascii.b2a_hex(os.urandom(15))

# fastest
#salt = '%02x' % random.randrange(16**30)


# chars to hex
# hex(ord("c"))
# '0x63'
# format(ord("c"), "x")
# '63'
# "c".encode("hex")
# '63'

print('')
print('')
print('')


#felix run python
#```python
import random
import string
for i in range(10):
    #random.seed(666)
    print(''.join(random.choices(string.ascii_uppercase + string.digits, k=32)))
#```
