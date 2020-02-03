# NeuralLib
this is small lib for neural networks in Python3.7.
First lib is lib or Leaky ReLu activation, 
socend lib is is or Sigmoid activation,
this libs is 5 leyers.
To use this libs paste libs near to your python file.
to import ReLu lib write: from pynetrelu import *
to import Sigmoid lib write: from pynetsigmoid import *
To created new neural network write this: 
<your name on request> = Network5([n,n,n,n,n])
to treaning your network write:
<your network>.trening(inputs,must,speed lerning)
to get out network write:
out = <your network>.status(leyer number)# 1,2,3,4 or 5.

example:

import numpy as np
from pynetrelu import *



Net = Network5([20,50,30,20,2])


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

for i in range(5):
    vvod = float(input())
    N0 = np.full((20,2),vvod)
    out = Net.think(N0)
    print(out[0][0])

