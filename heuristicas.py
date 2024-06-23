import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt
import os

# Definición de la clase Lugar para representar cada nodo
class Lugar:
    def __init__(self, municipio, nombre, este, norte):
        self.municipio = municipio
        self.nombre = nombre
        self.este = este
        self.norte = norte

# Ruta del archivo de Excel
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'CoordenadasUTM.xlsx')

# Leer el archivo de Excel
df = pd.read_excel(file_path, sheet_name='Hoja1', engine='openpyxl')

print(df.columns)
print(df.head())

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(lugar1, lugar2):
    return sqrt((lugar1.este - lugar2.este)**2 + (lugar1.norte - lugar2.norte)**2)

# Crear un grafo vacío
G = nx.Graph()

# Agregar nodos al grafo
lugares = {}
for index, row in df.iterrows():
    # Verificar si las coordenadas son válidas
    if pd.notnull(row['Este']) and pd.notnull(row['Norte']):
        lugar = Lugar(row['Municipio'], row['NombreLugar'], row['Este'], row['Norte'])
        lugares[row['NombreLugar']] = lugar
        G.add_node(lugar.nombre)

# Agregar aristas ponderadas basadas en la distancia euclidiana
for u in lugares:
    for v in lugares:
        if u != v and not G.has_edge(u, v):
            distancia = euclidean_distance(lugares[u], lugares[v])
            G.add_edge(u, v, weight=distancia)

# Dibujar el grafo
pos = {lugar.nombre: (lugar.este, lugar.norte) for lugar in lugares.values() if pd.notnull(lugar.este) and pd.notnull(lugar.norte)}
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_color='black')

# Agregar etiquetas de peso en las aristas
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=8)

# Ajustar el diseño para evitar problemas con tight_layout
plt.title('Grafo de Lugares con Distancia Euclidiana como Heurística')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.show()
