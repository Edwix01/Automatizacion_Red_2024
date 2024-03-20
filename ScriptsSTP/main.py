import des_int_act 
import desig_stp
import bridge_id
import conex
import gra
import ver_int
import gtop
import numpy as np
import blkstp
import up_mconex
import info_int
import stp_blk
import des_disp

"""
En esta seccion se ejecutan los procesos necesarios para 
el descrubrimiento de la topologia
"""

#Descubrir dispositivos Activos
comunidad = "$1$5.v/c/$"
direc = des_disp.in_des()
#Descubrir Interfaces activas 
d = (des_int_act.in_act(direc,comunidad))
direc = d.keys()

"""
#Obtener los bridges designados por cada puerto activo
a = desig_stp.desg_bridge(d,comunidad)
print(a)
#Obtener ID Bridge de cad2
# a conmutador en la red
e = bridge_id.bri_id(direc,comunidad)
print(e)


#Establecer primera aproximacion de conexiones entre dispositivos
#No existe informacion de los puertos
m = conex.con_com(direc,e,a)
gra.gr(m)
"""

#Obtener la mac de cada una de las interfaces de los dispositivos
mas =  ver_int.get_macs(direc,comunidad)
print(mas)


#Obtener la tabla de direcciones Macs de cada conmutador
t = ver_int.tab_macs(direc,comunidad)
print(t)
"""
#Copia de las tablas macs
t1 = ver_int.tab_macs(direc)

#Establecer conexiones con especificacion de los puertos
#conectados

pstp = stp_blk.dstp_act(direc)
mf = np.transpose(ver_int.desg_bridge(direc,m,mas,t,pstp))

#Obtener puertos bloqueados por stp
psblk = blkstp.stp_act(direc)

#Obtener informacion de las interfaces N.depuerto/Mac del puerto
inf = info_int.inf_int(direc)

#Actualizacion de conexiones definiendo puertos bloqueados
maa,lstp = up_mconex.upm(direc,mf,psblk,e,inf,t1)

#graficas
print(maa)
grafo = gtop.generar_grafo_conexiones(maa)
gr = gtop.ac_pu(grafo,lstp)
gtop.dibujar_grafo(gr)
"""