# 数字图像处理 第6周作业

首先对图像添加高斯噪声和椒盐噪声，分别封装为函数 `add_gaussian_noise()` 和 `add_salt_pepper_noise()` 。添加高斯噪声时，原图像加上噪声后的结果应该做 0~255 区间截断处理，防止溢出。添加椒盐噪声时，设定出现胡椒噪声（黑点）和盐噪声（百点）的概率相同，简化分析。

添加噪声后的图像与原图像的对比图为 `img_noise.jpg` 。

![img_noise](./img_noise.jpg)

添加了高斯噪声的直观感觉是图像变得更加模糊，在一小片区域中黑白变化更明显，因为高斯噪声是在正负值范围内分布，可能增大或减小相邻像素之间灰度值差。添加了椒盐噪声之后，就好像在图片中均匀撒了椒盐，出现明显的小白点和小黑点。

然后使用两种滤波方法：中值滤波和高斯滤波。

对于添加高斯噪声的图像，滤波前后效果对比图为：

![img_gaussian_filtered](./img_gaussian_filtered.jpg)

中值滤波和高斯滤波的峰值信噪比 PSNR 分别为：

```text
Image with gaussian noise, median filtered, PSNR: 78.60 dB
Image with gaussian noise, gaussian filtered, PSNR: 78.08 dB
```

添加高斯噪声的图像，经过中值滤波和高斯滤波之后，都有一定程度的模糊，小片区域内像素灰度值对比差异减小，左侧黑色圆孔也更加圆润，但差异并不明显，PSNR 也很接近。

对于添加椒盐噪声的图像，滤波前后效果对比图为：

![img_salt_filtered](./img_salt_filtered.jpg)

中值滤波和高斯滤波的峰值信噪比 PSNR 分别为：

```text
Image with salt&pepper noise, median filtered, PSNR: 87.97 dB
Image with salt&pepper noise, gaussian filtered, PSNR: 80.61 dB
```

添加椒盐噪声的图像，经过中值滤波之后噪声明显减小，效果比高斯滤波更好。因为中值滤波选取的卷积核较小 $3\times3$ ，而椒盐噪声分布较为稀疏（设定的概率值只有0.05），因此在一个卷积核覆盖范围内椒盐噪声数量较少，其极端灰度值0或255不会影响中间值，因此中值滤波对于椒盐噪声非常有效。而经过高斯滤波之后，图像更加模糊，而且椒盐噪声也没有很好的去除。

下面使用了两种高频提升方法：拉普拉斯算子、Sobel 算子、高斯-拉普拉斯算子。处理过后的图像为：

![img_sharpened](./img_sharpened.jpg)

经过拉普拉斯算子锐化之后，图像中边缘更加明显，尤其是左上角的几个同心圆线条更加黑，与桌子对比更加明显。Sobel 算子和高斯-拉普拉斯算子能够提取出图形中的边缘，但后者亮度更高、边缘更清晰，效果更好。

完整源代码见 `./main.py` 。
