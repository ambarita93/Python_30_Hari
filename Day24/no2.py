import numpy as np

np_zeros = np.zeros((3,4),dtype=int,order='C')
print(np_zeros)

np_ones = np.ones((3,5),dtype=float,order='C')
print(np_ones)

random_float = np.random.random(2)
print(random_float)

normal_array = np.random.normal(50,1,100)
print(normal_array)