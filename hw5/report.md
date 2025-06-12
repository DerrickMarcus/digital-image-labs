# 数字图像处理 第5周作业

## 1. 均衡化

处理思路：

1. 读取灰度图片 `image` 之后，首先遍历每一个像素，统计每个灰度值出现的次数，得到原图像的统计直方图 `hist`。
2. 统计直方图归一化，除以总像素个数，得到像素值的概率密度函数 `pdf`。
3. 将概率密度函数累加得到累积分布函数 `cdf`，乘以最大灰度级 255，得到原灰度值映射到的新灰度值关系 `pixel_new`。
4. 根据 `pixel_new` 生成均衡化后的图像 `image_equalized`，并遍历像素得到统计直方图。

源代码文件见 `./task1/main.py`，运行结果如下：

![img1_compare](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/img1_compare.png)

![img2_compare](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/img2_compare.png)

可见，处理过后图片的对比度明显增强，像素的灰度值动态范围扩大至几乎占满 $[0,255]$ 区间。图片1中人物裤子亮度明显增加，这周更加明显。图片2中两侧面包板变暗，与手指的对比更加明显。

## 2. 规定化

处理思路：由于输入为彩色图片，需要对 RGB 三个通道分别进行规定化，共用一个函数 `channel_specification()`。

在 `channel_specification()` 函数中，首先调用 `compute_cdf()` 函数，其中计算 cdf 的方法与 task1 均衡化相同。得到原图像和模板图像的直方图累积分布函数，然后建立两个累积分布函数的映射关系 `mappping`：对于原图像 cdf 中的每一个值，找到在模板图像 cdf 中与它最接近的值，其对应的灰度级就是规定化之后的灰度级，再根据 `mapping` 逐像素构建规定化之后的图像。

在 `histogram_specification` 中，将原图像和模板图像拆分为 R,G,B 三个通道，对每个通道进行规定化处理，再拼接起来得到规定化之后的图像。

源代码文件见 `./task2/main.py`，运行结果如下：

![img1_compare](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/img1_compare.jpg)

![img2_compare](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/img2_compare.jpg)

对于图片1，处理过后图片整体变得更加暗淡，不如原图像那么明亮鲜艳，主要原因是绿色通道像素值原本集中在高值部分，显得整体明亮，经过规定化之后分布更加均匀，低值部分像素数目增多，高值部分像素减少。蓝色通道像素值更加集中在低值部分，因为作为模板的图片2蓝色通道像素值也集中在低值部分。

对于图片2，处理过后，草原的对比度明显增加，部分绿色区域经过处理之后变得更偏近黄色，可能是因为虽然蓝色通道整体强度略有提升，但是作为模板的图片1中红色和绿色通道的像素值更集中在高值部分，规定化之后的图片2红色和绿色通道强度提升更多，因此从视觉上黄色区域增多。
