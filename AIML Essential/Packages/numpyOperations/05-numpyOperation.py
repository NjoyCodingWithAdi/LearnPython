
import numpy as np

# extract 5,6,7,8 using slicing
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print (a)

'''Functions to read your data
a. Inbuilt function
b. Numpy function 
c. Panda function - Most widely used one'''

# Save the array into a text file

np.savetxt('newfile.txt', a)

# Read the text file using numPy

newarr = np.loadtxt('..\\LearnPython-1\\newfile.txt')
print(newarr)