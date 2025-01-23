import matplotlib.pyplot as plt
import numpy as np

# Datos de MongoDB y Redis
mongodb_results = {
    "Create": [0.12, 0.14, 0.07, 0.07, 0.07],
    "Read": [0.012030, 0.017260, 0.001872, 0.007053, 0.017996],
    "Update": [0.08, 0.07, 0.05, 0.05, 0.05],
    "Delete": [0.04, 0.04, 0.05, 0.04, 0.04],
}

redis_results = {
    "Create": [0.06, 0.05, 0.05, 0.05, 0.06],
    "Read": [0.001545, 0.000163, 0.000222, 0.000234, 0.000227],
    "Update": [0.04, 0.05, 0.05, 0.05, 0.05],
    "Delete": [0.03, 0.03, 0.04, 0.04, 0.04],
}

# Operaciones
operations = ["Create", "Read", "Update", "Delete"]

# Calcular promedios
mongodb_avg = [np.mean(mongodb_results[op]) for op in operations]
redis_avg = [np.mean(redis_results[op]) for op in operations]

# Crear un gráfico de barras comparativo
x = np.arange(len(operations))  # Posiciones para las barras
width = 0.35  # Ancho de las barras

fig, ax = plt.subplots(figsize=(10, 6))

# Barras para MongoDB y Redis
bars_mongodb = ax.bar(x - width / 2, mongodb_avg, width, label='MongoDB', color='blue', alpha=0.7)
bars_redis = ax.bar(x + width / 2, redis_avg, width, label='Redis', color='green', alpha=0.7)

# Añadir etiquetas, título y leyenda
ax.set_xlabel('Operaciones', fontsize=12)
ax.set_ylabel('Tiempo Promedio (s)', fontsize=12)
ax.set_title('Comparación de Rendimiento entre MongoDB y Redis', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(operations)
ax.legend()

# Añadir etiquetas de valor en las barras
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.4f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

add_labels(bars_mongodb)
add_labels(bars_redis)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
