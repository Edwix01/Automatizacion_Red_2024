import b_id
import stp_info
import com_conex
import des_disp
import des_int_act
import gr
import map_int
import stp_blk
import verstp

#Fase 1
print("Ejecutando fase 1")
# Ingreso de Parametros - Comunidad SNMP, Direcciones IP
comunidad = "public"
#direc = des_disp.in_des()
direc = ["192.168.20.1","192.168.20.2","192.168.20.3","192.168.20.4","192.168.20.5","192.168.20.6"]

#Fase 2
print("Ejecutando fase 2")
#Informacion STP
# Bridge ID, Designed Bridge
b_id = b_id.bri_id(direc,comunidad)
st_inf = stp_info.stp_inf(direc,comunidad)

#Fase 3 
print("Ejecutando fase 3")
#Identificación de Conexiones
l = com_conex.b_conex(direc,b_id,st_inf)
print(l)

#Fase 4
print("Ejecutando Fase 4")
#Deteccion de puertos habilitados con stp
nf = verstp.obtener_numeros_despues_del_punto(l)
nodb=stp_blk.stp_status(direc,nf,comunidad)
#Creación del grafo
info_int = map_int.ma_int(direc,comunidad)
grafo = gr.crear_grafo(direc, l, info_int,nodb)
gr.dibujar_grafo(grafo)
