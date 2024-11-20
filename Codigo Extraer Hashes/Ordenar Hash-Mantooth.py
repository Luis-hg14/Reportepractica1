import re
import pandas as pd

# Archivo de entrada y salida
input_file = "Archivo.txt"  # Reemplaza con el nombre de tu archivo
output_file = "archivos_separados.csv"  # Usar .csv

# Leer el archivo de texto
with open(input_file, "r") as file:
    lines = file.read().split("\n\n")  # Separar por bloques de archivos

# Expresión regular para extraer datos
pattern = re.compile(
    r"^(.*) - (\d+ bytes)\nMD5: (.*)\nSHA1: (.*)\nSHA256: (.*)\nSHA512: (.*)$"
)

# Procesar datos
data = []
for block in lines:
    match = pattern.match(block.strip())
    if match:
        data.append(match.groups())

# Crear un DataFrame y guardar en CSV
columns = ["Nombre del archivo", "Tamaño", "MD5", "SHA1", "SHA256", "SHA512"]
df = pd.DataFrame(data, columns=columns)
df.to_csv(output_file, index=False)  # Guardar en formato CSV

print(f"Datos guardados en {output_file}")
