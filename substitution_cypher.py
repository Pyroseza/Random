from string import ascii_uppercase, ascii_lowercase, digits
from random import shuffle
usable_chars=ascii_uppercase+ascii_lowercase+' '+digits
key = [s for s in usable_chars]
shuffle(key)
key = ''.join(key)
message="secret hidden message"
encoded_message=''.join([key[usable_chars.find(c)] for c in message])
decoded_message=''.join([usable_chars[key.find(c)] for c in encoded_message])
print(f"key={key}")
print(f"message={message}")
print(f"encoded message={encoded_message}")
print(f"decoded message={decoded_message}")
