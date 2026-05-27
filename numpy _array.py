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



# np.ones and np.zeros using this we can create an array on the go and all elements of this array will be one

g=np.ones((3,4))
print("\n",g)

h=np.zeros((3,4))
print("\n",h)


# to initialize with random numbers ( it will give random numbers from 0 to 1 )

i=np.random.random((3,4))
print("\n",i)


# np.linespace, suppose i want 10 random numbes from -10 to 10
j=np.linspace(-10,10,10)
print("\n",j)



#np.identity used to create identity matrix
k=np.identity(3)
print("\n",k)