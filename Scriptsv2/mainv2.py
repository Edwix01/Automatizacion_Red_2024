import bridge_id
import stp_info
import com_conex
import des_disp
import des_int_act
import gr
import networkx as nx
import matplotlib.pyplot as plt
import random
import map_int
import stp_blk
import verstp
import matplotlib.colors as mcolors

comunidad = "$1$5.v/c/$"
direc = des_disp.in_des()
#Descubrir Interfaces activas 
d = (des_int_act.in_act(direc,comunidad))
direc = d.keys()

info_int = map_int.ma_int(direc,comunidad)


b_id = bridge_id.bri_id(direc,comunidad)

st_inf = stp_info.stp_inf(direc,comunidad)

l = com_conex.b_conex(direc,b_id,st_inf)


# Crear una lista para almacenar los primeros números antes del punto
l1 = []

# Recorrer todas las tuplas y dentro de cada tupla obtener el primer número antes del punto
for tupla in l:
    for elemento in tupla:
        nodo_principal = elemento.split('.')[0]
        if nodo_principal not in l1:
            l1.append(nodo_principal)


# Define los colores para los nodos
# Definir colores pastel predefinidos
colores_pastel = {
    'pastel_blue': mcolors.CSS4_COLORS['lightblue'],    # Azul pastel
    'pastel_green': mcolors.CSS4_COLORS['lightgreen'],  # Verde pastel
    'pastel_yellow': mcolors.CSS4_COLORS['lightcoral'] # Amarillo pastel
}

# Reemplazar los colores en colores_nodos con colores pastel
colores_nodos= {
    'principal': colores_pastel['pastel_blue'],   # Azul pastel para nodos principales
    'subnodo': colores_pastel['pastel_green'],    # Verde pastel para subnodos
    'subnodob': colores_pastel['pastel_yellow']   # Amarillo pastel para subnodos
}

nf = verstp.obtener_numeros_despues_del_punto(l)

nodb=stp_blk.stp_status(direc,nf,comunidad)

# Crear el grafo
grafo = gr.crear_grafo(l1, l, info_int, colores_nodos,nodb)

# Determinar tamaños de los nodos individualmente
tamanos_nodos = [grafo.nodes[nodo]['size'] for nodo in grafo.nodes()]

# Dibujar el grafo con posiciones fijas utilizando el algoritmo Kamada-Kawai
posiciones = nx.spring_layout(grafo,seed=42)
nx.draw(grafo, pos=posiciones, with_labels=True, labels=nx.get_node_attributes(grafo, 'label'), node_size=tamanos_nodos, node_color=[grafo.nodes[nodo]['color'] for nodo in grafo.nodes()], font_size=8, font_weight='bold',font_family="serif")

plt.show()
