from pysnmp.entity.rfc3413.oneliner import cmdgen
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def get_mac_table(ip_address, community='public', port=161):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((ip_address, port)),
        0, 25,
        '1.3.6.1.2.1.17.4.3.1'
    )

    if errorIndication:
        print(f"Error: {errorIndication}")
        return None
    elif errorStatus:
        print(f"Error: {errorStatus} at {errorIndex}")
        return None
    else:
        mac_table = []
        mac_address = []
        port = []
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                if '17.4.3.1.2' in name.prettyPrint() :
                    mac_address.append(val.prettyPrint())
                elif '17.4.3.1.1' in name.prettyPrint():
                    port.append(val.prettyPrint())

        mac_table =list(zip(mac_address,port))
        diccionario_final = {}

        for clave, valor in mac_table:
            if clave not in diccionario_final:
                diccionario_final[clave] = valor

        return diccionario_final


def mantener_primera_aparicion(diccionario):
    valores_encontrados = set()
    diccionario_resultante = {}

    for clave, valor in diccionario.items():
        if valor not in valores_encontrados:
            diccionario_resultante[clave] = valor
            valores_encontrados.add(valor)

    return diccionario_resultante

def obtener_mac_puertos_switch(ip, comunidad='public', puerto=161):
    cmdGen = cmdgen.CommandGenerator()

    # OID para la tabla de interfaces
    oid_tabla_interfaces = '1.3.6.1.2.1.2.2.1.6'

    # Realizar consulta SNMP
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData(comunidad),
        cmdgen.UdpTransportTarget((ip, puerto)),
        0, 25,  # Índices de inicio y fin
        oid_tabla_interfaces
    )

    if errorIndication:
        print(f"Error: {errorIndication}")
    elif errorStatus:
        print(f"Error: {errorStatus} at {errorIndex}")
    else:
        p = []
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                p.append(val.prettyPrint())

    return p



informacion_switches = {}

# Ejemplo de uso
for n in range(1, 5):
    server_ip='192.168.20.{0}'.format(n)
    mac_table_result = get_mac_table(server_ip)
    print(mac_table_result)
    puertos = obtener_mac_puertos_switch(server_ip)
    informacion_switches[server_ip] = {}
    informacion_switches[server_ip]['tabla_mac'] = mac_table_result
    informacion_switches[server_ip]['macs_puertos'] = puertos

def encontrar_clave_por_valor(diccionario, valor_buscar):
    for clave, valor in diccionario.items():
        if valor == valor_buscar:
            return clave
    return None  # Retorna None si no se encuentra ninguna coincidencia


def con_conex(infosw):
    n = len(infosw)
    mc = np.zeros((n,n))
    for i in range(0,n):
        server_ip1='192.168.20.{0}'.format(i+1)
        for j in range(0,n):
            server_ip2='192.168.20.{0}'.format(j+1)
            c_ports = informacion_switches[server_ip2]['macs_puertos']
            c_tabmacs = informacion_switches[server_ip1]['tabla_mac']
            for z in c_tabmacs.values():
                if z in c_ports:
                   clav = encontrar_clave_por_valor(c_tabmacs, z)
                   print('ESta conectado',i,j)
                   #mc[i,j] = clav
                   mc[i,j] = 1

    return mc



def graficar_topologia(matriz_adyacencia):
    # Crear un grafo dirigidoena
    G = nx.DiGraph()

    # Obtener el número de nodos
    num_nodos = len(matriz_adyacencia)

    # Agregar nodos al grafo
    G.add_nodes_from(range(1, num_nodos + 1))

    # Agregar arcos al grafo según la matriz de adyacencia
    for i in range(num_nodos):
        for j in range(num_nodos):
            if matriz_adyacencia[i][j] == 1:
                G.add_edge(i + 1, j + 1)

    # Crear el diseño del grafo y dibujarlo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20, linewidths=1, edge_color="gray")
    plt.title("Topología de la Red")
    plt.show()


