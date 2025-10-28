import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # для 3D графіка

# -----------------------------
# 1. Definicja zakresu x i y
# -----------------------------
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)  # створюємо сітку координат
Z = np.sin(2*X**2 + Y**2) # обчислюємо значення функції

# -----------------------------
# 2. Surface plot (wykres powierzchniowy)
# -----------------------------
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title("Surface plot f(x,y) = sin(2x^2 + y^2)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("f(x,y)")
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10)

# -----------------------------
# 3. Contour plot (wykres konturowy)
# -----------------------------
ax2 = fig.add_subplot(1, 2, 2)
cont = ax2.contourf(X, Y, Z, levels=50, cmap='viridis')
ax2.set_title("Contour plot f(x,y) = sin(2x^2 + y^2)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
fig.colorbar(cont, ax=ax2)

plt.tight_layout()
plt.show()