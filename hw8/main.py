import cv2
import matplotlib.pyplot as plt
import numpy as np


def roberts_edge(image):
    kernel_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
    kernel_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)

    grad_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)
    grad_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)

    output = cv2.magnitude(grad_x, grad_y)
    output = cv2.normalize(output, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return output


def sobel_edge(image):
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    output = cv2.magnitude(grad_x, grad_y)
    output = cv2.normalize(output, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return output


def laplace_edge(image):
    output = cv2.Laplacian(image, cv2.CV_64F, ksize=3)
    output = cv2.convertScaleAbs(output)
    return output


def hough_transform(image, edge):
    lines = cv2.HoughLinesP(
        edge,
        rho=1,  # 距离精度
        theta=np.pi / 180,  # 角度精度
        threshold=80,  # 阈值
        minLineLength=60,  # 最小可接受线段长度
        maxLineGap=5,  # 最大线段间隔
    )

    image_lines = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # 画红色线，线条宽度为1像素
            cv2.line(image_lines, (x1, y1), (x2, y2), (0, 0, 255), 1)
    return image_lines


def main():
    image_path = "./digital_image_hw8_img3.png"
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    result_roberts = roberts_edge(image)
    result_sobel = sobel_edge(image)
    result_laplace = laplace_edge(image)
    result_canny = cv2.Canny(image, 100, 200)

    plt.figure()

    plt.subplot(2, 3, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Original image")
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.imshow(result_roberts, cmap="gray")
    plt.title("Roberts operator")
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.imshow(result_sobel, cmap="gray")
    plt.title("Sobel operator")
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.imshow(result_laplace, cmap="gray")
    plt.title("Laplace operator")
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.imshow(result_canny, cmap="gray")
    plt.title("Canny operator")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("./digital_image_hw8_edge3.png")
    plt.show()

    # 对 Canny 算子边缘检测结果进行 Hough 变换
    image_lines = hough_transform(image, result_canny)

    plt.figure()

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image_lines, cv2.COLOR_BGR2RGB))
    plt.title("Hough line detection (Canny edges)")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("./digital_image_hw8_line31.png")
    plt.show()


if __name__ == "__main__":
    main()
