from scrapli.driver.core import GenericDriver

def connect_to_switch(host, username, password):
    """
    Conectar al switch TP-Link JetStream mediante SSH utilizando Scrapli.
    
    Args:
        host (str): Dirección IP del switch.
        username (str): Nombre de usuario para autenticación SSH.
        password (str): Contraseña para autenticación SSH.
    """
    # Configuración del driver de Scrapli para Genie (genérico)
    driver = GenericDriver(
        {
            "host": host,
            "auth_username": username,
            "auth_password": password,
            "auth_strict_key": False,  # Esto permite aceptar automáticamente la clave de host si es nueva
            "platform": "generic",
        }
    )

    try:
        # Conectar al dispositivo
        driver.open()
        print("Conexión establecida correctamente.")

        # Ejecutar un comando de ejemplo (puedes ejecutar otros comandos según tus necesidades)
        response = driver.send_command("show system information")
        print("Resultado del comando:")
        print(response.result)
    except Exception as e:
        print("Error al conectar al switch:", e)
    finally:
        # Cerrar la conexión
        driver.close()

# Ejemplo de uso
if __name__ == "__main__":
    host = "10.0.1.6"  # Dirección IP del switch TP-Link JetStream
    username = "networking"  # Nombre de usuario SSH
    password = "Ygvfe34a.2018"  # Contraseña SSH
    connect_to_switch(host, username, password)
