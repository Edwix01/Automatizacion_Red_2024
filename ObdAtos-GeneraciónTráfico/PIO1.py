import pandas as pd
import numpy as np
file_path = 'conteo Pio1.xlsx'
df = pd.read_excel(file_path)
datosPio1 = df.values


def GuardarenExcel(Datos, Columnas, Archivo):
    df = pd.DataFrame(Datos, columns=Columnas)
    nombre_archivo = Archivo
    df.to_excel(nombre_archivo, index=False)


Pio1 = datosPio1[1:, 1:4]
tipo_vehiculos = np.zeros([14,3])
P_Carrosxcalle = np.zeros(14)
Medias = np.zeros([14,3])
N_vehiculosxhora = []
DatosPio1 = np.empty((P_Carrosxcalle.shape[0], 7), dtype=P_Carrosxcalle.dtype)

for i in range(int(np.floor(len(Pio1[:]) / 4))):
    for j in range(3):
        Medias[i][j]=(float(np.sum(Pio1[i * 4:(i + 1) * 4, j])))
    N_vehiculosxhora.append(float(sum(Medias[i, :])))

for i in range(int(np.floor(len(Pio1[:]) / 4))):
    P_Carrosxcalle[i] = np.sum(Medias[i, 0:3]) / N_vehiculosxhora[i]
    for j in range(3):
        tipo_vehiculos[i][j] = np.sum(Medias[i, j::3])


for i in range(P_Carrosxcalle.shape[0]):
    el1 = 1
    el2 = N_vehiculosxhora[i]
    el3 = tipo_vehiculos[i]
    extra_element = [i * 3600, (i * 3600)+3600, N_vehiculosxhora[i]] + tipo_vehiculos[i].tolist()
    DatosPio1[i] = np.insert(P_Carrosxcalle[i], 0, extra_element)


DatosCL = np.delete(DatosPio1, 4, axis=1)

columnas = ['H_inicio', 'H_fin', 'N_carros', 'Livianos', 'Camiones','P_PIOA3']
GuardarenExcel(DatosCL, columnas, 'DatosPio1.xlsx')




