import paramiko

def conectar_ssh(ip, usuario, contraseña):
    try:
        # Conexión SSH al switch
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=usuario, password=contraseña)

        print("Conexión SSH establecida correctamente.")

        return ssh
    except Exception as e:
        print(f"Error al establecer la conexión SSH: {e}")
        return None

def cambiar_credenciales(ip_switch, usuario_actual, contraseña_actual, nuevo_usuario, nueva_contraseña):
    try:
        ssh = conectar_ssh(ip_switch, usuario_actual, contraseña_actual)
        if ssh:
            # Comandos para cambiar el usuario y la contraseña
            comandos = [
                f'configure terminal',
                f'username {nuevo_usuario} privilege 15 secret {nueva_contraseña}',  # Cambiar usuario y contraseña
                f'exit',
                f'write memory'  # Guardar la configuración
            ]

            # Ejecutar los comandos
            for comando in comandos:
                stdin, stdout, stderr = ssh.exec_command(comando)
                print(stdout.read().decode())

            print("Cambio de credenciales exitoso.")
            ssh.close()
    except Exception as e:
        print(f"Error al cambiar las credenciales: {e}")

def configurar_ip_switch(ip_switch, usuario, contraseña, ip_nueva, mascara, hostname):
    try:
        ssh = conectar_ssh(ip_switch, usuario, contraseña)
        if ssh:
            # Comandos para configurar la IP en el switch
            comandos = [
                f'configure terminal',
                f'hostname {hostname}',
                f'interface vlan 1',
                f'ip address {ip_nueva} {mascara}',  # Asignar la nueva dirección IP
                f'no shutdown',
                f'exit',
                f'exit',
                f'write memory'  # Guardar la configuración
            ]

            # Ejecutar los comandos
            for comando in comandos:
                stdin, stdout, stderr = ssh.exec_command(comando)
                print(stdout.read().decode())

            print("Configuración de la dirección IP exitosa.")
            ssh.close()
    except Exception as e:
        print(f"Error al configurar la dirección IP: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    ip_switch = '192.168.1.1'       # Dirección IP del switch
    mascara = '255.255.255.0'      # Macara
    hostname = 'SE_SUPER'
    usuario = 'admin'               # usuario por defecto del switch
    contraseña = 'password'         # contraseña por defecto del switch
    nuevo_usuario = 'nuevo_admin'   # Nuevo usuario para el switch
    nueva_contraseña = 'nueva_password'  # Nueva contraseña para el switch
    ip_nueva = '192.168.1.10'       # Nueva dirección IP para asignar al switch

    # Cambiar las credenciales del switch
    cambiar_credenciales(ip_switch, usuario, contraseña, nuevo_usuario, nueva_contraseña)

    # Configurar la dirección IP del switch
    configurar_ip_switch(ip_switch, nuevo_usuario, nueva_contraseña, ip_nueva, mascara, hostname)
