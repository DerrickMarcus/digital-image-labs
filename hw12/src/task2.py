import cv2
import matplotlib.pyplot as plt
import numpy as np

from noise import add_gaussian_noise, blur_image, exp_kernel
from restore import inverse_filter, wiener_filter


def main():
    image = cv2.imread("data/DIP.bmp", cv2.IMREAD_GRAYSCALE)
    kernel = exp_kernel(size=7, D0=120)
    H = np.fft.fft2(np.fft.ifftshift(kernel), s=image.shape)
    blurred = blur_image(image, kernel)

    noisy_1 = add_gaussian_noise(blurred, mean=0, var=8)
    noisy_2 = add_gaussian_noise(blurred, mean=0, var=16)
    noisy_3 = add_gaussian_noise(blurred, mean=0, var=24)

    inv_1 = inverse_filter(noisy_1, H, k=0.8, d=0.1, eps=0)
    inv_2 = inverse_filter(noisy_2, H, k=0.8, d=0.1, eps=0)
    inv_3 = inverse_filter(noisy_3, H, k=0.8, d=0.1, eps=0)

    wiener_1 = wiener_filter(noisy_1, H, K=0.02)
    wiener_2 = wiener_filter(noisy_2, H, K=0.02)
    wiener_3 = wiener_filter(noisy_3, H, K=0.02)

    plt.figure(figsize=(12, 12))
    plt.subplot(3, 3, 1)
    plt.imshow(noisy_1, cmap="gray")
    plt.title("Noisy image, Var = 8")
    plt.axis("off")

    plt.subplot(3, 3, 2)
    plt.imshow(inv_1, cmap="gray")
    plt.title("Inverse filter")
    plt.axis("off")

    plt.subplot(3, 3, 3)
    plt.imshow(wiener_1, cmap="gray")
    plt.title("Wiener filter")
    plt.axis("off")

    plt.subplot(3, 3, 4)
    plt.imshow(noisy_2, cmap="gray")
    plt.title("Noisy image, Var = 16")
    plt.axis("off")

    plt.subplot(3, 3, 5)
    plt.imshow(inv_2, cmap="gray")
    plt.title("Inverse filter")
    plt.axis("off")

    plt.subplot(3, 3, 6)
    plt.imshow(wiener_2, cmap="gray")
    plt.title("Wiener filter")
    plt.axis("off")

    plt.subplot(3, 3, 7)
    plt.imshow(noisy_3, cmap="gray")
    plt.title("Noisy image, Var = 24")
    plt.axis("off")

    plt.subplot(3, 3, 8)
    plt.imshow(inv_3, cmap="gray")
    plt.title("Inverse filter")
    plt.axis("off")

    plt.subplot(3, 3, 9)
    plt.imshow(wiener_3, cmap="gray")
    plt.title("Wiener filter")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("result/task2.png")
    plt.show()


if __name__ == "__main__":
    main()
