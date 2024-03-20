import bridge_id
import stp_info
import com_conex
import des_disp
import des_int_act
import gr
import map_int
import stp_blk
import verstp


# Ingreso de Parametros - Comunidad SNMP, Direcciones IP

comunidad = "$1$5.v/c/$"
direc = des_disp.in_des()

#Detección de interfaces activas 
d = (des_int_act.in_act(direc,comunidad))
direc = d.keys() #Direcciones IP Filtradas

info_int = map_int.ma_int(direc,comunidad)

#Informacion STP
# Bridge ID, Designed Bridge
b_id = bridge_id.bri_id(direc,comunidad)
st_inf = stp_info.stp_inf(direc,comunidad)

#Identificación de Conexiones
l = com_conex.b_conex(direc,b_id,st_inf)

#Filtro de Switches sin conexiones
"""
l1 = []
for tupla in l:
    for elemento in tupla:
        nodo_principal = elemento.split('.')[0]
        if nodo_principal not in l1:
            l1.append(nodo_principal)
"""


#Deteccion de puertos habilitados con stp
#Detección de puertos bloqueados por stp
nf = verstp.obtener_numeros_despues_del_punto(l)
nodb=stp_blk.stp_status(direc,nf,comunidad)

#Creación del grafo
grafo = gr.crear_grafo(direc, l, info_int,nodb)
gr.dibujar_grafo(grafo)
