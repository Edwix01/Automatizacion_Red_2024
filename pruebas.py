import subprocess

def connect_to_switch():
    """
    Conectarse al switch Tplink Jet Stream mediante SSH.
    """
    # Comando SSH
    command = [
        'ssh',
        '-o', 'KexAlgorithms=+diffie-hellman-group1-sha1',
        '-o', 'HostKeyAlgorithms=+ssh-dss',
        '-c', 'aes256-cbc',
        'networking@10.0.1.13'
    ]
    
    try:
        # Ejecutar el comando SSH
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("Error al conectar al switch:", e)

# Conectarse al switch
connect_to_switch()
