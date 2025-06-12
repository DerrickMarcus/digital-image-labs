import matplotlib.pyplot as plt
import numpy as np

p = np.linspace(0, 255, 256)

T = 255
delta = 255 / 3

I_r = (1 + np.sin(2 * np.pi / T * p)) * 255 / 2
I_g = (1 + np.sin(2 * np.pi / T * (p - delta))) * 255 / 2
I_b = (1 + np.sin(2 * np.pi / T * (p - 2 * delta))) * 255 / 2

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(p, I_r, "r")
plt.plot(p, I_g, "g")
plt.plot(p, I_b, "b")
plt.xlim(0, 255)
plt.ylim(0, 255)
plt.title("Pseudo color transformation\nT=255, delta=255/3")
plt.xlabel("Gray level")
plt.ylabel("Intensity")
plt.grid(True)

T = 255
delta = 255 / 6

I_r = (1 + np.sin(2 * np.pi / T * p)) * 255 / 2
I_g = (1 + np.sin(2 * np.pi / T * (p - delta))) * 255 / 2
I_b = (1 + np.sin(2 * np.pi / T * (p - 2 * delta))) * 255 / 2

plt.subplot(1, 2, 2)
plt.plot(p, I_r, "r")
plt.plot(p, I_g, "g")
plt.plot(p, I_b, "b")
plt.xlim(0, 255)
plt.ylim(0, 255)
plt.title("Pseudo color transformation\nT=255, delta=255/6")
plt.xlabel("Gray level")
plt.ylabel("Intensity")
plt.grid(True)

plt.tight_layout()
plt.savefig("./digital_image_hw9_sine_plot_1.png")
plt.show()

# -----------------------------------------------------------------

T = 255
delta = T / 3

I_r = (1 + np.sin(2 * np.pi / T * p)) * 255 / 2
I_g = (1 + np.sin(2 * np.pi / T * (p - delta))) * 255 / 2
I_b = (1 + np.sin(2 * np.pi / T * (p - 2 * delta))) * 255 / 2

plt.figure(figsize=(15, 6))

plt.subplot(1, 3, 1)
plt.plot(p, I_r, "r")
plt.plot(p, I_g, "g")
plt.plot(p, I_b, "b")
plt.xlim(0, 255)
plt.ylim(0, 255)
plt.title("Pseudo color transformation\nT=255, delta=T/3")
plt.xlabel("Gray level")
plt.ylabel("Intensity")
plt.grid(True)

T = 255 / 2
delta = T / 3

I_r = (1 + np.sin(2 * np.pi / T * p)) * 255 / 2
I_g = (1 + np.sin(2 * np.pi / T * (p - delta))) * 255 / 2
I_b = (1 + np.sin(2 * np.pi / T * (p - 2 * delta))) * 255 / 2


plt.subplot(1, 3, 2)
plt.plot(p, I_r, "r")
plt.plot(p, I_g, "g")
plt.plot(p, I_b, "b")
plt.xlim(0, 255)
plt.ylim(0, 255)
plt.title("Pseudo color transformation\nT=255/2, delta=T/3")
plt.xlabel("Gray level")
plt.ylabel("Intensity")
plt.grid(True)

T = 255 / 4
delta = T / 3

I_r = (1 + np.sin(2 * np.pi / T * p)) * 255 / 2
I_g = (1 + np.sin(2 * np.pi / T * (p - delta))) * 255 / 2
I_b = (1 + np.sin(2 * np.pi / T * (p - 2 * delta))) * 255 / 2

plt.subplot(1, 3, 3)
plt.plot(p, I_r, "r")
plt.plot(p, I_g, "g")
plt.plot(p, I_b, "b")
plt.xlim(0, 255)
plt.ylim(0, 255)
plt.title("Pseudo color transformation\nT=255/4, delta=T/3")
plt.xlabel("Gray level")
plt.ylabel("Intensity")
plt.grid(True)

plt.tight_layout()
plt.savefig("./digital_image_hw9_sine_plot_2.png")
plt.show()
