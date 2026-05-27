# creating numpy array

import numpy as np
a=np.array([1,2,3])
print(a)
print(type(a))

#2d and 3d numpy array
b=np.array([[1,2,3],[3,4,5]])
print("2d array: \n",b)

c=np.array([[[1,2],[3,4],[5,6],[7,8]]])
print("3d array: \n", c)


#dtype

d=np.array([1,2,3], dtype=float)
print("\n",d)

# dtype can be bool, complex also 
dd=np.array([1,2,3], dtype=bool)
print("\n",dd)


ddd=np.array([1,2,3], dtype=complex)
print("\n",ddd)


#np.arrange . it wprks like range suppose you want to create a array of 1-10 than you use it like

e=np.arange(1,11)
print("\narray: ", e)
# we can also use stripes in it if we want
ee=np.arange(1,11,3)
print("\narray: ", ee)



#with reshape. it converts a numpy array into another shape

f=np.arange(1,11).reshape(5,2)
print("\n",f)