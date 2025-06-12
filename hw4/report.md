# 数字图像处理 第四周作业

编写 MATLAB 代码：首先载入 `./work.mat` 得到变量 `image`，其类型是 `complex double`，取幅度值得到 `spectrum`。然后进行对数变换：

```matlab
c = 1;
log_spectrum = c * log(1 + spectrum);
```

最后将处理前后的两幅图片进行对比，同时使用灰度映射和添加颜色条增强可视化效果。

源代码见 `./main.m`，运行结果图片见 `./result.jpg`。

![result](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/result.jpg)

由于对数函数始终在 $t = s$ 上方，所以低灰度值扩展，高灰度值压缩，处理后图片整体变亮，部分原本的灰度值低的区域明显变亮。
