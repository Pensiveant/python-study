# reference:https://numpy.org/doc/stable/reference/routines.statistics.html

import numpy as np

# -----------------numpy.amin(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)----------------
array = np.array([[1, 2, 3],[4,5,6],[7, 8, 9]])
min=np.amin(array) # 1

min1=np.amin(array,axis=0) # array([1, 2, 3])
min2=np.amin(array,axis=1) # array([1, 4, 7])

print('')