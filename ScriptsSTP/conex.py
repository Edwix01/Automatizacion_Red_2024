import numpy as np

def con_com(ips,idp,ide):
    m = np.zeros((len(ips),len(ips)))
    k = 0
    for i in ips:
        l = 0
        for j in ips:
            if ( idp[i] in ide[j] ) and (l != k):
                m[k,l] = 1

            l +=1
        
        k+=1

    return m
