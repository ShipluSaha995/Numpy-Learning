import numpy as np

a1=np.arange(10)
a2=np.arange(12, dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

print(f"a1={a1.ndim}, a2={a2.ndim}, a3={a3.ndim}")