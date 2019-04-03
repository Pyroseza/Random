#!/usr/bin/env python
class ThingToMakeDynamic():
    pass

    def __init__(self):
        self.a = "a"

obj = ThingToMakeDynamic()

print("object created and only has {0} attribute".format(len(vars(obj))))

for key in vars(obj):
    print(key, " -> ",getattr(obj,key))
    
print("check for 'a'")
print("a -> ",getattr(obj,"a"))
print("check for 'b'")
try:
    print("b -> ",getattr(obj,"b"))
except:
    print("b does not exist")

user_input_attribute = input("add a new attribute:")
user_input_value = input("add a new value:")
setattr(obj, user_input_attribute, user_input_value)

new_attributes = ["one", "two", "three", "four", "five"]
print("adding more attributes! \n {0}".format(new_attributes))

for p in new_attributes:
    setattr(obj, p, new_attributes.index(p) + 1)
    
print("object now has more attributes to use! total {0}".format(len(vars(obj))))
for key in vars(obj):
    print(key, " -> ",getattr(obj,key))
