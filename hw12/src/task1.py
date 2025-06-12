import cv2
import matplotlib.pyplot as plt
import numpy as np

from noise import blur_image, exp_kernel
from restore import inverse_filter


def main():
    image = cv2.imread("data/DIP.bmp", cv2.IMREAD_GRAYSCALE)

    kernel = exp_kernel(size=7, D0=120)
    blurred_image = blur_image(image, kernel)

    H = np.fft.fft2(np.fft.ifftshift(kernel), s=image.shape)
    restored_image = inverse_filter(blurred_image, H, k=0.8, d=0.1, eps=0)

    plt.figure(figsize=(15, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Original image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(blurred_image, cmap="gray")
    plt.title("Blurred image")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(restored_image, cmap="gray")
    plt.title("Restored image")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("result/task1.png")
    plt.show()


if __name__ == "__main__":
    main()
