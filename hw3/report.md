# 《数字图像处理》第3次作业

## 处理思路

源代码路径：`./main.py`。

使用 OpenCV 库。读取图片后，先将蒙版图片和背景图片调整形状为与原图片相同。对于蒙版图片，先用一个较大的高斯核进行高斯模糊处理，可能有助于将边缘部分空缺处的灰度值提高，从而增大白色区域。

将蒙版图片二值化，设定阈值为128，高于128认为是白色，设置为1；低于128认为是黑色，设置为0。然后进行形态学处理：先膨胀后腐蚀，有助于填补缺口、平滑边界部分。膨胀和腐蚀函数可以使用自编版本 `dilate(), erode()`，提供了源图像、卷积核、迭代次数三个参数，也可以直接使用 cv2 库中内置的函数 `cv2.dilate(), cv2.erode()`。对于膨胀操作，每一个像素点作为卷积核的中心，卷积核范围内的像素中存在白色像素时，就将这个像素点置为白色。对于腐蚀操作，每一个像素点作为卷积核的中心，卷积核范围内的像素中全部为白色像素时，将这个像素点置为白色。处理过后的蒙版与原图像相乘，得到提取出的人物图片。

替换背景时，只需将提取出的人物图片和背景图片去除蒙版的部分相加即可。

经过测试，卷积核大小设定为 `(7, 7)`，迭代次数分别为3,3时效果较好。

## 运行结果

图片1：处理过后衣服两侧的小凹陷被填补，但是衣服右侧和脖子右侧也多出了额外的背景部分。

![person1](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/person1.jpg)

![new_image1](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/new_image1.jpg)

图片2：衣服左侧的两处凹陷能够填补，但是衣服右侧的大片缺失区域难以填补。

![person2](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/person2.jpg)

![new_image2](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/new_image2.jpg)
