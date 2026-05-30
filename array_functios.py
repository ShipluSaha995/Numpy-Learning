import numpy as np
a1=np.random.random((3,3))
a1=np.round(a1*100)
print(a1)

# max/min/sum/prod

print(np.max(a1))
print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))
print(np.max(a1, axis=0)) #column wise
print(np.max(a1, axis=1)) #row wise



# mean/median/std/var

print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))

print(np.mean(a1, axis=0)) #column wise
print(np.mean(a1, axis=1)) #row wise


# trigonometric functions

print(np.sin(a1))
print(np.cos(a1))
print(np.tan(a1))

print(np.arcsin(a1))
print(np.arccos(a1))
print(np.arctan(a1))


# dot product

a2=np.arange(12).reshape(3,4)
a3=np.arange(12,24).reshape(4,3)

print(np.dot(a2,a3))



#log and Exponent

print(np.log(a1))
print(np.exp(a1))


# round/floor/cell

print(np.round(np.random.random((2,3))*100))
print(np.floor(np.random.random((2,3))*100))
print(np.ceil(np.random.random((2,3))*100))

