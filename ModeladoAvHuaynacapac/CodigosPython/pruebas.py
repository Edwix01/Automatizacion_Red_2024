import matplotlib.pyplot as plt

# Configurar matplotlib para usar una fuente similar a LaTeX
plt.rcParams['font.family'] = 'STIXGeneral'  # STIX general es similar a la fuente de LaTeX

# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [10, 20, 25, 30, 40]

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(categorias, valores, color='green')

# Añadir título y etiquetas
plt.title('Gráfico de Barras', fontsize=16)
plt.xlabel('Categorías', fontsize=14)
plt.ylabel('Valores', fontsize=14)

# Añadir etiquetas a cada barra
for i, v in enumerate(valores):
    plt.text(i, v + 0.5, str(v), ha='center', fontsize=12)

# Mostrar la gráfica
plt.show()
