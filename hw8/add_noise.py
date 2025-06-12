import cv2
import matplotlib.pyplot as plt
import numpy as np


def add_gaussian_noise(image, mean=0, sigma=10):
    noise = np.random.normal(mean, sigma, image.shape).astype(np.float32)
    noisy_image = image.astype(np.float32) + noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image


def main():
    img = cv2.imread("./digital_image_hw8_img1.png", cv2.IMREAD_GRAYSCALE)

    # 添加轻度高斯噪声
    light_noise_img = add_gaussian_noise(img, mean=0, sigma=10)

    # 添加重度高斯噪声
    heavy_noise_img = add_gaussian_noise(img, mean=0, sigma=20)

    cv2.imwrite("digital_image_hw8_img2.png", light_noise_img)
    cv2.imwrite("digital_image_hw8_img3.png", heavy_noise_img)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.title("Original image")
    plt.imshow(img, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title("Image with light noise")
    plt.imshow(light_noise_img, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("Image with heavy noise")
    plt.imshow(heavy_noise_img, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("digital_image_hw8_img_noise.png")
    plt.show()


if __name__ == "__main__":
    main()
