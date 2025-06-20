# 数字图像处理 第13周作业

## 1. 平移变换

运行文件 `src/translate.py` ，向右平移50像素，向左平移30像素，将平移之后空出来的像素设为0（黑色），平移变换的结果为：

![202505171122810](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo-image/images/202505171122810.png)

## 2. 放缩变换

运行文件 `src/scale.py` ，宽度放大至原来的 1.4 倍，高度缩小为原来的 0.7 倍，分别进行最近邻插值和双线性插值，放缩变换的结果为：

![202505171122355](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo-image/images/202505171122355.png)

可见，最近邻插值的图像，边缘处出现阶梯形状的锯齿，毛刺明显，部分区域（如背景处）层次感明显，像素块不连续，跳跃感较强，是由于最近邻插值仅用一个最靠近的原图像素赋值，会丢弃周围像素的信息。而双线性插值边缘更加平滑，无明显的锯齿，如果是放大变换的话，仅有轻微的模糊，但整体视觉上更加符合图片直接放缩变形的结果。双线性插值通过对周围四个像素做加权平均，弱化了像素间的突变，新像素值在空间上过渡更加平滑。

## 3. 旋转变换

运行文件 `src.rotate.py` ，以中间宽度处、三分之一高度处为中心，将图片旋转逆时针旋转30度，分别进行最近邻插值和双线性插值，旋转变换的结果为：

![202505171123783](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo-image/images/202505171123783.png)

同样，最近邻插值的图像，边缘处锯齿和毛刺明显，而双线性插值边缘更加平滑。

## 4. 透视变换

运行文件 `perpective.py` ，原图像中选定4个点，指定变换后4个点的位置，然后计算透视矩阵并应用透视变换，结果为：

![202505171146656](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo-image/images/202505171146656.png)

与上面的放缩变换与旋转变换类似，最近邻插值的边缘锯齿和不连续的视觉效果更加突出，而双线性插值的图像更加平滑连续。
