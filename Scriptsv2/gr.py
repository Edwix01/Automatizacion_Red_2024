import networkx as nx
import matplotlib.pyplot as plt
import random

import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo(direcciones, conexiones, etiquetas, colores,nodb):
    # Crear un nuevo grafo dirigido
    G = nx.DiGraph()

    # Paso 1: Agregar nodos principales y definir su tamaño
    for direccion in direcciones:
        nodo_id = direccion.split('.')[-1]
        G.add_node(nodo_id, size=1000, color=colores['principal'])  # Asignar color azul a los nodos principales
        # Agregar etiquetas personalizadas
        G.nodes[nodo_id]['label'] = 'S' + nodo_id

    # Paso 2: Agregar subnodos
    for conexion in conexiones:
        subnodo_id, tupla_id = conexion

        # Paso 3: Separar el identificador del subnodo para obtener el nodo principal
        nodo_principal_id1 = subnodo_id.split('.')[0]
        nodo_principal_id2 = tupla_id.split('.')[0]

        e_id1 = subnodo_id.split('.')[1]
        e_id2 = tupla_id.split('.')[1]

        e1 = etiquetas[nodo_principal_id1][e_id1]
        e2 = etiquetas[nodo_principal_id2][e_id2]

        G.add_node(subnodo_id, size=100, color=colores['subnodo'])  # Asignar color verde a los subnodos
        G.add_node(tupla_id, size=100, color=colores['subnodo'])    # Asignar color verde a los subnodos

        # Agregar etiquetas personalizadas
        G.nodes[subnodo_id]['label'] = e1
        G.nodes[tupla_id]['label'] = e2

        # Establecer conexiones
        G.add_edge(subnodo_id, tupla_id)
        G.add_edge(nodo_principal_id1, subnodo_id)
        G.add_edge(nodo_principal_id2, tupla_id)
    for xn in nodb:
        G.add_node(xn, size=100, color=colores['subnodob'])    # Asignar color verde a los subnodos

    return G




