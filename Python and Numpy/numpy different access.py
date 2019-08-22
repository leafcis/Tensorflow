import numpy as np

matrix = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

print(matrix[np.array([0, 2, 4])]) # [1. 3. 5.]
print(matrix < 3) # [True True False False False False]
print(matrix[matrix < 3]) # [1. 2.]