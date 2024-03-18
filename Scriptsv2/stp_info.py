from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

comunidad = "public"
a = {}
def stp_inf(direc,comunidad):
    for server_ip in direc:
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            #'1.3.6.1.2.1.17.1.1',
            '1.3.6.1.2.1.17.2.15.1.8'
            #'1.3.6.1.2.1.2.2.1.2'
            #'1.3.6.1.2.1.2.2.1.6'
            #'1.3.6.1.2.1.17.4.3.1.1'
        )

        errorIndication1, errorStatus1, errorIndex1, varBindTable1 = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            #'1.3.6.1.2.1.17.1.1',
            '1.3.6.1.2.1.17.2.15.1.9'
            #'1.3.6.1.2.1.2.2.1.2'
            #'1.3.6.1.2.1.2.2.1.6'
            #'1.3.6.1.2.1.17.4.3.1.1'
        )

        db = []
        pd = []
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                db.append((val.prettyPrint())[-12:])

        for varBindTableRow1 in varBindTable1:
            for name1, val1 in varBindTableRow1:
                pd.append((str(name1).split(".")[-1], (val1.prettyPrint())[-12:]))

        a[server_ip] = [db,pd]
    return a


