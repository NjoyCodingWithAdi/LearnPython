# numpy: numpy is an external package <mainly used for mathematical calculations >

# Dimensions in Arrays

# 0-D Arrays

import numpy as np

arrOne = np.array(42)
print(arrOne)

# 1-D Arrays

arrTwo = np.array([1, 2, 3, 4, 5])
print(arrTwo)

# 2-D Arrays

arrThree = np.array([[1, 2, 3], [4, 5, 6]])
print(arrThree)

# 3-D Arrays - An array that has 2-D arrays (matrices) as its elements is called 3-D array. These are often used to represent a 3rd order tensor. 
# Example - Image is 3D array - R, G, B

arrFour = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arrFour)

# Check the dimention of array

print(arrOne.ndim)
print(arrTwo.ndim)
print(arrThree.ndim)
print(arrFour.ndim)

# Higher Dimensional Arrays

arrFive = np.array([1, 2, 3, 4], ndmin=5)
print(arrFive)
print('number of dimensions :', arrFive.ndim)

# Revert the 3d array to convert single vector

print("Use of ravel")
print(arrFour.ravel)
print("Use of flatten")
print(arrFour.flatten)