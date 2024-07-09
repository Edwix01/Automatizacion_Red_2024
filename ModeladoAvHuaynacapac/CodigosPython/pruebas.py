import pandas as pd
import matplotlib.pyplot as plt
import os

# Función para leer el archivo CSV y graficar columnas específicas en subplots
def obt_metricas_tiempo(archivo_csv, nombres_columnas,tiempo):
    # Leer el archivo CSV
    df = pd.read_csv(archivo_csv)
    # Supongamos que df es tu DataFrame y columna_a_contar es la columna de interés
    num_elementos_unicos = df['tripinfo_id'].nunique()

    print(f"Número de elementos únicos en la columna: {num_elementos_unicos}")



# Ruta del archivo
ruta_actual = os.path.abspath(__file__)
directorio_anterior = os.path.dirname(ruta_actual)
ruta_final = os.path.dirname(directorio_anterior)
archivo_csv = os.path.join(ruta_final, "tripinfo.csv")

# Lista de nombres de columnas a graficar
#nombres_columnas = ['tripinfo_waitingTime', 'tripinfo_duration', 'tripinfo_routeLength']
metrica = "tripinfo_routeLength"
intervalo = 120
# Llamar a la función para graficar las columnas en subplots
obt_metricas_tiempo(archivo_csv, metrica,intervalo)