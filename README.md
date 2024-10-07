# Análisis de imágenes borrosas y con mal nivel de iluminación

Este script utiliza la biblioteca `cv2` de OpenCV para detectar imágenes borrosas y con mal nivel de iluminación dentro de una carpeta especificada por el usuario. Las imágenes que cumplan con cualquiera de estas condiciones serán movidas a una carpeta llamada "imagenes_para_eliminar" dentro de la carpeta seleccionada.

## Requisitos

- Python 3.x
- OpenCV (cv2)
- Tkinter

## Instalación de dependencias

Para instalar las dependencias necesarias, ejecuta el siguiente comando en tu terminal:

```
pip install opencv-python tkinter
```

## Uso

1. Ejecuta el script Python.
2. Se abrirá una ventana de selección de carpeta donde debes seleccionar la carpeta que contiene las imágenes que deseas analizar.
3. El script recorrerá todos los archivos de la carpeta seleccionada y las imágenes que cumplan con cualquiera de las condiciones de borrosidad o mal nivel de iluminación serán movidas a la carpeta "imagenes_para_eliminar".
4. Una vez completado el análisis, se mostrará el mensaje "Análisis completado".

## Detección de imágenes borrosas

La función `is_blurry` utiliza la transformada de Laplaciano para evaluar la varianza de la imagen en escala de grises. Si la varianza es menor a 100, se considera que la imagen es borrosa.

## Detección de imágenes con mal nivel de iluminación

La función `has_bad_lighting` evalúa el contraste y exposición de la imagen en escala de grises utilizando un histograma. Si el histograma de la imagen tiene un porcentaje significativo de píxeles con un nivel de brillo bajo o alto, se considera que la imagen tiene mal nivel de iluminación.

## Consideraciones adicionales

- El script solo considera archivos con extensiones `.png`, `.jpg`, `.jpeg`, `.bmp` y `.tiff`.
- Si no se selecciona ninguna carpeta, el script mostrará un mensaje y se cerrará.
- Si hay errores al leer las imágenes, se ignorarán y el script continuará con el siguiente archivo.
- El umbral de borrosidad y el umbral de nivel de iluminación pueden ajustarse en las funciones `is_blurry` y `has_bad_lighting`.

## Créditos

Este script fue creado por Beri (https://github.com/iberi22) con ayuda de llms.

