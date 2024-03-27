import bridge_id
import stp_info
import com_conex
import des_disp
import des_int_act
import gr
import map_int
import stp_blk
import verstp
import time 

# Ingreso de Parametros - Comunidad SNMP, Direcciones IP
comunidad = "$1$5.v/c/$"
direc = des_disp.in_des()

tif1 = time.time()
#Fase 1
#Detección de interfaces activas 
#d = (des_int_act.in_act(direc,comunidad))
#direc = d.keys() #Direcciones IP Filtradas
tff1 = time.time()
print("Tiempo en fase 1: ",(tff1-tif1))


tif2 = time.time()
#Fase 2
#Informacion STP
# Bridge ID, Designed Bridge
b_id = bridge_id.bri_id(direc,comunidad)
st_inf = stp_info.stp_inf(direc,comunidad)
tff2 = time.time()
print("Tiempo en fase 2: ",(tff2-tif2))
print(b_id)
print(st_inf)
tif3 = time.time()
#Fase 3
#Identificación de Conexiones
l = com_conex.b_conex(direc,b_id,st_inf)
print(l)
tff3 = time.time()
print("Tiempo en fase 3: ",(tff3-tif3))

#Filtro de Switches sin conexiones
"""
l1 = []
for tupla in l:
    for elemento in tupla:
        nodo_principal = elemento.split('.')[0]
        if nodo_principal not in l1:
            l1.append(nodo_principal)
"""
tif4 = time.time()
#Fase 4
#Deteccion de puertos habilitados con stp
#Detección de puertos bloqueados por stp
nf = verstp.obtener_numeros_despues_del_punto(l)
nodb=stp_blk.stp_status(direc,nf,comunidad)
tff4 = time.time()
print("Tiempo en fase 4: ",(tff4-tif4))


tif5 = time.time()
#Fase 5
#Creación del grafo
info_int = map_int.ma_int(direc,comunidad)
grafo = gr.crear_grafo(direc, l, info_int,nodb)
tff5 = time.time()
print("Tiempo en fase 5: ",(tff5-tif5))
gr.dibujar_grafo(grafo)

