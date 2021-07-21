# -*- coding: utf-8 -*-
# 双线性插值
import numpy as np
import matplotlib.pyplot as plt
import cv2


def bilinear_interp(img, out_dim):
    src_h, src_w, c = img.shape
    dst_w, dst_h = out_dim
    scale_y = float(src_h) / dst_h
    scale_x = float(src_w) / dst_w
    dst_img = np.zeros([dst_h, dst_w, c], img.dtype)
    for i in range(c):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):
                # 计算出原始图坐标
                src_x = (dst_x + 0.5) * scale_x - 0.5
                src_y = (dst_y + 0.5) * scale_y - 0.5
                # 找出原始图四个点坐标
                src_x0 = int(np.floor(src_x))
                src_x1 = min(src_x0 + 1, src_w - 1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1, src_h - 1)

                # 计算值
                temp0 = (src_x1 - src_x) * img[src_y0, src_x0, i] + (src_x - src_x0) * img[src_y0, src_x1, i]
                temp1 = (src_x1 - src_x) * img[src_y1, src_x0, i] + (src_x - src_x0) * img[src_y1, src_x1, i]
                dst_img[dst_y, dst_x, i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)
    return dst_img


if __name__ == '__main__':
    img = cv2.imread('lenna.png')
    dst = bilinear_interp(img, [800, 800])
    # 调cv2的imshow不需要将BGR转为RGB，而用plt.imshow则需要转为RGB
    cv2.imshow('image', img)
    cv2.imshow('scale image', dst)
    cv2.waitKey(0)
