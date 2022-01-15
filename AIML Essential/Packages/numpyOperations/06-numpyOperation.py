# create a random array of 5,5 dimension
# save it in a txt file 'exOne'

# read exOne.txt and extract the data into 'b'
# print b

import numpy as np

a = np.random.random((5,5))
print(a)

np.savetxt('exOne.txt',a)

b = np.loadtxt('..\\LearnPython-1\\exOne.txt')
print(b)
