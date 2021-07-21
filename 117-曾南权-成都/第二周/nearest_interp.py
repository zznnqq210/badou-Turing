# -*- coding: utf-8 -*-
# 最邻近插值

import cv2
import numpy as np


def func(image, out_dim):
    h, w, c = image.shape
    out_width, out_height = out_dim
    empty_img = np.zeros([out_height, out_width, c], image.dtype)
    sh = out_width / h
    sw = out_width / w
    for i in range(out_height):
        for j in range(out_width):
            x = int(i / sh)
            y = int(j / sw)
            empty_img[i, j] = image[x, y]
    return empty_img


if __name__ == '__main__':
    img = cv2.imread('lenna.png')
    zoom = func(img, [800, 800])
    print(zoom)
    print(zoom.shape)
    cv2.imshow('nearest interp', zoom)
    cv2.imshow('image', img)
    cv2.waitKey(0)
