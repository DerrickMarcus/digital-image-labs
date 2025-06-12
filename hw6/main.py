import cv2
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2025)


def add_gaussian_noise(image, mu=0, sigma=20):
    image = image.astype(np.float32)
    noise = np.random.normal(mu, sigma, image.shape).astype(np.float32)
    output = image + noise
    output = np.clip(output, 0, 255).astype(np.uint8)
    return output


def add_salt_pepper_noise(image, prob=0.05):
    output = np.copy(image)
    rnd = np.random.rand(image.shape[0], image.shape[1])
    output[rnd < prob / 2] = 0
    output[rnd > 1 - prob / 2] = 255
    output = output.astype(np.uint8)
    return output


def compute_psnr(original, filtered, n=8):
    mse = np.mean((original - filtered) ** 2)
    if mse == 0:
        psnr = float("inf")
    else:
        psnr = 20 * np.log10((2**n - 1) ** 2 / np.sqrt(mse))
    return psnr


def laplacian_sharpen(image):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], dtype=np.float32)
    # kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
    output = cv2.filter2D(image, -1, kernel)
    return output


def sobel_sharpen(image):
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float32)
    gradient_x = cv2.filter2D(image, -1, kernel_x)
    gradient_y = cv2.filter2D(image, -1, kernel_y)
    output = cv2.addWeighted(gradient_x, 0.5, gradient_y, 0.5, 0)
    return output


def log_sharpen(image):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    kernel = np.array(
        [
            [0, 0, -1, 0, 0],
            [0, -1, -2, -1, 0],
            [-1, -2, 16, -2, -1],
            [0, -1, -2, -1, 0],
            [0, 0, -1, 0, 0],
        ],
        dtype=np.float32,
    )
    output = cv2.filter2D(blurred, -1, kernel)
    return output


def main():
    image_path = "./img.jpg"
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    image_gaussian = add_gaussian_noise(image, mu=0, sigma=25)
    image_salt = add_salt_pepper_noise(image, prob=0.05)

    plt.figure(figsize=(12, 8))

    plt.subplot(1, 3, 1)
    plt.title("Original image")
    plt.imshow(image, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.title("Image with gaussian noise")
    plt.imshow(image_gaussian, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.title("Image with salt&pepper noise")
    plt.imshow(image_salt, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("./img_noise.jpg")
    plt.show()

    image_gaussian_median = cv2.medianBlur(image_gaussian, ksize=3)
    image_gaussian_gaussian = cv2.GaussianBlur(image_gaussian, ksize=(3, 3), sigmaX=0)
    psnr_gaussian_median = compute_psnr(image, image_gaussian_median)
    psnr_gaussian_gaussian = compute_psnr(image, image_gaussian_gaussian)
    print(
        f"Image with gaussian noise, median filtered, PSNR: {psnr_gaussian_median:.2f} dB"
    )
    print(
        f"Image with gaussian noise, gaussian filtered, PSNR: {psnr_gaussian_gaussian:.2f} dB"
    )

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.title("Original image")
    plt.imshow(image, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.title("Image with gaussian noise")
    plt.imshow(image_gaussian, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.title("Image with gaussian noise, after median filter")
    plt.imshow(image_gaussian_median, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.title("Image with gaussian noise, after gaussian filter")
    plt.imshow(image_gaussian_gaussian, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("./img_gaussian_filtered.jpg")
    plt.show()

    image_salt_median = cv2.medianBlur(image_salt, ksize=3)
    image_salt_gaussian = cv2.GaussianBlur(image_salt, ksize=(3, 3), sigmaX=0)
    psnr_salt_median = compute_psnr(image, image_salt_median)
    psnr_salt_gaussian = compute_psnr(image, image_salt_gaussian)
    print(
        f"Image with salt&pepper noise, median filtered, PSNR: {psnr_salt_median:.2f} dB"
    )
    print(
        f"Image with salt&pepper noise, gaussian filtered, PSNR: {psnr_salt_gaussian:.2f} dB"
    )

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.title("Original image")
    plt.imshow(image, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.title("Image with salt&pepper noise")
    plt.imshow(image_salt, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.title("Image with salt&pepper noise, after median filter")
    plt.imshow(image_salt_median, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.title("Image with salt&pepper noise, after gaussian filter")
    plt.imshow(image_salt_gaussian, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("./img_salt_filtered.jpg")
    plt.show()

    image_laplacian = laplacian_sharpen(image)
    image_sobel = sobel_sharpen(image)
    image_log = log_sharpen(image)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.title("Original image")
    plt.imshow(image, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.title("Laplacian sharpened image")
    plt.imshow(image_laplacian, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.title("Sobel sharpened image")
    plt.imshow(image_sobel, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.title("LoG sharpened image")
    plt.imshow(image_log, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("./img_sharpened.jpg")
    plt.show()


if __name__ == "__main__":
    main()
