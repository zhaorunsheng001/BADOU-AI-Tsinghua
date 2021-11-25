import numpy as np
import cv2 as cv


def rgb2bilinear(src_img, out_dim):
    src_h, src_w, src_c = src_img.shape
    res_h, res_w = out_dim[0], out_dim[1]

    if src_h == res_h and src_w == res_w:
        return src_img.copy()

    res_img = np.zeros((res_h, res_w, 3), np.uint8)

    scale_h, scale_w = float(src_h / res_h), float(src_w / res_w)

    for i in range(3):
        for res_x in range(res_h):
            for res_y in range(res_w):

                src_x = res_x*scale_h + 0.5*(scale_h-1)
                src_y = res_y*scale_w + 0.5*(scale_w-1)

                # 找到原始坐标点
                src_x0 = int(np.floor(src_x))  # 14
                src_x1 = min(src_x0 + 1, src_w - 1)  # 15
                src_y0 = int(np.floor(src_y))  # 20
                src_y1 = min(src_y0 + 1, src_h - 1)  # 21

                #计算差值
                tmp_0 = (src_x - src_x0) * src_img[src_y0, src_x1, i] + (src_x1 - src_x) * src_img[src_y0, src_x0, i]
                tmp_1 = (src_x - src_x0) * src_img[src_y1, src_x1, i] + (src_x1 - src_x) * src_img[src_y1, src_x0, i]

                res_img[res_y, res_x, i] = int((src_y1 - src_y) * tmp_0) + int((src_y - src_y0) * tmp_1)

    return res_img



if __name__ == '__main__':
    src_img = cv.imread("lenna.png")
    cv.imshow("src_img", src_img)
    # src_img = cv.cvtColor(src_img, cv.COLOR_BGR2RGB)
    bilinear_img = rgb2bilinear(src_img, (700, 700))
    cv.imshow("bilinear_img", bilinear_img)
    cv.waitKey()