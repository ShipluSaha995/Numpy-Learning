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

import numpy as np

arr=np.linspace(10, 50, 5)
print(arr)

#Create an array of numbers from 1 to 20, but only odd numbers.