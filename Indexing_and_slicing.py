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

# 3D array

print(a3)

print(a3[0,1,1])
print(a3[1,0,0])
print(a3[1,1,0])


# slicing
print(a1)
print(a1[2:5])
print(a1[0:5])

print(a1[2:5:2])
# start = 2 → start from index 2
# stop = 5 → go up to (but not including) index 5
# step = 2 → move 2 positions at a time
print(a1[1:9:2])
print(a1[3:10:3]) 




# 2D Array

print(a2)
print(a2[0,:])
print(a2[:,2])
print(a2[1:, 1:3])
print(a2[1:2, 0:2])
print(a2[2:, 2:4])
print(a2[2:, 1:3])
print(a2[0:, 2:4])
print(a2[::2, ::3])
print(a2[::2, 1::2])
print(a2[1::2, ::3])
print(a2[:2, 1:])


#3D array

a3=np.arange(27).reshape(3,3,3)
print(a3)


print(a3[1])
print(a3[::2])
print(a3[0,1,:])
print(a3[1,:,1])
print(a3[2,1:,1:])
print(a3[::2, 0, ::2])
