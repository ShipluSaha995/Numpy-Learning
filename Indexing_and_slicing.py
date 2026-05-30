import numpy as np

a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

print(a1)

# find the last item from a1

print(a1[-1])
print(a1[0])

#2d array 

print(a2)
print(a2[1,2])
print(a2[2,3])
print(a2[2,1])
print(a2[0,0])