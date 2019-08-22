import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../src/Lena.png') # 이미지 읽어오기

plt.imshow(img)
plt.show()