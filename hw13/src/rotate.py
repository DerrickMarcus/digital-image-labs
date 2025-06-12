import cv2
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 黑体
plt.rcParams["axes.unicode_minus"] = False  # 负号正常显示


def main():
    img = cv2.imread("images/Lena.bmp", cv2.IMREAD_GRAYSCALE)
    h, w = img.shape

    # 设置旋转参数：角度、中心、比例
    angle = 30
    center = (w / 2, h / 3)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # 最近邻插值
    rotated_1 = cv2.warpAffine(
        img,
        M,
        (w, h),
        flags=cv2.INTER_NEAREST,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0,),
    )
    # 双线性插值
    rotated_2 = cv2.warpAffine(
        img,
        M,
        (w, h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0,),
    )

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(rotated_1, cmap="gray")
    plt.title(f"旋转 {angle} + 最近邻插值")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(rotated_2, cmap="gray")
    plt.title(f"旋转 {angle} + 双线性插值")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("images/rotated.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
