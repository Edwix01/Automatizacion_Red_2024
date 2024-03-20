from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

def desg_bridge(in_fa,cmsnmp):
    
    ma = {}
    for ip in in_fa.keys():
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(cmsnmp),
            cmdgen.UdpTransportTarget((ip, 161)),
            0,25,
            '1.3.6.1.2.1.17.2.15.1.8'
            #'1.3.6.1.2.1.2'
        ) 
        inte = []


        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                        inte.append((val.prettyPrint())[-12:])
            
        ma[ip] = inte
    return ma