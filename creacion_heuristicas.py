import pandas as pd
import networkx as nx
import math

# Crear la tabla de entrada con pandas
data = {
    'Origen': ['Guadalupe Tlachco', 'Guadalupe Tlachco', 'B', 'B', 'C', 'C'],
    'Destino': ['B', 'C', 'Guadalupe Tlachco', 'C', 'Guadalupe Tlachco', 'B'],
    'Tiempo': [6, 15, 10, 5, 15, 5],
    'Costo': [8, 7, 5, 3, 7, 3],
    'Distancia': [6, 150, 100, 50, 150, 50]
}

df = pd.DataFrame(data)

# grafo dirigido 
G = nx.DiGraph()

# Añadir nodos y aristas al grafo
for index, row in df.iterrows():
    G.add_edge(row['Origen'], row['Destino'], tiempo=row['Tiempo'], costo=row['Costo'], distancia=row['Distancia'])

def calculo_disE(p,q):

    return heuristicas_distancia
    
# Heurísticas admisibles y consistentes
def calcular_heuristicas(grafo, objetivo):
    heuristicas = {}
    for nodo in grafo.nodes:
        if nodo == objetivo:
            heuristicas[nodo] = 0
        else:
            heuristicas[nodo] = float('inf')
            for neighbor in grafo.neighbors(nodo):
                heuristicas[nodo] = min(heuristicas[nodo], grafo[nodo][neighbor]['distancia'])
    return heuristicas

# Calcular heurísticas para cada criterio
objetivo = 'C'
heuristicas_tiempo = calcular_heuristicas(G, objetivo)
heuristicas_costo = calcular_heuristicas(G, objetivo)
heuristicas_distancia = calcular_heuristicas(G, objetivo)

print("Heurísticas basadas en el tiempo:", heuristicas_tiempo)
print("Heurísticas basadas en el costo:", heuristicas_costo)
print("Heurísticas basadas en la distancia:", heuristicas_distancia)
