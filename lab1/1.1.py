import numpy as np
import matplotlib.pyplot as plt

# Definiujemy zakres x
x = np.linspace(0, 5, 500)  # dopasuj zakres do potrzeb

# Definicje funkcji
f1 = -x * np.exp(-x / 2)
f2 = np.sin(np.pi*x) + 2*np.cos(2*np.pi*x) + 3*np.sin(2*np.pi*x) * np.exp(-x/2)
# f3 tylko gdy x > 2, w pozostałych miejscach 0
f3 = np.where(x > 2, 2*x*np.exp(-x), 0)

# ----------------------
# Wykres na jednym wykresie
# ----------------------
plt.figure(figsize=(8,5))
plt.plot(x, f1, label='f1(x) = -x * e^(-x/2)')
plt.plot(x, f2, label='f2(x) = sin(πx) + 2cos(2πx) + 3sin(2πx)e^(-x/2)')
plt.plot(x, f3, label='f3(x) = 2x*e^(-x) gdy x>2')
plt.title('Wszystkie funkcje na jednym wykresie')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# ----------------------
# Wykresy na 3 subplotach
# ----------------------
fig, axs = plt.subplots(3, 1, figsize=(8,10), sharex=True)

axs[0].plot(x, f1, color='blue')
axs[0].set_title('f1(x) = -x * e^(-x/2)')
axs[0].grid(True)

axs[1].plot(x, f2, color='green')
axs[1].set_title('f2(x) = sin(πx) + 2cos(2πx) + 3sin(2πx)e^(-x/2)')
axs[1].grid(True)

axs[2].plot(x, f3, color='red')
axs[2].set_title('f3(x) = 2x*e^(-x) gdy x>2')
axs[2].set_xlabel('x')
axs[2].grid(True)

plt.tight_layout()
plt.show()