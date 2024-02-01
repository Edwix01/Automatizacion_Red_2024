from prettytable import PrettyTable

def display_interface_table(interface_dict):
    table = PrettyTable()
    table.field_names = ["Dirección IP", "Interfaces Activas"]

    for ip, interfaces in interface_dict.items():
        table.add_row([ip, ", ".join(interfaces)])

    print(table)

if __name__ == "__main__":
    # Ejemplo de un diccionario con direcciones IP y sus interfaces activas
    ip_interface_dict = {
        '192.168.1.1': ['eth0', 'eth1'],
        '192.168.1.2': ['eth2'],
        '192.168.1.3': ['eth3', 'eth4']
    }

    display_interface_table(ip_interface_dict)
