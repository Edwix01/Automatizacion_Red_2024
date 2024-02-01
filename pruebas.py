from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

def get_active_interfaces(ip_addresses):
    interfaces_dict = {}

    for ip_address in ip_addresses:
        error_indication, error_status, error_index, var_bind_table = cmdGen.nextCmd(
            cmdgen.CommunityData('public'),
            cmdgen.UdpTransportTarget((ip_address, 161)),
            '1.3.6.1.2.1.2.2.1.8',  # ifAdminStatus
            lexicographicMode=False
        )

        error_indication, error_status, error_index, var_bind_table1 = cmdGen.nextCmd(
            cmdgen.CommunityData('public'),
            cmdgen.UdpTransportTarget((ip_address, 161)),
            '1.3.6.1.2.1.2.2.1.2',  # ifDescr
            lexicographicMode=False
        )

        active_interfaces = [val1.prettyPrint() for row, row1 in zip(var_bind_table, var_bind_table1) 
                             for (_, val), (_, val1) in zip(row, row1) if val.prettyPrint() == '1' and val1.prettyPrint() != "Null0"]

        interfaces_dict[ip_address] = active_interfaces

    return interfaces_dict

if __name__ == "__main__":
    ip_addresses_to_check = ['192.168.1.1', '192.168.1.2']  # Reemplaza con tus direcciones IP

    result_dict = get_active_interfaces(ip_addresses_to_check)

    for ip, interfaces in result_dict.items():
        print(f"Dirección IP: {ip}, Interfaces Activas: {', '.join(interfaces)}")
