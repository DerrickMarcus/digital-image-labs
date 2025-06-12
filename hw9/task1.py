import cv2
import matplotlib.pyplot as plt
import numpy as np


def iterative_threshold(img, eps=1):
    prev_T = img.mean()
    while True:
        G1 = img[img > prev_T]
        G2 = img[img <= prev_T]
        if len(G1) == 0 or len(G2) == 0:
            break
        m1 = G1.mean()
        m2 = G2.mean()
        T = (m1 + m2) / 2
        if abs(prev_T - T) < eps:
            break
        prev_T = T
    _, binary = cv2.threshold(img, prev_T, 255, cv2.THRESH_BINARY)
    print(f"Iterative threshold: {prev_T}")
    return binary


def main():
    image = cv2.imread("./digital_image_hw9_img1.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Image read failed. Please check the file path.")
        return

    # 迭代阈值法
    iterative_result = iterative_threshold(image)

    # 局部阈值法（自适应阈值）
    local_result = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=11, C=2
    )

    # 大津法
    thres, otsu_result = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    print(f"Otsu's threshold: {thres}")

    titles = [
        "Original Image",
        "Iterative threshold",
        "Local threshold",
        "Otsu Algorithm",
    ]
    images = [image, iterative_result, local_result, otsu_result]

    plt.figure(figsize=(12, 8))
    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i], cmap="gray")
        plt.title(titles[i], color="red")
        plt.axis("off")
        # if i != 0:
        #     cv2.imwrite(f"./digital_image_hw9_img1_segment_{i}.jpg", images[i])

    plt.tight_layout()
    plt.savefig("./digital_image_hw9_img1_result_1.jpg")
    plt.show()

    # 膨胀与腐蚀
    kernel = np.ones((3, 3), dtype=np.uint8)
    iterative_result = cv2.morphologyEx(iterative_result, cv2.MORPH_CLOSE, kernel)
    local_result = cv2.morphologyEx(local_result, cv2.MORPH_CLOSE, kernel)
    otsu_result = cv2.morphologyEx(otsu_result, cv2.MORPH_CLOSE, kernel)

    images = [image, iterative_result, local_result, otsu_result]

    plt.figure(figsize=(12, 8))
    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i], cmap="gray")
        plt.title(titles[i], color="red")
        plt.axis("off")
        # if i != 0:
        #     cv2.imwrite(f"./digital_image_hw9_img1_segment_{i + 3}.jpg", images[i])

    plt.tight_layout()
    plt.savefig("./digital_image_hw9_img1_result_2.jpg")
    plt.show()


if __name__ == "__main__":
    main()
