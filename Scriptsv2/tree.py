import json

icon_capability_map = {
    'router': 'router',
    'switch': 'switch',
    'bridge': 'switch',
    'station': 'host'
}


def connection_tree_web(interconnections, port_info):
    connections = []
    for connection in interconnections:
        source_switch, source_port = connection[0].split('.')
        target_switch, target_port = connection[1].split('.')
        source_port_name = port_info.get(source_switch, {}).get(source_port)
        target_port_name = port_info.get(target_switch, {}).get(target_port)
        if source_port_name and target_port_name:
            connections.append([
                (f'switch{source_switch}', source_port_name),
                (f'switch{target_switch}', target_port_name)
            ])
    return connections

def get_icon_type(device_cap_name, device_model=''):
    """
    Device icon selection function. Selection order:
    - LLDP capabilities mapping.
    - Device model mapping.
    - Default 'unknown'.
    """
    if device_cap_name:
        icon_type = icon_capability_map.get(device_cap_name)
        if icon_type:
            return icon_type
    return 'unknown'

def generate_topology_json(*args):
    """
    JSON topology object generator.
    Takes as an input:
    - discovered hosts set,
    - LLDP capabilities dict with hostname keys,
    - interconnections list,
    - facts dict with hostname keys.
    """
    discovered_hosts, interconnections = args
    host_id = 0
    host_id_map = {}
    topology_dict = {'nodes': [], 'links': []}
    for host in discovered_hosts:
        host_id_map[host] = host_id
        topology_dict['nodes'].append({
            'icon':'switch',
            'id': host_id,
            'name': host,
        })
        host_id += 1
    link_id = 0

    for link in interconnections:
        topology_dict['links'].append({
            'id': link_id,
            'source': host_id_map[link[0][0]],
            'target': host_id_map[link[1][0]],
            'srcIfName': if_shortname(link[0][1]),
            'srcDevice': link[0][0],
            'tgtIfName': if_shortname(link[1][1]),
            'tgtDevice': link[1][0],
        })
        link_id += 1
    return topology_dict

# Función auxiliar si_shortname
def if_shortname(interface):
    return interface

def write_topology_file(topology_json, header, dst):
    with open(dst, 'w') as topology_file:
        topology_file.write(header)
        topology_file.write(json.dumps(topology_json, indent=4, sort_keys=True))
        topology_file.write(';')
