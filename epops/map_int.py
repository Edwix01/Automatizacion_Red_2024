from pysnmp.entity.rfc3413.oneliner import cmdgen
import re
cmdGen = cmdgen.CommandGenerator()
d2={}

def ma_int(direc,datos):
    for server_ip in direc:
        comunidad = datos[server_ip]["snmp"]
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            '1.3.6.1.2.1.2.2.1.2'
        )
        c=1
        d1 = {}
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                if "Ethernet" in val.prettyPrint() and  not("0/0" in val.prettyPrint() ) :
                    # Utilizar una expresión regular para extraer la primera letra y los números
                    cadena = val.prettyPrint()
                    # Utilizar una expresión regular para encontrar solo los números y barras
                    numeros = re.sub(r'[^\d/]', '', cadena)
                    if datos[server_ip]["marca"] == "tplink":
                        d1[str(name).split(".")[-1]] = cadena[0] + numeros
                    else:
                        d1[str(c)] = cadena[0] + numeros
                    c+=1
        d2[str(server_ip.split(".")[-1])] = d1
    return d2


