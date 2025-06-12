# 数字图像处理 第7周作业

## 任务1

原图像：

![digital_image_hw7_lena](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw7_lena.png)

首先通过 `fshift = np.fft.fftshift(np.fft.fft2(img))` 获得图像的二维频谱图。

对于理想低通滤波器，低于截止频率的点（与中心频率点距离小于 `D0` 的点）设置增益为1，其余点为0。

对于 n 阶巴特沃斯滤波器，表达式为：

$$
H(d)=\frac{1}{1+(\frac{d}{D_0})^{2n}}
$$

对于 n 阶一型切比雪夫滤波器，表达式为：

$$
H(d)=\frac{1}{\sqrt{1+\varepsilon^2T_n^2(\frac{d}{D_0})}}
$$

其中， $T_n(\Omega)$ 为 n 阶切比雪夫多项式：

$$
T_n(\Omega) =
\begin{cases}
\cos(n\arccos\Omega), & 0\le \Omega \le 1 \\
\cosh(n\operatorname{arccosh}\Omega), & \Omega >1
\end{cases}
$$

经过频域变换之后，再通过 `np.abs(np.fft.ifft2(filtered))` 变换回空域。

经过三种低通滤波器之后的图像为：

![digital_image_hw7_lowpass](./digital_image_hw7_lowpass_comparision.png)

可见，经过理想低通滤波器之后有明显的振铃效应，有较大失真，另外两种滤波器几乎感受不到振铃效应 。在截至频率相同时，理想低通滤波之后的图像在视觉上比巴特沃斯滤波器和切比雪夫滤波器更模糊，可能是由于高频率直接截断，缺少过渡频率部分，图像变化不够清晰。另外，与切比雪夫滤波器相比，巴特沃斯滤波器的亮度稍稍略高，对比度稍稍明显，可能是因为巴特沃斯滤波器通带幅度最大平坦，通过的低频分量更多。

改变巴特沃斯低通滤波器的截止频率，滤波效果如下：

![digital_image_hw7_butterworth_d0](./digital_image_hw7_butterworth_d0.png)

截止频率越高，能够通过的频率范围越大，图像越清晰；高频分量越多，细节越多。当截止频率达到70以上的时候，滤波之后的图像差别已经很小，与原图像较为接近，也说明高频分量对图像的整体影响较小。这也为图片压缩提供了思路：只保留频域低频分量，摒弃部分高频分量，也能较好的完成图像的重建。

改变巴特沃斯低通滤波器的阶数，滤波效果如下：

![digital_image_hw7_butterworth_n](./digital_image_hw7_butterworth_n.png)

巴特沃斯滤波器的阶数越高，过渡带越窄，越接近于理想低通滤波器，滤波之后的图像也越模糊。同时，当结束达到 5 或 6 时，也出现了一点振铃效应。

该部分源代码见 `./task1.py` 。

## 任务2

原图像：

![digital_image_hw7_circuit](https://cdn.jsdelivr.net/gh/DerrickMarcus/picgo_image/images/digital_image_hw7_circuit.png)

与低通滤波器类似，同样使用理想高通滤波器、巴特沃斯高通滤波器、切比雪夫高通滤波器三种滤波器进行高频增强。

巴特沃斯高通滤波器、切比雪夫高通滤波器的表达式中，只需将对应的低通滤波器中的 $\dfrac{d}{D_0}$ 改为 $\dfrac{D_0}{d}$ 即可。

经过三种高通滤波器之后的图像为：

![digital_image_hw7_highpass_comparision](./digital_imega_hw7_highpass_comparison.png)

高通滤波器将图像的纹理、边缘等具有变化信息的部分提取出来，同时减小低频分量，因此图像亮度变低，整体呈黑色。与理想低通类似，理想高通滤波之后的图像也出现了类似振铃的现象，在白色区域之间会出现额外的白色区域，而巴特沃斯滤波器和切比雪夫滤波器效果较好，能够将电路中电阻等小的元件和管脚的边缘和轮廓提取出来。

该部分源代码见 `./task2.py` 。
