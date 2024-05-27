import numpy as np
import matplotlib.pyplot as plt
from django.template.defaultfilters import length

np.random.seed(123)
all_walks = []
for x in range(500):
    random_walk = [0]
    for i in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step += 1
        else:
            step += np.random.randint(1, 7)
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
plt.clf()

ends = np_aw_t[-1, :]
plt.hist(ends)
plt.show()

xa = [element for element in ends if element >= 60]
xa_l = length(xa)/5
print(xa_l)
