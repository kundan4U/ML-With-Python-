"""
import numpy as np

a = np.arange(0, 10)
print(a)


1D to 2D

import numpy as np
a = np.array([[10],[20],[30]])
b = np.array([[40],[50],[60]])
c = np.dstack((a, b))
print(a)
print(b)
print(c)
"""
import numpy as np
a=np.array([1])
b=np.array([20])
for i in range(a,b):
    if(i%2!=0):
        print(i)