import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
print(w * x) # [0. 0.5]
print(np.sum(w * x)) # 0.5
print(np.sum(w * x) + b) # -0.19999999999999996