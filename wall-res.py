#! /bin/env python

import os
import re
from PIL import Image

# Definir los tipos de resolución basados en la Wikipedia
resolutions = {
    (720, 480): "SD",
    (1280, 720): "HD",
    (1920, 1080): "Full_HD",
    (2560, 1440): "Quad_HD",
    (3840, 2160): "4K",
    (5120, 2880): "5K",
    (6016, 3384): "6K",
    (7680, 4320): "8K",
    (2560, 1080): "UltraWide_Full_HD",
    (3440, 1440): "UltraWide_Quad_HD",
    (5120, 2160): "UltraWide_5K",
    (3840, 1600): "UltraWide_Quad_HD+",
}

# Expresión regular para detectar si el archivo ya está en el formato deseado
pattern = re.compile(r'^\d+-\d+x\d+-.+$')

def get_resolution_type(width, height):
    return resolutions.get((width, height), "Custom")

def main(directory):
    files = os.listdir(directory)
    id_counter = 1

    for file in files:
        # Ignorar los archivos que ya tienen el formato deseado
        if pattern.match(file):
            continue

        filepath = os.path.join(directory, file)

        try:
            with Image.open(filepath) as img:
                width, height = img.size
        except Exception as e:
            print(f"Error al abrir el archivo {file}: {e}")
            continue

        resolution_type = get_resolution_type(width, height)
        new_filename = f"{id_counter}-{width}x{height}-{resolution_type}{os.path.splitext(file)[1]}"
        new_filepath = os.path.join(directory, new_filename)

        os.rename(filepath, new_filepath)
        print(f"Renamed: {file} -> {new_filename}")
        id_counter += 1

if __name__ == "__main__":
    directory = "./wallpapers"  # Cambia esto al directorio deseado
    main(directory)

