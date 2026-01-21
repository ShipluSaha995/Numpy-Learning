# Numpy is the fundamental packedge or core python library for scientific computing or numerical computing in python.
# it is much faster and more memory efficient.

'''
Numpy Array: A numpy array is a grid of values and it contains information about the raw data,
how to locate an element and how to interpret an element.

We can also say that it is a collection of the elements of same data-type.

key point:

--> Stored in conteguous memory  
--> Can be 1 dimensional, 2 dimensional and multi-dimensional  
--> Optimized for fast mathematical operations  

'''  
# Difference between Numpy Array and Python list 

'''
1. Consumes less memory than  python lists
2. Fast as compared to the Pyhton lists
3. Store same data-type but Python lists can store different data-types
4. Numpy array supports vectorized operations but lists requires loop

'''


# install numpy in your setup just type pip install numpy before installig numpy make sure your i have downloaded python and the pip 
# to check the numpy version :

'''
import numpy as np
print(np.__version__)
'''
# creating a numpy array
'''
import numpy as np
a = np.array([1,2,3,4,5])
print(a)
print(type(a))
'''
'''
import numpy as np
num=int(input("Enter range: "))
print("Elemets: ")
arr=[]
for i in range(num):
    element=int(input())
    arr.append(element)

print(np.array(arr))
'''

'''
# 2 Dimensional array
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.ndim)
'''
"""

import numpy as np 

row = int(input("Rows: "))
colom = int(input("Colom: "))

matrix=[]

print("Enter elements row by row: ")

for i in range(row):
    rows= list(map(int,input(f"Enter {colom} elements for rows{i+1}: ").split()))
    matrix.append(rows)

arr=np.array(matrix)
print(arr)
print(arr.shape)
print(arr.ndim)
"""

# multi dimensional array 
"""
import numpy as np

arr = np.array([[['A', 'B','C'],['D', 'E', 'F'],['G','H','I']],
                [['J','K','L'], ['M','N','O'],['P','Q','R']],
                [['S','T','U'], ['V','W','X'],['Y','Z',' ']]])
print(arr)
print("\n", arr.shape)
print("\n", arr[2,0,0]+arr[0,2,1]+arr[0,2,2]+arr[1,2,0]+arr[1,0,2]+arr[2,0,2])
name=arr[2,0,0]+arr[0,2,1]+arr[0,2,2]+arr[1,2,0]+arr[1,0,2]+arr[2,0,2]
print(f'My name is {name}')
"""
'''
import numpy as np

x=int(input("blocks: "))
y=int(input("rows per block: "))
z=int(input("colom per row: "))

data=[]

for i in range(x):
    block=[]
    for j in range(y):
        row=list(map(int, input().split()))
        block.append(row)

    data.append(block)

arr=np.array(data)
print(arr)
'''
'''
# rows selection
#print the rows we need 

import numpy as np

arr=np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]
            ])

print("\n",arr[1]) #this wil prinnt the first row

#print(arr[strat:end:step])

print("\n",arr[0:4]) #here the ending index is exclusive

print("\n", arr[0:4:2]) #it will print the 0 number row and the 2nd row (the counting of rows start from 0)
print("\n", arr[::2])

# to print the arrays in reverse order like down to up we can use negative 
print("\n", arr[::-1])
'''

#Colom Selection

import numpy as np

arr=np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]
            ])

print("\n", arr[:, 0]) # counting of the colom will start from 0 the colon is for to select all the rows

print("\n", arr[:, 1])

print("\n", arr[:, 0:3]) # sets the range of the colom to print 
print("\n", arr[:, ::2]) #setting the step

print("\n", arr[:, ::-1]) #reverse the coloms

print("\n",arr[:, ::])

#selecting  quadrent

print("\n", arr[0:2, 0:2])
print("\n", arr[0:2, 2:])