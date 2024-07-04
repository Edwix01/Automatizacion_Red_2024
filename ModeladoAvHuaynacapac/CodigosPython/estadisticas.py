import pandas as pd
import matplotlib.pyplot as plt
import os

# Función para leer el archivo CSV y graficar columnas específicas en subplots
def graficar_columnas_subplots(archivo_csv, nombres_columnas):
    # Leer el archivo CSV
    df = pd.read_csv(archivo_csv)

    # Verificar si las columnas existen en el DataFrame
    for nombre_columna in nombres_columnas:
        if nombre_columna not in df.columns:
            print(f"La columna '{nombre_columna}' no existe en el archivo CSV.")
            return

    # Graficar las columnas especificadas en subplots
    num_columnas = len(nombres_columnas)
    fig, axes = plt.subplots(num_columnas, 1, figsize=(10, 6 * num_columnas), sharex=True)

    if num_columnas == 1:
        axes = [axes]  # Asegurarse de que 'axes' sea iterable si hay solo un subplot

    for ax, nombre_columna in zip(axes, nombres_columnas):
        ax.plot(df[nombre_columna], marker='o', linestyle='-', label=nombre_columna)
        ax.set_title(f'Gráfica de la columna: {nombre_columna}')
        ax.set_xlabel('Índice')
        ax.set_ylabel(nombre_columna)
        ax.grid(True)
        ax.legend()

    plt.tight_layout()
    plt.show()

# Ruta del archivo
ruta_actual = os.path.abspath(__file__)
directorio_anterior = os.path.dirname(ruta_actual)
ruta_final = os.path.dirname(directorio_anterior)
archivo_csv = os.path.join(ruta_final, "tripinfo.csv")

# Lista de nombres de columnas a graficar
nombres_columnas = ['tripinfo_waitingTime', 'tripinfo_duration', 'tripinfo_routeLength']

# Llamar a la función para graficar las columnas en subplots
graficar_columnas_subplots(archivo_csv, nombres_columnas)
