# Python

Python is a programming language that easy to learn. We can use it free because python is Open source.

Python's syntax is similar to English. And Python doesn't have uncomfortable compile process.

Python code is very easy to read and have good perfomance.

# Numpy
딥러닝을 구현하다 보면 배열이나 행렬 계산이 많이 등장한다.

`넘파이`의 배열 클래스인 numpy.array에는 편리한 메서드가 많이 준비되어 있다.

넘파이는 외부 라이브러리이므로
> import numpy as np

를 통해 라이브러리를 불러온다.

넘파이 배열을 생성하기 위해서는 np.array() 메서드를 이용한다. np.array()는 파이썬의 리스트를 인수로 받아 넘파이 라이브러리가 제공하는 특수 형태 배열(numpy.ndarray)을 반환한다.

넘파이 배열을 생성해보자.
```
import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x) # [1. 2. 3.]
print(type(x)) # <class 'numpy.ndarray'>
```

다음으로 넘파이의 산술 연산을 알아보겠다.

```
import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

# 원소별 덧셈
print(x + y) # [3. 6. 9.]
# 원소별 뺄셈
print(x - y) # [-1. -2. -3.]
# 원소별 곱셈
print(x * y) # [ 2.  8. 18.]
# 원소별 나눗셈
print(x / y) # [0.5 0.5 0.5]
```
여기서 주의할 점은 배열 x와 y의 원소 수가 둘 다 원소를 3개씩 갖는 1차원 배열로 같다는 것이다.

x와 y의 원소 수가 같다면 산술 연산은 각 원소에 대해서 행해진다. 원소수가 다르면 오류가 발생하게 되니 원소 수 맞추기는 중요하다.

참고로, '원소별'이라는 말은 영어로 element-wise라고 한다. '원소별 곱셈'은 element-wise product라고 한다.

넘파이 배열은 원소별 계산 뿐 아니라 넘파이 배열과 수치 하나(스칼라 값)의 조합으로 된 산술 연산도 수행할 수 있다. 이 경우 스칼라 값과의 계산이 넘파이 배열의 원소별로 한 번씩 수행된다.

벡터는 리스트, 스칼라는 단일 값이라고 생각하면 편하다.

```
import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x / 2.0) # [0.5 1.  1.5]
```

넘파이는 1차원 배열 뿐 아니라 다 차원 배열도 작성할 수 있다.

```
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
```
2차원 배열은 행렬이라고 한다. 행렬의 형상은 N차원 배열에서 그 배열의 각 차원의 크기이다.

형상이 같은 행렬끼리면 행렬의 산술 연산도 대응하는 원소별로 계산된다. 행렬과 스칼라 값의 산술 연산도 가능하다.

넘파이 배열은 N차원 배열을 작성할 수 있는데, 1차원 배열, 2차원 배열, 3차원 배열처럼 원하는 차수의 배열을 만들 수 있다는 뜻이다. 수학에서 1차원 배열은 벡터, 2차원 배열은 행렬, 백터와 행렬을 일반화한 것을 텐서라고 한다.

넘파이에서는 형상이 다른 배열끼리도 계산할 수 있다.

```
import numpy as np

matrix = np.array([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])
array = np.array([1.0, 2.0, 3.0])

print(matrix * 3) # [[ 3.  6.  9.]
                  #  [12. 15. 18.]]
print(matrix * array) # [[ 1.  4.  9.]
                      #  [ 4. 10. 18.]]
```
위 코드에서는 2 * 3 행렬에 스칼라 값 3과 array([1.0, 2.0, 3.0]) 벡터 값을 곱했다.
그 결과 행렬 matrix와 똑같은 형상으로 변환 된 뒤 원소별 연산이 이루어졌다.

이것을 브로드캐스트 기능이라고 한다.

![](https://user-images.githubusercontent.com/36766295/63498119-3288aa80-c500-11e9-96a4-6e8e0859bd4d.png)


원소 접근 방식은 기존 배열과 그렇게 다를 바 없다.


