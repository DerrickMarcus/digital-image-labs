import cv2
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


def main():
    img = cv2.imread("images/Lena.bmp", cv2.IMREAD_GRAYSCALE)
    h, w = img.shape

    # 定义透视变换的四对点
    # 原图中的矩形区域四个顶点
    src_pts = np.float32([[50, 50], [w - 50, 50], [w - 50, h - 50], [50, h - 50]])
    # 透视后映射到的四边形顶点
    dst_pts = np.float32([[10, 100], [w - 100, 50], [w - 50, h - 100], [100, h - 50]])

    # 计算透视矩阵
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)

    # 最近邻插值
    warped_1 = cv2.warpPerspective(
        img,
        M,
        (w, h),
        flags=cv2.INTER_NEAREST,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0,),
    )
    wraped_2 = cv2.warpPerspective(
        img,
        M,
        (w, h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0,),
    )

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap="gray")
    plt.scatter(src_pts[:, 0], src_pts[:, 1], c="r")
    for i, pt in enumerate(src_pts):
        plt.text(pt[0] + 5, pt[1] + 5, f"{i + 1}", color="red")
    plt.title("原始图像")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(warped_1, cmap="gray")
    plt.scatter(dst_pts[:, 0], dst_pts[:, 1], c="r")
    for i, pt in enumerate(dst_pts):
        plt.text(pt[0] + 5, pt[1] + 5, f"{i + 1}", color="red")
    plt.title("透视变换图像+最近邻插值")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(wraped_2, cmap="gray")
    plt.scatter(dst_pts[:, 0], dst_pts[:, 1], c="r")
    for i, pt in enumerate(dst_pts):
        plt.text(pt[0] + 5, pt[1] + 5, f"{i + 1}", color="red")
    plt.title("透视变换图像+双线性插值")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("images/perspective.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
