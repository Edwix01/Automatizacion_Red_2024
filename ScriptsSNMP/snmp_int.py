from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

for n in range(1, 5):
    server_ip="192.168.20.{0}".format(n)
    print ("\nFetching stats for...", server_ip)
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData('public'),
        cmdgen.UdpTransportTarget((server_ip, 161)),
        0,16,
        '1.3.6.1.2.1.2.2.1.8'
    )

    estado = []
    inte = []
    for varBindTableRow in varBindTable:
        for name, val in varBindTableRow:
            if (val.prettyPrint()) == '1':
                estado.append(1)
            else:
                estado.append(0)

print(estado)
