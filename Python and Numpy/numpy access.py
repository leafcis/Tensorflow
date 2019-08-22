import numpy as np

matrix = np.array([[1.0, 2.0], [3.0, 4.0]])

print(matrix[0][1]) # 2.0

for row in matrix:
    print(row)
    # 0
    # [1. 2.]
    # 1
    # [3. 4.]