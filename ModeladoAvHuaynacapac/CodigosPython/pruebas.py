import os

# Obtener la ruta absoluta del archivo actual
ruta_actual = os.path.abspath(__file__)
directorio_anterior = os.path.dirname(ruta_actual)
ruta_final = os.path.dirname(directorio_anterior)

