import cv2
import matplotlib.pyplot as plt
import numpy as np


def ideal_highpass(fshift, D0):
    rows, cols = fshift.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.ones((rows, cols), np.float32)

    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            if d <= D0:
                mask[i, j] = 0
    filtered = fshift * mask
    output = np.abs(np.fft.ifft2(filtered))
    return output


def butterworth_highpass(fshift, D0, n):
    rows, cols = fshift.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.float32)

    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            if d == 0:
                mask[i, j] = 0
            else:
                mask[i, j] = 1 / (1 + (D0 / d) ** (2 * n))
    filtered = fshift * mask
    output = np.abs(np.fft.ifft2(filtered))
    return output


def chebyshev_highpass(fshift, D0, epsilon, n):
    rows, cols = fshift.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.float32)

    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            if d == 0:
                mask[i, j] = 0
            else:
                if d >= D0:
                    Tn = np.cos(n * np.arccos(D0 / d))
                else:
                    Tn = np.cosh(n * np.arccosh(D0 / d))
                mask[i, j] = 1 / np.sqrt(1 + epsilon**2 * Tn**2)
    filtered = fshift * mask
    output = np.abs(np.fft.ifft2(filtered))
    return output


def main():
    img = cv2.imread("./digital_image_hw7_circuit.png", cv2.IMREAD_GRAYSCALE)
    fshift = np.fft.fftshift(np.fft.fft2(img))

    ideal_filtered = ideal_highpass(fshift, D0=30)
    butterworth_filtered = butterworth_highpass(fshift, D0=30, n=2)
    chebyshev_filtered = chebyshev_highpass(fshift, D0=30, epsilon=1, n=2)

    plt.figure(figsize=(10, 8))

    # 原始图像
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original image")
    plt.axis("off")

    # 理想高通滤波器
    plt.subplot(2, 2, 2)
    plt.imshow(ideal_filtered, cmap="gray")
    plt.title("Ideal highpass filter, D0=30")
    plt.axis("off")

    # 巴特沃斯高通滤波器
    plt.subplot(2, 2, 3)
    plt.imshow(butterworth_filtered, cmap="gray")
    plt.title("Butterworth highpass filter, D0=30, n=2")
    plt.axis("off")

    # 切比雪夫高通滤波器
    plt.subplot(2, 2, 4)
    plt.imshow(chebyshev_filtered, cmap="gray")
    plt.title("Chebyshev highpass filter, D0=30, epsilon=1, n=2")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("./digital_imega_hw7_highpass_comparison.png")
    plt.show()


if __name__ == "__main__":
    main()
