import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

dfRA = pd.read_excel('DatosRA.xlsx')
datosRA = dfRA.values
horas = datosRA[:,0:2]
def leer_datos(n_archivo):
    df = pd.read_excel(n_archivo)
    datos = df.values
    probabilidades = datos[:, 3:5]
    return probabilidades

"""archivos_origen = {
    'DatosRA.xlsx': "48909342#5",
    'DatosMS.xlsx': "337277984#6",
    'DatosCL.xlsx': "893257053",
    'DatosCLB.xlsx': "-60204530",
    'DatosSA.xlsx': "552651836",
    'DatosAA.xlsx': "42492699#4",
    'DatosV.xlsx': "940158936#2",
    'DatosJA.xlsx': "42143918#12",
    'DatosE.xlsx': "311212628#1",
    'DatosGC.xlsx': "554582109#1",
    'DatosRO.xlsx': "45421575#2",
    'DatosNU.xlsx': "48202925#1",
    'DatosPio1.xlsx': "399285452#3",
    'DatosPio2.xlsx': "542435212",
    'DatosCC.xlsx': "370601722#1",
}
"""
archivos_origen = {
    'DatosRA.xlsx': "48909342#5",}

Matriz_calle = {}
for n_archivo, id_origen in archivos_origen.items():
    autos_tipo = leer_datos(n_archivo)
    key = n_archivo.split('.')[0][5:]
    Matriz_calle[key] = {"datos": autos_tipo, "id_origen": id_origen}


raiz = ET.Element('flows')
AT_vehiculo = [["auto", "passenger","red", "6.56"],
               ["camion", "truck","white", "4.46"]]

for tipo in AT_vehiculo:
    id_vehiculo, tipo, color, factor_velocidad = tipo
    vtype = ET.SubElement(raiz, 'vType', {
        "id": id_vehiculo,
        "vClass": tipo,
        "color": color,
        "maxSpeed": factor_velocidad})

for intervalo_hora in range(len(horas)):
    intervalo = ET.SubElement(raiz, 'interval', {
        "begin": str(horas[intervalo_hora, 0]),
        "end": str(horas[intervalo_hora, 1])})
    for calle, info in Matriz_calle.items():
        datos_calle = info["datos"]
        id_origen = info["id_origen"]
        for i, tipo in enumerate(["auto", "camion"]):
            flow = ET.SubElement(intervalo, 'flow', {
                "id": (str(calle) + str(tipo) + str(intervalo_hora)),
                "from": id_origen,
                "number": str(int(1*datos_calle[intervalo_hora, i])),
                "type": tipo,
                "departLane": "free"})

ET.indent(raiz)
et = ET.ElementTree(raiz)
et.write("flujosRA.xml", xml_declaration=False)
