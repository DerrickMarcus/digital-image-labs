import cv2
import matplotlib.pyplot as plt
import numpy as np

from noise import add_gaussian_noise, blur_image, motion_kernel
from restore import inverse_filter, wiener_filter


def main():
    image = cv2.imread("data/DIP.bmp", cv2.IMREAD_GRAYSCALE)

    size = 21
    angle = 90
    psf = motion_kernel(size, angle)

    blurred = blur_image(image, psf)

    blurred = add_gaussian_noise(blurred, mean=0, var=8)

    H = np.fft.fft2(np.fft.ifftshift(psf), s=image.shape)

    inv_restored = inverse_filter(blurred, H, k=0.8, d=0.1, eps=1e-3)

    wiener_restored = wiener_filter(blurred, H, K=0.01)

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Original image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(blurred, cmap="gray")
    plt.title("Blurred image")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(inv_restored, cmap="gray")
    plt.title("Restored image (Inverse filter)")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(wiener_restored, cmap="gray")
    plt.title("Restored image (Wiener filter)")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("result/task3.png")
    plt.show()


if __name__ == "__main__":
    main()
