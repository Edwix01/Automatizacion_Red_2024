import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

dfRA = pd.read_excel('DatosRA.xlsx')
datosRA = dfRA.values
horas = datosRA[:,0:2]
dfgiros = pd.read_excel('ID_GIROS.xlsx')
datosgiros = dfgiros.values
id_giros = datosgiros[:,1:]

def leer_datos(n_archivo, columnas):
    df = pd.read_excel(n_archivo)
    datos = df.values
    probabilidades = datos[:, columnas]
    return probabilidades

archivos_y_columnas = {
    'DatosRA.xlsx': (slice(5, 8), "48909342#5"),
    'DatosMS.xlsx': (slice(5, 8), "337277984#6"),
    'DatosCL.xlsx': (slice(5, 8), "893257053"),
    'DatosCLB.xlsx': (slice(5, 6), "-60204530"),
    'DatosSA.xlsx': (slice(5, 6), "552651836"),
    'DatosAA.xlsx': (slice(5, 8), "42492699#4"),
    'DatosV.xlsx': (slice(5, 8), "940158936#2"),
    'DatosJA.xlsx': (slice(5, 8), "42143918#12"),
    'DatosE.xlsx': (slice(5, 8), "311212628#1"),
    'DatosGC.xlsx': (slice(5, 8), "554582109#1"),
    'DatosRO.xlsx': (slice(5, 8), "45421575#2"),
    'DatosNU.xlsx': (slice(5, 8), "48202925#1"),
    'DatosPio1.xlsx': (slice(5, 6), "399285452#3"),
    'DatosPio2.xlsx': (slice(5, 6), "542435212"),
    'DatosCC.xlsx': (slice(5, 6), "370601722#1"),
    'DatosMS1.xlsx': (slice(2, 4), "-389741416"),
    'DatosGC1.xlsx': (slice(2, 5), "554582109#2"),
    'DatosRO1.xlsx': (slice(5, 8), "45421575#3"),
    'DatosNU1.xlsx': (slice(5, 7), "542435211"),
}


Matriz_calle = {}
for n_archivo, (columnas, id_origen) in archivos_y_columnas.items():
    probabilidades = leer_datos(n_archivo, columnas)
    key = n_archivo.split('.')[0][5:]  # Obtener la clave a partir del nombre del archivo
    Matriz_calle[key] = {"datos": probabilidades, "id_origen": id_origen}

giros = ET.Element('turns')

for intervalo_hora in range(len(horas)):
    intervalo = ET.SubElement(giros, 'interval', {
        "begin": str(horas[intervalo_hora, 0]),
        "end": str(horas[intervalo_hora, 1])})
    for i, (calle, info) in enumerate(Matriz_calle.items()):
        datos_calle = info["datos"]
        id_origen = info["id_origen"]
        origen = ET.SubElement(intervalo, 'fromEdge', {"id": id_origen})
        for edge_giro in range((datos_calle.shape)[1]):
            destino = ET.SubElement(origen, 'toEdge', {
                "id": str(id_giros[(2*i)+1,edge_giro]),
                "probability": str(datos_calle[intervalo_hora, edge_giro])})


ET.indent(giros)
et = ET.ElementTree(giros)
et.write("giros.xml", xml_declaration=False)
