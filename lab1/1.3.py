from skimage import io
import matplotlib.pyplot as plt

# Ścieżka do zdjęcia
image_path = "moje_zdjecie.jpg"  # <- wstaw tu nazwę swojego pliku

# Wczytanie zdjęcia
image = io.imread(image_path)

# Wyświetlenie zdjęcia
plt.imshow(image)
plt.axis('off')  # wyłączenie osi
plt.title("Moje kolorowe zdjęcie")
plt.show()