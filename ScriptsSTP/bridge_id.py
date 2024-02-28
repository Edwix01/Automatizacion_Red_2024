from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()


def bri_id(ips):
    #a = {'192.168.20.1':  '0x80010cb31dd00000', '192.168.20.2': '0x80010c8ed8960000', '192.168.20.3': '0x80010c59d8a50000',
    #      '192.168.20.4': '0x80010cdac7c60000','192.168.20.5': '0x80010cdecb160000','192.168.20.6': '0x80010c2d37e40000',}
    a = {}
    for server_ip in ips:
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData('public'),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            '1.3.6.1.2.1.2.2.1.6'
        )
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                if  (name.prettyPrint()).split('.')[-1] == "1":
                    a[server_ip] = "0x8001"+val.prettyPrint()[2::]
    return a
