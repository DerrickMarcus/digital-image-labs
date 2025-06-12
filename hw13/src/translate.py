import cv2
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 指定中文字体为黑体
plt.rcParams["axes.unicode_minus"] = False  # 正确显示负号


def main():
    img = cv2.imread("images/Lena.bmp", cv2.IMREAD_GRAYSCALE)

    h, w = img.shape

    # 向右平移50像素，向下平移30像素
    tx, ty = 50, 30
    M = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)

    translated = cv2.warpAffine(
        img, M, (w, h), None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (0,)
    )

    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("原始图像")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(translated, cmap="gray")
    plt.title("平移后的图像")
    plt.axis("off")

    plt.savefig("images/translate.png", dpi=300)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
