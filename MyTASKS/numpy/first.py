import numpy as np

a = np.array([200000000,400000000,500000000], dtype='int8')
b = np.array([[300000000,200000000,100000000], [300000000,500000000,7.0]],dtype='int8')
print(b.ndim)
print(a.shape)
print(b.shape)
print(a.dtype)
print(b.dtype)
print(a.itemsize)
print(b.itemsize)
print(a.nbytes)

