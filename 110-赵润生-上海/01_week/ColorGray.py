import cv2
import numpy as np
import cv2 as cv

def rgb2gray(src_img):
    img_H, img_W = src_img.shape[:2]
    empty_image = np.zeros((img_H, img_W), np.float32)
    for i in range(img_H):
        for j in range(img_W):
            empty_image[i, j] = src_img[i, j][0]*0.3 + src_img[i, j][1]*0.59 + src_img[i, j][2]*0.11
    return empty_image.astype(np.uint8)

if __name__ == '__main__':
    src_img = cv.imread("lenna.png")
    cv.imshow("src_img", src_img)
    src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    gray_img = rgb2gray(src_img)
    cv.imshow("gray_img", gray_img)
    cv.waitKey()