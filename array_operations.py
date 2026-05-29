import numpy as np

a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)

#scaler operations
#arithmetic operation

print(a1*2)
print(a2+2)
print(a1-2)
print(a2/2)
print(a1**2)


#relational

print(a2<15)
print(a2>15)


#vector operator , when we apply a operation in two numpy array
# arithmetic operation

print("array: ", a1+a2)
print("array: ", a1-a2)
print("array: ", a1*a2)
print("array: ", a1/a2)
print("array: ", a1**a2)