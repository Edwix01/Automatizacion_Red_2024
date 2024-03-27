import graphic_topology_tree
import tree_network_connection

def main():
    
    username = 'test'
    password = 'test'

    device_data, neighbor_device_data, blocked_ports_current_device = tree_network_connection.general_data_device(username, password)
    device_connections, int_device_connections = tree_network_connection.identify_connections(device_data, neighbor_device_data)

    ##### GRAFICA SIN PUERTOS #####
    graphic_topology_tree.device_connection(device_connections)
    #### GRAFICA CON PUERTOS ####
    graphic_topology_tree.device_connection_interfaces_block(int_device_connections,blocked_ports_current_device)


if __name__ == "__main__":
    main()
