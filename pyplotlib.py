import matplotlib.pyplot as plt
from random import randint
x_vals = [_ for _ in range(100)]
y_vals = [randint(1,5) for _ in range(len(x_vals))]
plt.plot(x_vals, y_vals)
plt.ylabel('some numbers')
#plt.legend()
plt.savefig('graph.png')
#plt.savefig('graph.png', bbox_inches='tight')
plt.show()
plt.cla()
