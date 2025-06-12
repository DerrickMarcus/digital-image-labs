# 数字图像处理 第九周作业

## Task 1

该部分源代码为 `./task1.py` 。

待分割的原图像如下：

![digital_image_hw9_img1](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img1.jpg)

分别采用迭代阈值法、局部阈值法、大津算法进行图像分割。效果如下：

![digital_image_hw9_img1_result_1](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img1_result_1.jpg)

整体上局部阈值法效果略好于迭代阈值法、大津算法，文字辨识度更好、更加均匀，但是由于分块区域最终选定阈值不同，图像中出现了明显的孤立黑点，类似于椒盐噪声。而迭代阈值法、大津算法的结果中，字母有粗有细，比较不均匀。

若对风格后的图像进行闭运算 `cv2.MORPH_CLSOE` ，先腐蚀后膨胀，可以减小图像中不连续的点和突刺，但是最终效果并不理想，没有比腐蚀膨胀之前的效果更好，因为经过图像分割一些字母之后可能会被分成两个小部分，这些小部分在第一步腐蚀的时候就会被消除，导致最后的效果图中文字变瘦、部分出现残缺、像素点减少。不适合使用开运算 `cv2.MORPH_OPEN` ，因为图像中原本字体较小，一些字母比如 a,e,o 中间有小孔，先膨胀后腐蚀会填满这些小孔和缺口，让字母变成一团黑，难以辨认。

![digital_image_hw9_img1_result_2](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img1_result_2.jpg)

## Task 2

该部分源代码为 `./task2.py` 。

第一张——卫星云图：

![digital_image_hw9_img21](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img21.jpg)

第二张——焊接 X 光：

![digital_image_hw9_img22](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img22.jpg)

使用折线型的变换函数，伪彩色增强效果如下：

![digital_image_hw9_img21_line](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img21_line.jpg)

![digital_image_hw9_img22_line](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img22_line.jpg)

对于卫星云图，云部分亮度较高，映射之后红色通道最高，几乎为255，蓝色次之，绿色通道几乎为0，因此彩色图中云部分呈现红色和紫色。大陆和海洋部分亮度低，映射之后主要为绿色，因此彩色图中大陆和海洋呈现绿色，海洋亮度更低因此绿色更“纯正”。

对于焊接 X 光，裂缝部分亮度高，映射之后是明显的红色，背景部分亮度稍低，蓝色和红色合成紫色。右侧圆圈部分最暗，映射之后为青色和蓝色，说明蓝色和绿色通道像素值高，对应原图灰度级约在64以下。

使用正弦函数型的变换函数，固定周期 $T$ ，改变偏置 $\delta$ ，伪彩色增强效果如下：

![digital_image_hw9_img21_sine_1](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img21_sine_1.jpg)

![digital_image_hw9_img22_sine_1](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img22_sine_1.jpg)

对于卫星云图，第一种结果中以红绿蓝三种颜色为主，第二种结果以橙色和深蓝色为主，对比更加明显，能更清晰地看出云位于深蓝色部分，橙色是陆地和海洋。

对于焊接 X 光，右图相比于左图，中间绿色部分的蓝色分量增加，出现了一些黄色。

绘制出各个通道的变换函数如下：

![digital_image_hw9_sine_plot_1](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_sine_plot_1.png)

在一定范围内，偏置越大，各个通道变换函数达到峰值的点间距也越大，也就是峰值恰好是错开的，当其中一个通道达到峰值的时候，其他通道像素值较低，因此变换图中以红绿蓝为主。而偏置较小时，通常情况下都有两个像素值相近的通道，加和成另外一种颜色，因此变换图中出现了橙色、深蓝色等，看起来颜色更鲜艳丰富。

使用正弦函数型的变换函数，固定偏置 $\delta=T/3$ ，改变周期 $T$ ，伪彩色增强效果如下：

![digital_image_hw9_img21_sine_2](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img21_sine_2.jpg)

![digital_image_hw9_img22_sine_2](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_img22_sine_2.jpg)

对于卫星云图，从左到右随着周期减小，图像看起来更破碎，色块之间连续性减弱，也难以直观看出云层所在位置。

对于焊接 X 光，从左到右随着周期减小，同样是图像更加破碎，在上下带状区域的过渡部分，出现了红黄蓝交替的现象，这是因为周期减小后，较为微小的灰度级变化就对应一个周期，经过红黄蓝颜色峰值，因此出现类似于彩虹形状的边界。

绘制出各个通道的变换函数如下：

![digital_image_hw9_sine_plot_2](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw9_sine_plot_2.png)

周期改变时减小，变换函数振荡次数增大，也就是灰度图中不同的亮度对应到彩色图中可能是相同的颜色，对应到同一亮度的灰度级个数随着周期减小而增多，同时相邻灰度级对应的色彩差异更大，对比更明显。反映在变换效果上，直观感受就是图像更加破碎，图象被分成更多个更细小的色块，对比度更加明显。
