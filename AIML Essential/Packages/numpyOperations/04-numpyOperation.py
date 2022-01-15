# use the function reshape
# create an array from 0 to 20
# create an array by extracting numbers between 10, 20, 2

import numpy as np

arr = np.arange(21)
print(arr)

# concept of slicing
arrOne = arr[10:21:2]
print(arrOne)

# extract 5,6,7,8 using slicing
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print (a)

print(a[1:3,1:3])

# extract 4,5,7,8
print(a[1:3,0:2])

# find out the shape of an array 
print(a.shape)

# find out the dimention of an array 
print(a.ndim)

# find out the size of the array
print(a.size)

# find out the size of an array element
print("Memory size of one array element in bytes: ",a.itemsize)

# memory size of numpy array in bytes
print("Memory size of numpy array in bytes:",
      a.size * a.itemsize)


'''Functions to read your data
a. Inbuilt function
b. Numpy function 
c. Panda function - Most widely used one'''