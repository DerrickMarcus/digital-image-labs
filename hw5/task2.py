import cv2
import matplotlib.pyplot as plt
import numpy as np


def compute_cdf(channel):
    """计算单通道的累积分布函数

    Args:
        channel (np.ndarray): 单通道图像

    Returns:
        np.ndarray: 累积分布函数
    """
    hist = np.zeros(256, dtype=int)
    height, width = channel.shape
    for i in range(height):
        for j in range(width):
            hist[channel[i, j]] += 1

    pdf = hist / (height * width)

    cdf = np.zeros(256, dtype=float)
    cdf[0] = pdf[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + pdf[i]

    return cdf


def channel_specification(image, template):
    """对单个通道进行规定化

    Args:
        image (np.ndarray): 原图像通道
        template (np.ndarray): 模板图像通道

    Returns:
        np.ndarray: 规定化后的通道
    """
    cdf_image = compute_cdf(image)
    cdf_template = compute_cdf(template)

    mapping = np.zeros(256, dtype=int)
    for i in range(256):
        min_diff = float("inf")
        argmin_j = 0
        for j in range(256):
            diff = abs(cdf_image[i] - cdf_template[j])
            if diff < min_diff:
                min_diff = diff
                argmin_j = j
        mapping[i] = argmin_j

    new_channel = np.zeros_like(image)
    new_channel = mapping[image].astype(np.uint8)

    return new_channel


def histogram_specification(image_path, template_path):
    """根据模板图像对目标图像进行直方图规定化

    Args:
        image_path (str): 原图像路径
        template_path (str): 模板图像路径
    """
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    image_b, image_g, image_r = cv2.split(image)
    template_b, template_g, template_r = cv2.split(template)

    new_b = channel_specification(image_b, template_b)
    new_g = channel_specification(image_g, template_g)
    new_r = channel_specification(image_r, template_r)

    new_image = cv2.merge([new_b, new_g, new_r])
    new_path = image_path.rsplit(".", 1)[0] + "_new.jpg"
    cv2.imwrite(new_path, new_image)
    print(f"save the image after histogram specification to: {new_path}")

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    plt.title("Specified image")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    total_hist = np.zeros(256)
    for channel, color in enumerate(["b", "g", "r"]):
        hist = cv2.calcHist([image], [channel], None, [256], [0, 256])
        plt.plot(hist, color=color)
        total_hist += hist.flatten()
    plt.bar(range(256), total_hist, color="k", alpha=0.5)
    plt.title("Original histogram")
    plt.xlabel("Pixel level")
    plt.ylabel("Number of pixels")

    plt.subplot(2, 2, 4)
    total_hist = np.zeros(256)

    for channel, color in enumerate(["b", "g", "r"]):
        hist = cv2.calcHist([new_image], [channel], None, [256], [0, 256])
        plt.plot(hist, color=color)
        total_hist += hist.flatten()
    plt.bar(range(256), total_hist, color="k", alpha=0.5)
    plt.title("Specified histogram")
    plt.xlabel("Pixel level")
    plt.ylabel("Number of pixels")

    plt.tight_layout()

    compare_path = image_path.rsplit(".", 1)[0] + "_compare.jpg"
    plt.savefig(compare_path)
    print(f"save the comparison of original and specified image to: {compare_path}")

    plt.show()


def main():
    histogram_specification("./img1.jpg", "./img2.jpg")
    histogram_specification("./img2.jpg", "./img1.jpg")


if __name__ == "__main__":
    main()
