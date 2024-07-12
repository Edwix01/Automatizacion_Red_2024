import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dfRA = pd.read_excel('DatosRA.xlsx')
datosRA = dfRA.values
vehiculosRA = datosRA[:,2]
horas = datosRA[:,0:2]
archivos_csv = ['RA1.csv', 'RA2.csv', 'RA3.csv']
vehiculos_por_archivo = {}
for archivo in archivos_csv:
    df = pd.read_csv(archivo, delimiter=';')
    matriz_datos = df.values
    vehiculos = matriz_datos[:, 15]
    vehiculos_por_archivo[archivo] = vehiculos
Suma = np.zeros([int(np.floor(len(vehiculos_por_archivo[archivos_csv[0]][:])/12)),3])
for hora in range(int(np.floor(len(vehiculos_por_archivo[archivos_csv[0]][:])/12))):
    for i, (archivo, vehiculos) in enumerate(vehiculos_por_archivo.items()):
        Suma[hora][i] = (float(np.sum(vehiculos[hora*12:(hora+1)*12])))
vector = np.sum(Suma, axis=1)
print(datosRA[:,2])
print(vector)

"""correlation = np.corrcoef(vehiculosRA, vector)[0, 1]
plt.figure(figsize=(8, 6))
plt.scatter(vehiculosRA, vector, color='blue', label='Datos')
plt.plot(np.unique(vehiculosRA), np.poly1d(np.polyfit(vehiculosRA, vector, 1))(np.unique(vehiculosRA)), color='red', label=f'Correlación = {correlation:.3f}')
plt.xlabel('Datos reales')
plt.ylabel('Datos simulados')
plt.legend()
plt.title(f'Correlación entre datos reales y simulados')
plt.grid(True)
plt.show()
"""

x_labels = ["6-7 AM", "7-8 AM", "8-9 AM", "9-10 AM", "10-11 AM", "11-12 AM",
            "12 AM-1 PM", "1-2 PM", "2-3 PM", "3-4 PM", "4-5 PM", "5-6 PM",
            "6-7 PM", "7-8 PM"]
bar_width = 0.35
indices = np.arange(len(x_labels))


plt.bar(indices - bar_width / 2, vehiculosRA[:len(vector)], bar_width, label='Vehiculos contados')
plt.bar(indices + bar_width / 2, vector, bar_width, label='Vehiculos simulados')

# Configuración del gráfico
plt.xlabel('Horas')
plt.ylabel('Cantidad de Vehículos')
plt.title('Comparación de vehículos reales y simulados')
plt.xticks(indices, x_labels, rotation=45)
plt.legend()
plt.tight_layout()

# Mostrar gráfico
plt.show()