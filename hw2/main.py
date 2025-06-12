import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def decompose_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)

    r = image_array[:, :, 0]
    g = image_array[:, :, 1]
    b = image_array[:, :, 2]

    c = 255 - r
    m = 255 - g
    y = 255 - b

    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    i = (r_norm + g_norm + b_norm) / 3.0

    min_rgb = np.minimum(np.minimum(r_norm, g_norm), b_norm)
    s = 1 - (3.0 / (r_norm + g_norm + b_norm + 1e-6)) * min_rgb

    numerator = 0.5 * ((r_norm - g_norm) + (r_norm - b_norm))
    denominator = (
        np.sqrt((r_norm - g_norm) ** 2 + (r_norm - b_norm) * (g_norm - b_norm)) + 1e-6
    )
    h = np.arccos(numerator / denominator)
    h[b_norm > g_norm] = 2 * np.pi - h[b_norm > g_norm]
    h = h / (2 * np.pi)

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 3, 1)
    plt.imshow(r, cmap="gray")
    plt.title("Red Channel")
    plt.axis("off")

    plt.subplot(3, 3, 2)
    plt.imshow(g, cmap="gray")
    plt.title("Green Channel")
    plt.axis("off")

    plt.subplot(3, 3, 3)
    plt.imshow(b, cmap="gray")
    plt.title("Blue Channel")
    plt.axis("off")

    plt.subplot(3, 3, 4)
    plt.imshow(c, cmap="gray")
    plt.title("Cyan Channel")
    plt.axis("off")

    plt.subplot(3, 3, 5)
    plt.imshow(m, cmap="gray")
    plt.title("Magenta Channel")
    plt.axis("off")

    plt.subplot(3, 3, 6)
    plt.imshow(y, cmap="gray")
    plt.title("Yellow Channel")
    plt.axis("off")

    plt.subplot(3, 3, 7)
    plt.imshow(h, cmap="hsv")
    plt.title("Hue Channel")
    plt.axis("off")

    plt.subplot(3, 3, 8)
    plt.imshow(s, cmap="gray")
    plt.title("Saturation Channel")
    plt.axis("off")

    plt.subplot(3, 3, 9)
    plt.imshow(i, cmap="gray")
    plt.title("Intensity Channel")
    plt.axis("off")

    plt.suptitle("Image Decomposition")
    plt.tight_layout()

    output_filename = image_path.rsplit(".", 1)[0] + "_decomposed.jpg"
    plt.savefig(output_filename, bbox_inches="tight", dpi=300)
    print(f"Decomposed image saved as: {output_filename}")

    plt.show()


def main():
    image_path = "./img1.jpg"
    decompose_image(image_path)


if __name__ == "__main__":
    main()
