import cv2
import numpy as np


def exp_kernel(size=7, D0=120):
    assert size % 2 == 1, "Kernel size must be odd."
    center = size // 2
    kernel = np.zeros((size, size), dtype=np.float32)

    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            kernel[i, j] = np.exp(np.sqrt(x**2 + y**2) / D0)

    kernel /= np.sum(kernel)
    return kernel


def motion_kernel(size=7, angle=0):
    assert size % 2 == 1, "Kernel size must be odd."
    psf = np.zeros((size, size), dtype=np.float32)
    psf[(size - 1) // 2, :] = 1.0
    M = cv2.getRotationMatrix2D((size / 2 - 0.5, size / 2 - 0.5), angle, 1)
    psf = cv2.warpAffine(psf, M, (size, size))
    psf /= psf.sum()
    return psf


def blur_image(image, kernel):
    output = cv2.filter2D(image, ddepth=-1, kernel=kernel)
    return output


def add_gaussian_noise(image, mean=0, var=25):
    sigma = np.sqrt(var)
    noise = np.random.normal(mean, sigma, image.shape).astype(np.float32)

    output = image.astype(np.float32) + noise
    output = np.clip(output, 0, 255).astype(np.uint8)
    return output
