import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def gr(matriz):

    G = nx.from_numpy_matrix(matriz)

    # Dibujar el gráfico
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=1000, font_size=10)
    plt.show()
