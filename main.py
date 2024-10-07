import cv2
import os
import shutil
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Función para solicitar al usuario seleccionar una carpeta
def select_folder():
    Tk().withdraw()  # Oculta la ventana principal de Tkinter
    folder_path = askdirectory(title="Selecciona la carpeta a analizar")
    return folder_path

# Solicitar la carpeta del usuario
source_folder = select_folder()
if not source_folder:
    print("No se seleccionó ninguna carpeta. Saliendo del programa.")
    exit()

# Crear la carpeta de "imagenes_para_eliminar" dentro de la carpeta seleccionada
destination_folder = os.path.join(source_folder, 'imagenes_para_eliminar')
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Función para detectar imágenes borrosas usando la laplaciana
def is_blurry(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    return variance < 100  # Umbral ajustable

# Función para detectar imágenes con mal nivel de iluminación
def has_bad_lighting(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Evaluamos el contraste y exposición usando histograma
    hist, _ = np.histogram(gray.ravel(), bins=256, range=(0, 256))
    low_light_threshold = 50
    over_exposed_threshold = 200

    if hist[:low_light_threshold].sum() > 0.6 * hist.sum() or hist[over_exposed_threshold:].sum() > 0.6 * hist.sum():
        return True
    return False

# Recorrer todos los archivos de la carpeta
for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        image_path = os.path.join(source_folder, filename)
        image = cv2.imread(image_path)

        if image is None:
            continue  # Ignorar archivos no válidos

        # Detectar si la imagen está borrosa o tiene mal nivel de iluminación
        if is_blurry(image) or has_bad_lighting(image):
            # Mover imagen a la carpeta de eliminación
            print(f'Moviendo {filename} a {destination_folder}')
            shutil.move(image_path, os.path.join(destination_folder, filename))

print("Análisis completado.")
