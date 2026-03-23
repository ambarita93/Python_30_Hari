import numpy as np

python_list = [i for i in range(12)]

two_dimensional_list = [[0,1,2],[3,4,5],[6,7,8]]
print(two_dimensional_list)

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)


#float numpy array
numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2)

#boolean numpy arrays
numpy_bool_array = np.array([0,1,2,3,4,-1,0],dtype=bool)
print(numpy_bool_array)

#two dimensional list
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

np_to_list = numpy_array_from_list.tolist()
print("one dimension array: ",np_to_list)
print("two dimension array: ",numpy_two_dimensional_list.tolist())
