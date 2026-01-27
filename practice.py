#Create a NumPy array print its type and dtype
'''
import numpy as np

arr=np.array([5,10,15,20,25])
print(arr)
print(arr.dtype)

ran=int(input("Enter the range: "))
print("Data: ")
arr2=[]
for i in range(ran):
    elements=int(input())
    arr2.append(elements)
print(np.array(arr2))
print(type(arr2))
print(np.array(arr2).dtype)
'''
''''
Create:

1. A NumPy array of 8 zeros
2. A NumPy array of 8 ones
3. A NumPy array of 8 values all equal to 3
'''
'''
import numpy as np

arr=np.zeros(8)
arr2=np.ones(8)
arr3=np.full(8, 3)
print(f'{arr},\n {arr2},\n {arr3}')
'''

#Create 5 evenly spaced values between 10 and 50 (inclusive).
'''
import numpy as np

arr=np.linspace(10, 50, 5)
print(arr)
'''

'''
#Create an array of numbers from 1 to 20, but only odd numbers.
import numpy as np

arr=np.arange(1, 21, 2)
print(arr)
'''
'''
import numpy as np

arr=np.array([[10,20,30],
              [40,50,60]])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
'''

#Create an array of 1-12 and reshape it in 3 rows and 4 coluoms

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a=np.reshape(arr,(3, 4))
print(a)