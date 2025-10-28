from skimage import io, color, transform
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

img = io.imread("Red_Apple.jpg")
gray = color.rgb2gray(img)

kernel = np.ones((3, 3)) / 9
blurred = convolve2d(gray, kernel, mode='same')
small = blurred[::2, ::2]

large = transform.resize(small, gray.shape, order=1)

mse = mean_squared_error(gray, large)
print(f"MSE: {mse:.6f}")

fig, ax = plt.subplots(1, 3, figsize=(12, 4))
ax[0].imshow(gray, cmap='gray')
ax[0].set_title("Original Image")
ax[1].imshow(small, cmap='gray')
ax[1].set_title("Downscaled Image")
ax[2].imshow(large, cmap='gray')
ax[2].set_title("Upscaled Image")
for a in ax:
    a.axis('off')
plt.tight_layout()
plt.show()