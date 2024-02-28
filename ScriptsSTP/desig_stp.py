from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

def desg_bridge(ips,in_fa):
    
    ma = {}
    for ip in ips:
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData('public'),
            cmdgen.UdpTransportTarget((ip, 161)),
            0,25,
            ' 1.3.6.1.2.1.17.2.15.1.8'
            #'1.3.6.1.2.1.2'
        ) 
        inte = []


        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                    if (name.prettyPrint()).split('.')[-1] in in_fa[ip]:
                        inte.append((val.prettyPrint()))
            
        ma[ip] = inte
    return ma