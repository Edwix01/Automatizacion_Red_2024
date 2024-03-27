from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

def stp_act(dir_ip):
    intef = {}
    #Recorrer una lista con la direccion de los dispositivos activos
    for server_ip in dir_ip:
        f = 0
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData('public'),
        cmdgen.UdpTransportTarget((server_ip, 161)),
        0,25,
        '1.3.6.1.2.1.17.2.15.1.3',
        '1.3.6.1.2.1.17.2.15.1.8'
        )
        inte = []
        f=0
        et = ""
        for varBindTableRow in varBindTable:
            for name,val in varBindTableRow:
                if f == 1 and name[-1] == et:
                    inte = [str(name[-1]),val.prettyPrint()]   
                    f = 0
                if val == 2:
                    f = 1
                    et = name[-1]

        if len(inte) != 0:
            intef[server_ip]= [inte]
    
    return intef
