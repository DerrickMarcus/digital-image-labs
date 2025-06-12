import cv2
import matplotlib.pyplot as plt
import numpy as np


def pseudo_color_line(gray_img):
    def f_r(p):
        if p < 64:
            return 0
        elif p > 128:
            return 255
        else:
            return 255 / 64 * (p - 64)

    def f_g(p):
        if p < 64:
            return 255
        elif p > 128:
            return 0
        else:
            return 255 / 64 * (128 - p)

    def f_b(p):
        if p < 64:
            return 255 / 64 * p
        elif p > 192:
            return 255 / 63 * (255 - p)
        else:
            return 255

    # 构建 LUT 映射
    lut_r = np.array([np.clip(f_r(i), 0, 255) for i in range(256)], dtype=np.uint8)
    lut_g = np.array([np.clip(f_g(i), 0, 255) for i in range(256)], dtype=np.uint8)
    lut_b = np.array([np.clip(f_b(i), 0, 255) for i in range(256)], dtype=np.uint8)

    r = cv2.LUT(gray_img, lut_r)
    g = cv2.LUT(gray_img, lut_g)
    b = cv2.LUT(gray_img, lut_b)
    color_img = cv2.merge([b, g, r])
    return color_img


def pseudo_color_sine(gray_img, T, delta):
    def f_r(p):
        return (1 + np.sin(2 * np.pi / T * p)) * 255 / 2

    def f_g(p):
        return (1 + np.sin(2 * np.pi / T * (p - delta))) * 255 / 2

    def f_b(p):
        return (1 + np.sin(2 * np.pi / T * (p - 2 * delta))) * 255 / 2

    lut_r = np.array([np.clip(f_r(i), 0, 255) for i in range(256)], dtype=np.uint8)
    lut_g = np.array([np.clip(f_g(i), 0, 255) for i in range(256)], dtype=np.uint8)
    lut_b = np.array([np.clip(f_b(i), 0, 255) for i in range(256)], dtype=np.uint8)

    r = cv2.LUT(gray_img, lut_r)
    g = cv2.LUT(gray_img, lut_g)
    b = cv2.LUT(gray_img, lut_b)
    color_img = cv2.merge([b, g, r])
    return color_img


def main(img_path):
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Image read failed. Please check the file path.")
        return

    # 折线变换
    line_result = pseudo_color_line(image)
    plt.figure(figsize=(5, 5))
    plt.imshow(cv2.cvtColor(line_result, cv2.COLOR_BGR2RGB))
    plt.title("Pseudo color transform: line")
    plt.axis("off")
    plt.savefig(img_path.rsplit(".", 1)[0] + "_line" + "." + img_path.rsplit(".", 1)[1])
    plt.show()

    # 正弦函数变换
    # delta 大小对伪彩色增强的影响
    sine_result_1 = pseudo_color_sine(image, T=255, delta=255 / 3)
    sine_result_2 = pseudo_color_sine(image, T=255, delta=255 / 6)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(sine_result_1, cv2.COLOR_BGR2RGB))
    plt.title("Pseudo color transform: sine\nT=255, delta=255/3")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(sine_result_2, cv2.COLOR_BGR2RGB))
    plt.title("Pseudo color transform: sine\nT=255, delta=255/6")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(
        img_path.rsplit(".", 1)[0] + "_sine_1" + "." + img_path.rsplit(".", 1)[1]
    )
    plt.show()

    # T 大小对伪彩色增强的影响
    sine_result_3 = pseudo_color_sine(image, T=255, delta=255 / 3)
    sine_result_4 = pseudo_color_sine(image, T=255 / 2, delta=255 / 2 / 3)
    sine_result_5 = pseudo_color_sine(image, T=255 / 4, delta=255 / 4 / 3)
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(sine_result_3, cv2.COLOR_BGR2RGB))
    plt.title("Pseudo color transform: sine\nT=255, delta=T/3")
    plt.axis("off")
    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(sine_result_4, cv2.COLOR_BGR2RGB))
    plt.title("Pseudo color transform: sine\nT=255/2, delta=T/3")
    plt.axis("off")
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(sine_result_5, cv2.COLOR_BGR2RGB))
    plt.title("Pseudo color transform: sine\nT=255/4, delta=T/3")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(
        img_path.rsplit(".", 1)[0] + "_sine_2" + "." + img_path.rsplit(".", 1)[1]
    )
    plt.show()


if __name__ == "__main__":
    main("./digital_image_hw9_img21.jpg")
    main("./digital_image_hw9_img22.jpg")
