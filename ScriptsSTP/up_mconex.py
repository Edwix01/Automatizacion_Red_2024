def upm(ips,matriz,pstp,bids,inf,tmac):
    cl = pstp.keys()
    m_a =matriz
    p_stp = []
    for ip in cl:
        i = ips.index(ip)
        valor_a_buscar = pstp[ip][1]
        claves = [clave for clave, valor in bids.items() if valor == valor_a_buscar]
        j = ips.index(claves[0])
        m_a[i,j] = pstp[ip][0]
        g = inf[ip][(pstp[ip][0])]
        g1 = tmac[claves[0]][g]
        m_a[j,i] = g1
        p_stp.append((i,pstp[ip][0]))
    return m_a,p_stp