import subprocess

def tplinkmiko(username, password, host, comando):
    # Ruta al script de Expect
    script_expect = "./tp_linkssh.sh"
    
    # Argumentos para el script de Expect
    args = [script_expect, username, password, host, comando]
    
    try:
        # Ejecutar el script de Expect
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script de Expect: {e}")

# Ejemplo de uso
username = "networking"
password = "Ygvfe34a.2018"
host = "10.0.1.13"
comando = "show spanning-tree active"

tplinkmiko(username, password, host, comando)

