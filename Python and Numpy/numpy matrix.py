import numpy as np

matrix = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[3, 0], [0, 6]])

print(matrix) # [[1 2]
              #  [3 4]]
# 행렬의 형상
print(matrix.shape) # (2, 2)
# 행렬에 담긴 원소의 자료형
print(matrix.dtype) # int32

print(matrix + matrix2) # [[ 4  2]
                        #  [ 3 10]]
print(matrix * matrix2) # [[ 3  0]
                        #  [ 0 24]]