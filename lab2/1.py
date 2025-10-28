import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve
from sklearn.metrics import mean_squared_error

def f1(x): return np.sin(x)
def f2(x): return np.sin(x - 1)
def f3(x): return np.sign(np.sin(8*x))

def h1(t): return np.where((t >= 0) & (t < 1), 1, 0)
def h2(t): return np.where((t >= -0.5) & (t < 0.5), 1, 0)
def h3(t): return np.where(np.abs(t) <= 1, 1 - np.abs(t), 0)
def h4(t): return np.sinc(t / np.pi)

def interpolate_function(f, kernel, upsample_factor=2, name="f"):
    x = np.linspace(-np.pi, np.pi, 100)
    y = f(x)
    upsampled = np.zeros(len(y) * upsample_factor)
    upsampled[::upsample_factor] = y
    t = np.linspace(-5, 5, 100)
    h = kernel(t)
    y_interp = convolve(upsampled, h, mode='same') / np.sum(h)
    x_new = np.linspace(-np.pi, np.pi, len(y_interp))
    mse = mean_squared_error(f(x_new), y_interp)
    plt.figure(figsize=(7,4))
    plt.plot(x, y, 'o-')
    plt.plot(x_new, y_interp, '-')
    plt.title(f'{name}, kernel={kernel.__name__}, MSE={mse:.5f}')
    plt.grid(True)
    plt.show()
    return mse

for func, name in zip([f1, f2, f3], ['f1(x)=sin(x)', 'f2(x)=sin(x-1)', 'f3(x)=sign(sin(8x))']):
    for kernel in [h1, h3, h4]:
        interpolate_function(func, kernel, upsample_factor=4, name=name)