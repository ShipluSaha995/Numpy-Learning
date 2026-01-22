'''
import numpy as np

arr=np.array([1,2,3,4])

print(arr+1)
print(arr*2)
print(arr-2)
print(arr/2)
print(arr**5)
'''

#vectorized math functions

import numpy as np

arr=np.array([1,2,3,4])
print(np.sqrt(arr))

arr2=np.array([1.35, 2.56, 5.69, 8.99])
print(np.round(arr2))
print(np.ceil(arr2))
print(np.floor(arr2))

#print the area of a circle for the each radius given in an array

radius=np.array([1,2,3])
print("The area of the circles are: ", np.pi*radius **2)


