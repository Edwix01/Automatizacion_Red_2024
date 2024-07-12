import pandas as pd
import numpy as np
file_path = 'conteo Mariscal Sucre.xlsx'
df = pd.read_excel(file_path)
datos = df.values
def GuardarenExcel(Datos, Columnas, Archivo):
    df = pd.DataFrame(Datos, columns=Columnas)
    nombre_archivo = Archivo
    df.to_excel(nombre_archivo, index=False)

"""
A2	MSA2
A1	MSA1
A3	MSA3
"""

MS = datos[1:, 1:11]
tipo_vehiculos = np.zeros([14,3])
P_Carrosxcalle = np.zeros([14,3])
Medias = np.zeros([14,9])
N_vehiculosxhora = []
DatosMS = np.empty((P_Carrosxcalle.shape[0], P_Carrosxcalle.shape[1] + 6), dtype=P_Carrosxcalle.dtype)


for i in range(int(np.floor(len(MS[:])/4))):
    for j in range(9):
        Medias[i][j] = (float(np.sum(MS[i*4:(i+1)*4,j])))
    N_vehiculosxhora.append(float(sum(Medias[i, :])))

for i in range(int(np.floor(len(MS[:])/4))):
    for j in range(3):
        P_Carrosxcalle[i][j] = np.sum(Medias[i, j*3:(j+1)*3])/N_vehiculosxhora[i]
        tipo_vehiculos[i][j] = np.sum(Medias[i, j::3])

for i in range(P_Carrosxcalle.shape[0]):
    el1 = 1
    el2 = N_vehiculosxhora[i]
    el3 = np.round(tipo_vehiculos[i] * 0.5).astype(int)
    extra_element = [i * 3600, (i * 3600)+3600, N_vehiculosxhora[i]] + el3.tolist()
    DatosMS[i] = np.insert(P_Carrosxcalle[i], 0, extra_element)

DatosMS = np.delete(DatosMS, 4, axis=1)


columnas = ['H_inicio', 'H_fin', 'N_carros', 'Livianos', 'Camiones','P_MS2', 'P_MS1', 'P_MS3']
GuardarenExcel(DatosMS, columnas, 'DatosMS.xlsx')
