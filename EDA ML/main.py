import numpy as np
from cffi.ffiplatform import flatten

a=np.array([[1,2,3],[4,5,3],[5,4,7]])
print(a)
print(flatten(a))


