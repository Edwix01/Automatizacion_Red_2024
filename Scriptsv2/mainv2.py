import bridge_id
import stp_info
import com_conex
import des_disp
import des_int_act
import map_int
import stp_blk
import verstp
import time 
import leer
import tp_linkssh
import f
import obt_infyam
import obt_tplink
import obt_root
import tree

print("Ejecutando Fase 1")
#Fase 1
#Lectura de Archivo Yaml - Configuraciones
nombreyaml = "dispositivos.yaml"
datos = obt_infyam.infyam(nombreyaml)
direc = datos.keys()
iptp,credenciales = obt_tplink.filtplink(nombreyaml)
b_root = obt_root.obtr(datos,iptp)

print("Ejecutando Fase 2")
#Fase 2
#Informacion STP
# Bridge ID, Designed Bridge
b_id = bridge_id.bri_id(direc,datos)
st_inf = stp_info.stp_inf(direc,datos)

#Proceso extra para conmutadores TPLINK
f.epmiko(credenciales[iptp[0]]["usuario"],credenciales[iptp[0]]["contraseña"], iptp)
tp_d = leer.fil_bid("b_id.txt")
b_root = "c02c17093c00"
stn = tp_linkssh.tplink_id(b_root,st_inf,tp_d) 

print("Ejecutando Fase 3")
#Fase 3
#Identificación de Conexiones
l = com_conex.b_conex(direc,b_id,stn)
print(l)

#Mapeo de Las etiquetas
info_int = map_int.ma_int(direc,datos)
print(info_int)


interconnections = tree.connection_tree_web(l,info_int)
discovered_hosts = ['switch3', 'switch4', 'switch5', 'switch6', 'switch7', 'switch8','switch9', 'switch10', 'switch11', 'switch12','switch13', 'switch14', 'switch15', 'switch16','switch17', 'switch18', 'switch19', 'switch20','switch21']
print(interconnections)
OUTPUT_TOPOLOGY_FILENAME = 'topology.js'
TOPOLOGY_FILE_PATH = r"/home/du/Auto_Mon_2024_Cod/Automatizacion_Red_2024/Scriptsv2/app/topology.js"
TOPOLOGY_FILE_HEAD = f"\n\nvar topologyData = "
TOPOLOGY_DICT = tree.generate_topology_json(discovered_hosts, interconnections)
tree.write_topology_file(TOPOLOGY_DICT,TOPOLOGY_FILE_HEAD,TOPOLOGY_FILE_PATH )
print('HOLAAAAAAAAAAAAAAAAAAAA')
print(TOPOLOGY_DICT)
