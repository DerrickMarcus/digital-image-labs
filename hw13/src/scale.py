import cv2
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 黑体
plt.rcParams["axes.unicode_minus"] = False  # 负号正常显示


def main():
    img = cv2.imread("images/Lena.bmp", cv2.IMREAD_GRAYSCALE)
    h, w = img.shape

    # 放缩比例
    sx, sy = 1.4, 0.7
    M = np.array([[sx, 0, 0], [0, sy, 0]], dtype=np.float32)

    new_w, new_h = int(w * sx), int(h * sy)
    # 最近邻插值
    scaled_1 = cv2.warpAffine(
        img,
        M,
        (new_w, new_h),
        flags=cv2.INTER_NEAREST,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0,),
    )
    # 双线性插值
    scaled_2 = cv2.warpAffine(
        img,
        M,
        (new_w, new_h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0,),
    )

    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(scaled_1, cmap="gray")
    plt.title(f"放缩 sx:{sx}, sy:{sy} + 最近邻插值")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(scaled_2, cmap="gray")
    plt.title(f"放缩 sx:{sx}, sy:{sy} + 双线性插值")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("images/scaled.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
