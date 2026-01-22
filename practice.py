#Create a NumPy array print its type and dtype

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
