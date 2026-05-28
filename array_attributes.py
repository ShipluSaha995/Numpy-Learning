
import numpy as np

#ndim used to find the dimention of the array

a1=np.arange(10)
a2=np.arange(12, dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

print(f"a1={a1.ndim}, a2={a2.ndim}, a3={a3.ndim}")


#shape, used to find how many items in each dimantion
print(a2.shape)
print(a1.shape) 
print(a3.shape)


# size finds how many items in the array
print(a3.size)
print(a2.size)
print(a1.size)


#itemsize finds the size of the each memory that how much memeory they occupied (in bytes)
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)


#dtype type of the array
print(a1.dtype)
print(a2.dtype)
print(a3.dtype) 




#Changing datatypes 
#astype to change the datatype of the remaining array

print(a2.dtype)
a2 = a2.astype(np.int32)
print(a2.dtype)