from pysnmp.entity.rfc3413.oneliner import cmdgen
import numpy as np
cmdGen = cmdgen.CommandGenerator()
import gtop

def get_macs(dir,comunidad):
    
    ma = {}
    for ip in dir:
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((ip, 161)),
            0,25,
            '1.3.6.1.2.1.2.2.1.6'
            #'1.3.6.1.2.1.2'
        ) 
        inte = []
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                inte.append((val.prettyPrint()))
            
        ma[ip] = inte
    return ma

def tab_macs(dir,comunidad):
    
    ma = {}
    for ip in dir:
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((ip, 161)),
            0,25,
            '1.3.6.1.2.1.17.4.3.1.1'
        ) 

        errorIndication1, errorStatus1, errorIndex1, varBindTable1 = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((ip, 161)),
            0,25,
            '1.3.6.1.2.1.17.4.3.1.2'
        ) 

        l = []
        l1 = []
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                l.append((val.prettyPrint()))

        for varBindTableRow1 in varBindTable1:
            for name, val1 in varBindTableRow1:
                l1.append((val1.prettyPrint()))


        res = dict(zip(l, l1))
        
        ma[ip] = res
    return ma

def desg_bridge(ips,ma,macs,tabmacs,stpp):
        n = len(ma)-1
        mauc = ma
        for i in range(n+1):
            for j in range(n+1):
                if (((ma[i,j] != 0) or (ma[j,i] != 0)) and (i!=j)):
                    for u in macs[ips[i]]:
                        for h in stpp:
                            if h in tabmacs[ips[j]]:
                                del tabmacs[ips[j]][h]
                        
                        if u in tabmacs[ips[j]]:
                            mauc[i,j] = tabmacs[ips[j]][u]
                            """
                            print(""*20)
                            print(u)
                            print(tabmacs[ips[j]])
                            print(""*20)
                            print(np.transpose(mauc.astype(int)))             
                            """
        return mauc.astype(int)
