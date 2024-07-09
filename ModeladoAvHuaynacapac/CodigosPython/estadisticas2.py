import pandas as pd
import matplotlib.pyplot as plt
import os


#Columnas de interes
#Párametros
#Se gráfica el promedio en un intervalo de tiempo
#Tiempo en segundos

"""
tripinfo_depart: Tiempo de salida 
tripinfo_arrival: Tiempo de llegada
tiempos de viaje : tripinfo_duration
distancias de rutas, 
tiempos de espera en semáforos, 
conteo de vehículos.
"""

# Función para leer el archivo CSV y graficar columnas específicas en subplots
def obt_metricas_tiempo(archivo_csv, nombres_columnas,tiempo):
    # Leer el archivo CSV
    df = pd.read_csv(archivo_csv)
    df = df.sort_values(by='tripinfo_depart', ascending=False)
    print(df["tripinfo_depart"])
    promedio_por_intervalo = df.groupby(df['tripinfo_depart'] // tiempo * tiempo)['tripinfo_duration'].mean().reset_index()
    print(promedio_por_intervalo)


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