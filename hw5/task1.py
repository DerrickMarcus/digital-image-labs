import cv2
import matplotlib.pyplot as plt
import numpy as np


def histogram_equalization(image_path):
    """对图像进行直方图均衡化

    Args:
        image_path (str): 输入图像的路径
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = image.shape

    # 统计直方图
    hist = np.zeros(256, dtype=int)
    for i in range(height):
        for j in range(width):
            hist[image[i, j]] += 1

    # 归一化得到概率密度函数 PDF
    pdf = hist / (height * width)

    # 计算累积分布函数 CDF
    cdf = np.zeros(256, dtype=float)
    cdf[0] = pdf[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + pdf[i]

    # 映射回[0,255]
    pixel_new = (cdf * 255).astype("uint8")

    # 生成均衡化图像
    image_equalized = np.zeros_like(image)
    image_equalized = pixel_new[image]

    # 计算均衡化后的直方图
    hist_equalized = np.zeros(256, dtype=int)
    for i in range(height):
        for j in range(width):
            hist_equalized[image_equalized[i, j]] += 1

    new_path = image_path.rsplit(".", 1)[0] + "_new.png"
    cv2.imwrite(new_path, image_equalized)
    print(f"save the image after histogram equalization to: {new_path}")

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Original image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(image_equalized, cmap="gray")
    plt.title("Equalized image")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.bar(range(256), hist, color="black")
    plt.title("Original histogram")
    plt.xlabel("Gray level")
    plt.ylabel("Number of pixels")

    plt.subplot(2, 2, 4)
    plt.bar(range(256), hist_equalized, color="black")
    plt.title("Equalized histogram")
    plt.xlabel("Gray level")
    plt.ylabel("Number of pixels")

    plt.tight_layout()

    compare_path = image_path.rsplit(".", 1)[0] + "_compare.png"
    plt.savefig(compare_path)
    print(f"save the comparison of original and equalized image to: {compare_path}")

    plt.show()


def main():
    histogram_equalization("./img1.png")
    histogram_equalization("./img2.png")


if __name__ == "__main__":
    main()
