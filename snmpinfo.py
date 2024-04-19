from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

server_ip="10.0.1.13"
print ("\nFetching stats for...", server_ip)
errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
    cmdgen.CommunityData('$1$5.v/c/$'),
    cmdgen.UdpTransportTarget((server_ip, 161)),
    0,25,
    #'1.3.6.1.2.1.17.1.1',
    #'1.3.6.1.4.1.9.2.1.58' #Cisco
    #"1.3.6.1.4.1.25506.2.6.1.1.1.1.6"# HPE
    "1.3.6.1.4.1.11863.6.4.1.1.1.1.2" #Tpling
    #"1.3.6.1.2.1.25.3.3.1.2"
    #'1.3.6.1.2.1.2.2.1.6'
    #'1.3.6.1.2.1.17.4.3.1.1'
)
c=0
for varBindTableRow in varBindTable:
    for name, val in varBindTableRow:
            print(name.prettyPrint())
            print(val.prettyPrint())