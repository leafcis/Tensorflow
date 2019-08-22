import numpy as np

matrix = np.array([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])
array = np.array([1.0, 2.0, 3.0])

print(matrix * 3) # [[ 3.  6.  9.]
                  #  [12. 15. 18.]]
print(matrix * array) # [[ 1.  4.  9.]
                      #  [ 4. 10. 18.]]