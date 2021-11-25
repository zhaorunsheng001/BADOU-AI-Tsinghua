import numpy as np
import cv2 as cv


def rgb2nearest(src_img, out_dim):
    src_h, src_w, src_c = src_img.shape
    height, width = out_dim[0], out_dim[1]
    empty_img = np.zeros((height, width, src_c), np.uint8)

    # new image with scale_H * scale_W

    scale_H = src_h/ height
    scale_W = src_w / width

    for c in range(src_c):
        for i in range(height):
            for j in range(width):
                x = int(round(i * scale_H))
                y = int(round(j * scale_W))
                empty_img[i, j, c] = src_img[x, y, c]
    return empty_img


if __name__ == '__main__':
    src_img = cv.imread("lenna.png")
    cv.imshow("src_img", src_img)
    # src_img = cv.cvtColor(src_img, cv.COLOR_BGR2RGB)
    nearest_img = rgb2nearest(src_img, (800, 800))
    cv.imshow("nearest_img", nearest_img)
    cv.waitKey()
