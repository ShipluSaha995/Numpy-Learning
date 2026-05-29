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


