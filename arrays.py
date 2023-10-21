''' Python arrays '''
import numpy as np

my_array = np.array([45, 9, 7])
my_data = [9, 3, 45, 23]

print(my_array, type(my_array), type(my_data))

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]

my_mult_dim = np.array([list_1, list_2, list_3])
print(my_mult_dim, my_mult_dim.shape)

# name = 'Duke lester is an amazing employee'
# my_array_2 = np.fromiter(name, dtype='U2')
# print(my_array_2)

print(np.arange(0, 200,50, dtype=np.float32))
print(np.linspace(200, 3000, 200000000, dtype=np.int32))
print(np.empty([3, 4], dtype=np.int64))
