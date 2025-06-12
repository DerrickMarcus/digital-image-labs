import cv2
import matplotlib.pyplot as plt
import numpy as np


def ideal_lowpass(fshift, D0):
    rows, cols = fshift.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.float32)

    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            if d <= D0:
                mask[i, j] = 1
    filtered = fshift * mask
    output = np.abs(np.fft.ifft2(filtered))
    return output


def butterworth_lowpass(fshift, D0, n):
    rows, cols = fshift.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.float32)

    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            mask[i, j] = 1 / (1 + (d / D0) ** (2 * n))
    filtered = fshift * mask
    output = np.abs(np.fft.ifft2(filtered))
    return output


def chebyshev_lowpass(fshift, D0, epsilon, n):
    rows, cols = fshift.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.float32)

    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            if d == 0:
                mask[i, j] = 1
            else:
                if d >= D0:
                    Tn = np.cosh(n * np.arccosh(d / D0))
                else:
                    Tn = np.cos(n * np.arccos(d / D0))
                mask[i, j] = 1 / np.sqrt(1 + epsilon**2 * Tn**2)
    filtered = fshift * mask
    output = np.abs(np.fft.ifft2(filtered))
    return output


def main():
    img = cv2.imread("./digital_image_hw7_lena.png", cv2.IMREAD_GRAYSCALE)
    fshift = np.fft.fftshift(np.fft.fft2(img))

    ideal_filtered = ideal_lowpass(fshift, D0=30)
    butterworth_filtered = butterworth_lowpass(fshift, D0=30, n=2)
    chebyshev_filtered = chebyshev_lowpass(fshift, D0=30, epsilon=1, n=2)

    plt.figure(figsize=(10, 8))

    # 原始图像
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original image")
    plt.axis("off")

    # 理想低通滤波器
    plt.subplot(2, 2, 2)
    plt.imshow(ideal_filtered, cmap="gray")
    plt.title("Ideal lowpass filter, D0=30")
    plt.axis("off")

    # 巴特沃斯低通滤波器
    plt.subplot(2, 2, 3)
    plt.imshow(butterworth_filtered, cmap="gray")
    plt.title("Butterworth lowpass filter, D0=30, n=2")
    plt.axis("off")

    # 切比雪夫低通滤波器
    plt.subplot(2, 2, 4)
    plt.imshow(chebyshev_filtered, cmap="gray")
    plt.title("Chebyshev lowpass filter, D0=30, epsilon=1, n=2")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("./digital_image_hw7_lowpass_comparision.png")
    plt.show()

    # 研究截止频率对巴特沃斯滤波效果的影响
    D0_values = [10, 30, 50, 70, 90, 110]
    plt.figure(figsize=(10, 8))
    plt.suptitle("Effect of cutoff frequency on butterworth lowpass filter")
    for i, D0 in enumerate(D0_values):
        butterworth_filtered = butterworth_lowpass(fshift, D0, n=2)
        plt.subplot(2, len(D0_values) // 2, i + 1)
        plt.imshow(butterworth_filtered, cmap="gray")
        plt.title(f"D0={D0}")
        plt.axis("off")

    plt.tight_layout()
    plt.savefig("./digital_image_hw7_butterworth_d0.png")
    plt.show()

    # 研究阶数对巴特沃斯滤波效果的影响
    n_values = [1, 2, 3, 4, 5, 6]
    plt.figure(figsize=(10, 8))
    plt.suptitle("Effect of order on butterworth lowpass filter")
    for i, n in enumerate(n_values):
        butterworth_filtered = butterworth_lowpass(fshift, 30, n)
        plt.subplot(2, len(n_values) // 2, i + 1)
        plt.imshow(butterworth_filtered, cmap="gray")
        plt.title(f"n={n}")
        plt.axis("off")

    plt.tight_layout()
    plt.savefig("./digital_image_hw7_butterworth_n.png")
    plt.show()


if __name__ == "__main__":
    main()
