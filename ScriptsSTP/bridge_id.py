from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()


def bri_id(ips,comunidad):
    a = {}
    for server_ip in ips:
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            '1.3.6.1.2.1.17.1.1'
        )
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                a[server_ip] = (val.prettyPrint())[-12:]
    return a
