# python regex

import re
line = "i'm sexy and i know it, who i, boi yeah"
result = re.sub(r"\bi\b",r"I",line)
print(result)

# sed regex using python
import os
test = "echo i\'m sexy and i know it, who i, boi yeah | sed 's/\\bi\\b/I/g'"
print(test)
os.system(test)
