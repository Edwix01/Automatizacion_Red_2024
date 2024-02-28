from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

def stp_act(dir_ip):
    intef = {}
    #Recorrer una lista con la direccion de los dispositivos activos
    for server_ip in dir_ip:
        f = 0
        errorIndication, errorStatus, errorIndex, varBindTable1 = cmdGen.bulkCmd(
            cmdgen.CommunityData('public'),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,16,
            '1.3.6.1.2.1.17.2.15.1.1' #OID del Puerto STP
        )
        
        errorIndication1, errorStatus1, errorIndex1, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData('public'),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,16,
            '1.3.6.1.2.1.17.2.15.1.3' #OID del estado del puerto STP
        )

        errorIndication2, errorStatus2, errorIndex2, varBindTable2 = cmdGen.bulkCmd(
            cmdgen.CommunityData('public'),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,16,
            '1.3.6.1.2.1.17.2.15.1.8' #OID del estado del puerto STP
        )


        estado = []
        l = []
        k = []
        #1 si el puerto esta bloqueado por STP, 0 si no esta bloqueado
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                if (val.prettyPrint()) == '2':
                    f = 1
                    estado.append(1)
                else:
                    estado.append(0)


        c = 0
        #Reconocer la interfaz bloqueada
        for varBindTableRow1 in varBindTable1:
            for name1, val1 in varBindTableRow1:
                if (estado[c] == 1):
                    l = val1.prettyPrint()
                c = c+1
        c = 0
                #Reconocer la interfaz bloqueada
        for varBindTableRow2 in varBindTable2:
            for name2, val2 in varBindTableRow2:
                if (estado[c] == 1):
                    #k = (val2.prettyPrint())[-12:]
                    k = (val2.prettyPrint())
                c = c+1

        res = [l,k]
        if f == 1:
            intef[server_ip]= res
    return intef
