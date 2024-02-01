import subprocess

def check_device_availability(ip):
    try:
        # Ejecutar el comando ping con un timeout de 2 segundos
        subprocess.run(["ping", "-c", "1", "-W", "2", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def dis_act(barra,i,s):
    da = []
    for n in range(i, s):
        last_dot_index = barra.rfind(".")+1
        sip = barra[:last_dot_index]
        device_ip = sip+"{0}".format(n)
        if check_device_availability(device_ip):
            da.append(device_ip)

    return da

if __name__ == "__main__":
    print(dis_act("192.168.20.1",3,6))
    
