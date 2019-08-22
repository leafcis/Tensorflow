# Matplotlib

Matplotlib는 딥러닝 실험에서 중요한 그래프 그리기와 데이터 시각화를 위해 그래프를 그려주는 라이브러리다. 이 라이브러리를 이용하면 그래프 그리기와 데이터 시각화가 쉬워진다.

단순히 그래프를 그려보자. sin함수를 그려보겠다.

```
import numpy as np
import matplotlib.pyplot as plt # 그래프를 그리는 모듈 pyplot

# 데이터 준비
x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로
y = np.sin(x)

# 그래프 그리기
plt.plot(x, y)
plt.show()
```
코드 실행 결과는 아래와 같다.

![](https://user-images.githubusercontent.com/36766295/63511037-18a89100-c51b-11e9-9662-767d72d96f2f.png)

다음으로 cos 함수도 그려보겠다. 또, 제목과 각 축의 이름 표시와 pyplot의 다른 기능도 사용해보겠다.

```
import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos") # 점선으로 그린다
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title("sin & cos") # 제목
plt.legend()
plt.show()
```
코드 실행 결과는 아래와 같다.

![](https://user-images.githubusercontent.com/36766295/63511042-19412780-c51b-11e9-86a3-e5fdf5a3cd76.png)


pyplot에는 이미지를 표현해주는 메서드인 imshow()도 있다. 이미지를 읽어 들일 때는 matplotlib.image 모듈의 imread() 메서드를 이용한다.

```
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../src/Lena.png') # 이미지 읽어오기

plt.imshow(img)
plt.show()
```
코드 실행 결과는 아래와 같다.

![](https://user-images.githubusercontent.com/36766295/63511035-180ffa80-c51b-11e9-8b80-8c6e33993633.png)

