import pandas as pd
import requests
import time

# Clave API gratuita de VirusTotal
API_KEY = "0e8e59b9d5ad0d0e567f8958c31aab97747894b2c609047ee20fb262ae28a375"

# Función para consultar VirusTotal
def check_hash_virustotal(hash_value):
    url = f"https://www.virustotal.com/api/v3/files/{hash_value}"
    headers = {
        "x-apikey": API_KEY
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            malicious_count = data['data']['attributes']['last_analysis_stats']['malicious']
            return malicious_count
        elif response.status_code == 404:
            return "Hash no encontrado"
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Cargar los datos desde un archivo CSV
file_path ="/home/kali/Desktop/maestria/excel1.csv"  # Cambia esto por tu archivo CSV
df = pd.read_csv(file_path)

# Crear una nueva columna para almacenar los resultados
results = []
for index, row in df.iterrows():
    hash_value = row['hash']
    result = check_hash_virustotal(hash_value)
    results.append(result)
    time.sleep(15)  # Pausa para cumplir con el límite de 4 consultas por minuto

df['malicious_count'] = results

# Guardar los resultados en un nuevo archivo CSV
output_file = "resultado_analisis_hashes.csv"
df.to_csv(output_file, index=False)

print(f"Análisis completado. Resultados guardados en {output_file}.")
