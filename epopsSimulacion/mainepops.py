import b_id
import stp_info
import com_conex
import des_disp
import des_int_act
import map_int
import stp_blk
import verstp
import time
import dtsnmp


direc = ["10.0.1.1","10.0.1.2","10.0.1.3","10.0.1.4","10.0.1.5","10.0.1.6"]

def main_top(direc):
    #Fase 1
    #print("Ejecutando fase 1")
    # Ingreso de Parametros - Comunidad SNMP, Direcciones IP
    comunidad = "public"
    #direc = des_disp.in_des()

    #Fase 2
    #print("Ejecutando fase 2")
    #Informacion STP
    # Bridge ID, Designed Bridge
    bid,f1,fif1= b_id.bri_id(direc,comunidad)
    st_inf,f2,fif2 = stp_info.stp_inf(direc,comunidad)
    f = f1 or f2

    fif = dtsnmp.snmt(fif1,fif2)

    print(f,fif)
    #Fase 3 
    #print("Ejecutando fase 3")
    #Identificación de Conexiones

    l = com_conex.b_conex(direc,bid,st_inf)


    """ 
    #Fase 4
    print("Ejecutando Fase 4")
    #Deteccion de puertos habilitados
     con stp


    #Creación del grafo
    info_int = map_int.ma_int(direc,comunidad)
    grafo = gr.crear_grafo(direc, l, info_int,nodb)
    gr.dibujar_grafo(grafo)
    """
    return l,f,list(fif.keys())

