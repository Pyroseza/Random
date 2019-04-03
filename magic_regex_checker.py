import re
regex_array = []
limit_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

for i in range(len(limit_string)):
    regexp_text = "\w*" + str(limit_string[i])*3 + "\w*"
    regex_compiled = re.compile(regexp_text)
    regex_array.append(regex_compiled)

chars_to_test = "asdfJJJ123" # read from a file or whatever...
for i in range(len(regex_array)):
    if re.match(regex_array[i], chars_to_test):
        nope = True
        print("GOTCHA!")
        print(regex_array[i], re.match(regex_array[i], chars_to_test))
        break
