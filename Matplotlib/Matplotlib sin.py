import numpy as np
import matplotlib.pyplot as plt # 그래프를 그리는 모듈 pyplot

# 데이터 준비
x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로
y = np.sin(x)

# 그래프 그리기
plt.plot(x, y)
plt.show()