import cv2
import matplotlib.pyplot as plt
import numpy as np

from noise import add_gaussian_noise, blur_image, exp_kernel
from restore import cls_filter


def main():
    image = cv2.imread("data/DIP.bmp", cv2.IMREAD_GRAYSCALE)
    kernel = exp_kernel(size=7, D0=120)
    H = np.fft.fft2(np.fft.ifftshift(kernel), s=image.shape)
    blurred = blur_image(image, kernel)
    blurred = add_gaussian_noise(blurred, mean=0, var=8)

    cls_restored = cls_filter(blurred, H, s=0.001)

    plt.figure(figsize=(10, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(blurred, cmap="gray")
    plt.title("Blurred image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cls_restored, cmap="gray")
    plt.title("Restored image (CLS filter)")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("result/task4.png")
    plt.show()


if __name__ == "__main__":
    main()
