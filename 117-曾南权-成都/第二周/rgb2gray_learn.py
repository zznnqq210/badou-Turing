import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np
import cv2


img = cv2.imread('lenna.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print("image: %s" % img)
plt.subplot(221)
plt.imshow(img)

# 手动计算灰度
h1, w1 = img.shape[:2]
img_gray = np.zeros([h1, w1], np.float64)
for i in range(h1):
    for j in range(w1):
        m = img[i, j]
        # 算灰度值 R:0.3 G:0.59 B:0.11
        num = m[0] * 0.3 + m[1] * 0.59 + m[2] * 0.11
        # 变为0到1之间的数
        n = float(num / 255)
        img_gray[i, j] = n
print(img_gray)
print("image show gray: %s" % img_gray)
plt.subplot(222)
plt.imshow(img_gray, cmap='gray')

plt.subplot(223)
# 灰度化，直接调方法计算
img_gray1 = rgb2gray(img)
plt.imshow(img_gray1, cmap='gray')
print("---image gray----")
print(img_gray1)

# 二值化
# rows, cols = img_gray.shape
# for i in range(rows):
#     for j in range(cols):
#         if (img_gray[i, j] <= 0.5):
#             img_gray[i, j] = 0
#         else:
#             img_gray[i, j] = 1

img_binary = np.where(img_gray >= 0.5, 1, 0)
print("-----imge_binary------")
print(img_binary)
print(img_binary.shape)

plt.subplot(224)
plt.imshow(img_binary, cmap='gray')
plt.show()
