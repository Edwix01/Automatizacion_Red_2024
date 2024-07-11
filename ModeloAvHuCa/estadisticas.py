import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'STIXGeneral'  # STIX general es similar a la fuente de LaTeX
def graficar_m(datos,labelmetrica,labeltiempo):
        # Crear la gráfica
    plt.figure(figsize=(10, 6))
    x = datos[labeltiempo]
    y = datos[labelmetrica]
    plt.plot(x,y, 'o',label=labelmetrica, color='b')
    plt.vlines(x, ymin=0, ymax=y, color='blue', linestyle='dashed')
    # Añadir título y etiquetas a los ejes
    plt.title('Gráfica de la función de la métrica '+labelmetrica)
    plt.xlabel('Tiempo[Horas]')
    plt.ylabel('Métrica')
    # Añadir una leyenda
    plt.legend()
    # Mostrar la gráfica
    plt.grid(True)
    plt.show()

def graficar_v(datos):
        # Crear la gráfica
    plt.figure(figsize=(10, 6))
    y = datos['vehicle_id']
    x = datos['timestep_time']
    plt.plot(x,y, 'o', label="# de Vehiculos", color='b')
    # Añadir líneas verticales desde el eje x hasta cada punto
    plt.vlines(x, ymin=0, ymax=y, color='blue', linestyle='dashed')

    # Añadir título y etiquetas a los ejes
    plt.title('Gráfica del número de vehiculos generados')
    plt.xlabel('Tiempo[Horas]')
    plt.ylabel('# de Vehiculos')
    # Añadir una leyenda
    plt.legend()
    # Mostrar la gráfica
    plt.grid(True)
    plt.show()

# Función para leer el archivo CSV y graficar columnas específicas en subplots
def obt_metricas_tiempo(metrica_csv,vehiculos_csv,lblmetrica,tiempo):
    # Leer el archivo CSV
    dnv = pd.read_csv(vehiculos_csv)
    dfm = pd.read_csv(metrica_csv)
    dfm = dfm.sort_values(by='tripinfo_depart', ascending=False)
    metrica = dfm.groupby(dfm['tripinfo_depart'] // tiempo * tiempo)[lblmetrica].mean().reset_index()
    dfnv = dnv.sort_values(by='timestep_time', ascending=False)
    n_vehiculos = dfnv.groupby(dfnv['timestep_time'] // tiempo * tiempo)['vehicle_id'].nunique().reset_index()
    graficar_m(metrica,lblmetrica,'tripinfo_depart')
    graficar_v(n_vehiculos)

# Ruta del los archivos de salida de SUMO - No cambiar
ruta_actual = os.path.abspath(__file__)
ruta_final = os.path.dirname(ruta_actual)
metrica_csv = os.path.join(ruta_final, "tripinfo.csv")
vehiculo_csv = os.path.join(ruta_final, "fcd.csv")

#Ejecución del Código

#Métricas que se pueden visualizar
"""
tiempos de viaje:          tripinfo_duration
distancias de rutas:       tripinfo_routeLength
t. espera en semáforos:    tripinfo_waitingTime
conteo de vehículos
"""

#Parámetros para graficar
met = "tripinfo_duration"    #Métrica que se desea visualizar
intervalo = 3600              #Intervalo de tiempo de análisis
# Llamar a la función para graficar las columnas en subplots
obt_metricas_tiempo(metrica_csv, vehiculo_csv, met,intervalo)