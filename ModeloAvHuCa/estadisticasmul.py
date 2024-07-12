import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'STIXGeneral'  # STIX general es similar a la fuente de LaTeX

# Función para leer un archivo CSV y retornar la columna de la métrica específica
def load_metric_from_csv(file_path, metric_column, tiempo):
    dn = pd.read_csv(file_path)
    if metric_column == 'vehicle_id':
        dn = dn.sort_values(by='timestep_time', ascending=False)
        dn = dn.groupby(dn['timestep_time'] // tiempo * tiempo)['vehicle_id'].nunique().reset_index()
    else:
        dn = dn.sort_values(by='tripinfo_depart', ascending=False)
        dn = dn.groupby(dn['tripinfo_depart'] // tiempo * tiempo)[metric_column].mean().reset_index()
    return dn[metric_column]

# Leer las métricas de los tres archivos
"""
tiempos de viaje:          tripinfo_duration
distancias de rutas:       tripinfo_routeLength
t. espera en semáforos:    tripinfo_waitingTime
conteo de vehículos:       vehicle_id
""" 

dato = "vehicle_id"
tiempo = 3600 

metric1 = load_metric_from_csv('fcd.csv', dato, tiempo)
metric2 = load_metric_from_csv('fcd1.csv', dato, tiempo)
metric3 = load_metric_from_csv('fcd2.csv', dato, tiempo)
metric4 = load_metric_from_csv('fcd3.csv', dato, tiempo)

# Crear una figura y un eje
fig, ax = plt.subplots(figsize=(12, 7))

# Generar números del 1 al x
horas = 14
x = np.arange(1, horas + 1) + 5
bar_width = 0.2  # Ancho de las barras

# Crear gráficos de barras
ax.bar(x - 1.5 * bar_width, metric1[0:horas], width=bar_width, label='Escenario buses')
ax.bar(x - 0.5 * bar_width, metric2[0:horas], width=bar_width, label='Escenario tranvía')
ax.bar(x + 0.5 * bar_width, metric3[0:horas], width=bar_width, label='Aumento del tráfico normal')
ax.bar(x + 1.5 * bar_width, metric4[0:horas], width=bar_width, label='Modelo realista')

# Añadir títulos y etiquetas
ax.set_title('Comparación de Métrica ' + dato + ' entre escenarios')
ax.set_xlabel('Horas [h]')
ax.set_ylabel('Valor de Métrica')
ax.legend()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
