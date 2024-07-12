import pandas as pd
import numpy as np
file_path = 'conteo vehicular huaynacapac y bolivar.xlsx'
df = pd.read_excel(file_path)
datos = df.values
RA = datos[1:, 19:28]
def GuardarenExcel(Datos, Columnas, Archivo):
    df = pd.DataFrame(Datos, columns=Columnas)
    nombre_archivo = Archivo
    df.to_excel(nombre_archivo, index=False)

tipo_vehiculos = np.zeros([14,3])
P_Carrosxcalle = np.zeros([14,3])
Medias = np.zeros([14,9])
N_vehiculosxhora = []
DatosRA = np.empty((P_Carrosxcalle.shape[0], P_Carrosxcalle.shape[1] + 6), dtype=P_Carrosxcalle.dtype)

for i in range(int(np.floor(len(RA[:])/4))):
    for j in range(9):
        Medias[i][j]=(float(np.sum(RA[i*4:(i+1)*4,j])))
    N_vehiculosxhora.append(float(sum(Medias[i, :])))

for i in range(int(np.floor(len(RA[:])/4))):
    for j in range(3):
        P_Carrosxcalle[i][j] = np.sum(Medias[i, j*3:(j+1)*3])/N_vehiculosxhora[i]
        tipo_vehiculos[i][j] = np.sum(Medias[i, j::3])

for i in range(P_Carrosxcalle.shape[0]):
    el1 = 1
    el2 = N_vehiculosxhora[i]
    el3 = tipo_vehiculos[i]
    extra_element = [i * 3600, (i * 3600)+3600, N_vehiculosxhora[i]] + tipo_vehiculos[i].tolist()
    DatosRA[i] = np.insert(P_Carrosxcalle[i], 0, extra_element)

DatosRA = np.delete(DatosRA, 4, axis=1)

columnas = ['H_inicio', 'H_fin', 'N_carros', 'Livianos', 'Camiones','P_RA3', 'P_RA1', 'P_RA2']
GuardarenExcel(DatosRA, columnas, 'DatosRA.xlsx')
