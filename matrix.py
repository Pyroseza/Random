import random as r
import time

symbols = ["0", "1", " ", " ", " ", " ", " ", " "]
line = []
counter = 0
width = 118

for i in range(width):
    line.append(r.choice(symbols))

while 1:
    # if counter % 5 == 0:
    #     for i in [r.randint(0, width-1) for x in range(10)]:
    #         line[i] = r.choice(symbols)

    meh = ''.join([r.choice(symbols) for x in range(width)])

    print(f"{meh}")
    counter += 1
    time.sleep(0.01)
