import numpy as np
from pynetsigmoid import *
import matplotlib.pyplot as plt



Net = Network5([20,50,30,20,2])
sum_error = []


for pov in range(1000):
    if pov % 2 == 0:
        N0 = np.full((20,2),0.9)
        VD = np.full((2,2),0.3)
    else:
        N0 = np.full((20,2),0.3)
        VD = np.full((2,2),0.9)
    Net.trening(N0,VD,0.1)
    output = Net.status(5)
    print(output[0][0])
    sum_error.append(output[0][1])

for i in range(5):
    vvod = float(input())
    N0 = np.full((20,2),vvod)
    out = Net.think(N0)
    print(out[0][0])

plt.plot(sum_error)
plt.show()

