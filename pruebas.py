import networkx as nx
import matplotlib.pyplot as plt
import math

def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = {}
    if root is None:
        root = next(iter(nx.topological_sort(G)))  # Use el primer nodo en el orden topológico si no se especifica la raíz
    pos[root] = (xcenter, vert_loc)
    neighbors = list(G.neighbors(root))
    if len(neighbors) != 0:
        dx = width / 2
        nextx = xcenter - width / 2 - dx / 2
        for neighbor in neighbors:
            nextx += dx
            pos.update(hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap, vert_loc=vert_loc-vert_gap, xcenter=nextx))
    else:
        subnodes = [node for node in G.nodes() if node.startswith(root + '.')]
        if len(subnodes) != 0:
            dx = width / 2
            nextx = xcenter - width / 2 - dx / 2
            for subnode in subnodes:
                nextx += dx
                pos[subnode] = (nextx, vert_loc-2*vert_gap)
                pos[root] = (xcenter, vert_loc)
    return pos

def circular_positions(nodos):
    posiciones = {}
    # Encontrar el nodo principal y centrarlo
    root = None
    for nodo in nodos:
        if '.' not in nodo:  # Nodo principal
            root = nodo
            posiciones[root] = (0, 0)
            break

    if root is not None:
        # Configurar parámetros para la disposición circular
        num_subnodos = sum(1 for nodo in nodos if nodo.startswith(root + '.'))
        radio = 1
        angulo = 2 * math.pi / num_subnodos

        # Posicionar los subnodos alrededor del nodo principal en forma de círculo
        subnodo_count = 0
        for nodo in nodos:
            if nodo.startswith(root + '.'):
                x = radio * math.cos(subnodo_count * angulo)
                y = radio * math.sin(subnodo_count * angulo)
                posiciones[nodo] = (x, y)
                subnodo_count += 1

        # Avanzar hacia la derecha para los siguientes nodos principales
        x_offset = 2
        for nodo in nodos:
            if '.' not in nodo:  # Nodo principal
                if nodo != root:
                    posiciones[nodo] = (x_offset, 0)
                    x_offset += 2

    return posiciones


# Crear un grafo dirigido
grafo = nx.DiGraph()

# Agregar nodos al grafo
grafo.add_nodes_from(['A', 'B', 'C', 'A.1', 'A.2', 'B.1', 'B.2'])

# Agregar conexiones entre nodos
grafo.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'A.1'), ('B', 'A.2'), ('C', 'B.1'), ('C', 'B.2')])

# Calcular las posiciones de los nodos con hierarchy_pos
posiciones = circular_positions(grafo.nodes())

# Dibujar el grafo con posiciones ordenadas utilizando Matplotlib
plt.figure(figsize=(10, 8))
nx.draw(grafo, pos=posiciones, with_labels=True, node_size=1500, node_color='skyblue', font_size=12, font_weight='bold', edge_color='gray', arrows=True)
plt.title('Árbol con nodos principales y subnodos')
plt.show()
