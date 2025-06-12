import numpy as np


def inverse_filter(image, H_degrade, k=0.5, d=0.1, eps=1e-3):
    G = np.fft.fft2(image.astype(np.float32))
    M = np.where(np.abs(H_degrade) <= d, k, 1.0 / (H_degrade + eps))

    F_hat = G * M
    f_hat = np.fft.ifft2(F_hat)
    f_hat = np.real(f_hat).clip(0, 255).astype(np.uint8)
    return f_hat


def wiener_filter(image, H_degrade, K=0.01):
    G = np.fft.fft2(image.astype(np.float32))
    M = np.conj(H_degrade) / (np.abs(H_degrade) ** 2 + K)

    F_hat = G * M
    f_hat = np.fft.ifft2(F_hat)
    f_hat = np.real(f_hat).clip(0, 255).astype(np.uint8)
    return f_hat


def cls_filter(image, H_degrade, s=0.01):
    G = np.fft.fft2(image.astype(np.float32))

    # fmt: off
    lap = np.array([
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ], dtype=np.float32)
    # fmt: on
    P = np.fft.fft2(np.fft.ifftshift(lap), s=image.shape)

    M = np.conj(H_degrade) / (np.abs(H_degrade) ** 2 + s * np.abs(P) ** 2)

    F_hat = G * M
    f_hat = np.fft.ifft2(F_hat)
    f_hat = np.real(f_hat).clip(0, 255).astype(np.uint8)
    return f_hat
