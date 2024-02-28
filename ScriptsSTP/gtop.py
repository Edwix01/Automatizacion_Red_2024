import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def generar_grafo_conexiones(matriz):
    G = nx.Graph()

    # Agregar nodos principales (dispositivos) con etiquetas personalizadas
    for i in range(len(matriz)):
        etiqueta_dispositivo = f"S_{i}"
        G.add_node(i, etiqueta=etiqueta_dispositivo, size=1500, color='blue')

    # Agregar subnodos y conexiones con etiquetas personalizadas
    for i in range(len(matriz)):
        for j in range(1,10):
            subnodo_id = f"{i}-{j}"
            G.add_node(subnodo_id, size=500, color='red')
            G.add_edge(i, subnodo_id)

    # Agregar conexiones entre subnodos según la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            conexion = matriz[i,j]
            if conexion != 0:
                a = matriz[i,j]
                b = matriz[j,i]
                subnodo_i = f"{i}-{a}"
                subnodo_j = f"{j}-{b}"
                G.add_edge(subnodo_i, subnodo_j)
                G.nodes[subnodo_i]['color'] = 'green'
                G.nodes[subnodo_j]['color'] = 'green'
    return G


def ac_pu(G,stp_p):
    for i in stp_p:
        x,y = i
        subnodo_a = f"{x}-{y}"
        G.nodes[subnodo_a]['color'] = 'yellow'

    G1=G
    return G1

def dibujar_grafo(G):
    pos = nx.spring_layout(G, seed=50)
    etiquetas = {node: G.nodes[node].get('etiqueta', node) for node in G.nodes()}  # Obtener etiquetas personalizadas

    node_colors = [node[1].get('color', 'red') for node in G.nodes(data=True)]
    node_sizes = [node[1].get('size', 300) for node in G.nodes(data=True)]

    nx.draw(G, pos, labels=etiquetas, with_labels=True, node_size=node_sizes, font_size=10, node_color=node_colors, font_color='black', edge_color='black')
    plt.show()

"""
# Ejemplo de matriz de conexiones
matriz = np.array([[0, 2, 3, 0],
          [2, 0, 4, 3],
          [3, 4, 0, 2],
          [0, 3, 2, 0]])

a = {1: (0, 1), 4: (3, 1)}


grafo = generar_grafo_conexiones(matriz)
g_aux = ac_pu(grafo,a.values(),matriz)
dibujar_grafo(g_aux)
"""