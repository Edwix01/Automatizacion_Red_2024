from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

def inf_int(dir):
    m = {}
    for server_ip in dir:
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData('public'),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            #'1.3.6.1.2.1.2.2.1.6' #MACS de las interfaces
            '1.3.6.1.2.1.2.2.1.1'
        ) 


        errorIndication1, errorStatus1, errorIndex1, varBindTable1 = cmdGen.bulkCmd(
            cmdgen.CommunityData('public'),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            #'1.3.6.1.2.1.2.2.1.6' #MACS de las interfaces
            '1.3.6.1.2.1.2.2.1.6'
        ) 
        l = []
        k = []

        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                l.append(val.prettyPrint())

        for varBindTableRow1 in varBindTable1:
            for name1, val1 in varBindTableRow1:
                k.append(val1.prettyPrint())

        res = dict(zip(l, k))
        m[server_ip] = res

    return m
