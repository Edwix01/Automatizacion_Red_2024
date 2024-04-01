import yaml

# Cargar el archivo YAML
with open("/home/du/Auto_Mon_2024_Cod/Automatizacion_Red_2024/Scriptsv2/inventarios/dispositivos.yaml", "r") as archivo:
    datos = yaml.safe_load(archivo)

# Cargar el archivo YAML

# Acceder a los datos
for categoria, configuracion in datos.items():
    print(f"Categoría: {categoria}")
    for switch, detalles in configuracion['hosts'].items():
        print(f"Switch: {switch}")
        for clave, valor in detalles.items():
            print(f"{clave}: {valor}")
    print("Variables:")
    for clave, valor in configuracion['vars'].items():
        print(f"{clave}: {valor}")
    print()
# Obtener las IPs de los switches TPLink
