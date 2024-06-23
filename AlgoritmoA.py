import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Definición de la clase Nodo para representar nodos en el grafo
class Nodo:
    def __init__(self, nombre, g=0, h=0):
        self.nombre = nombre  # Nombre del nodo
        self.g = g  # Costo desde el inicio hasta este nodo
        self.h = h  # Costo heurístico desde este nodo hasta la meta
        self.f = g + h  # Costo total f = g + h
        self.padre = None  # Nodo padre en el camino

    # Método para comparar nodos basado en f
    def __lt__(self, otro):
        return self.f < otro.f

# Función para leer el grafo desde un archivo de texto
def leer_grafo(archivo_heuristics, archivo_kilometraje):
    grafo = {}
    conexiones = {}

    # Leer el archivo de kilometraje y almacenar las conexiones válidas
    with open(archivo_kilometraje, 'r') as file:
        for line in file:
            datos = line.strip().split(':')
            conexion = datos[0].strip()
            distancia = float(datos[1].strip())
            nodo1, nodo2 = conexion.split(' - ')
            conexiones[(nodo1, nodo2)] = distancia
            conexiones[(nodo2, nodo1)] = distancia

    # Leer el archivo de heurísticas y construir el grafo solo con conexiones válidas
    with open(archivo_heuristics, 'r') as file:
        for line in file:
            datos = line.strip().split(':')
            conexion = datos[0].strip()
            nodo1, nodo2 = conexion.split(' - ')
            if (nodo1, nodo2) in conexiones:
                costo = conexiones[(nodo1, nodo2)]
                if nodo1 not in grafo:
                    grafo[nodo1] = []
                if nodo2 not in grafo:
                    grafo[nodo2] = []
                grafo[nodo1].append((nodo2, costo))
                grafo[nodo2].append((nodo1, costo))

    return grafo

# Algoritmo A* modificado para usar heurísticas y grafo desde archivo
def a_estrella(inicio, meta, grafo, heuristics_file, archivo_kilometraje):
    lista_abierta = []  # Lista de nodos abiertos
    lista_cerrada = set()  # Conjunto de nombres de nodos cerrados

    # Leer heurísticas desde el archivo
    heuristics = {}
    with open(heuristics_file, 'r') as file:
        for line in file:
            datos = line.strip().split(':')
            conexion = datos[0].strip()
            heuristica_valor = float(datos[1].strip())
            nodo1, nodo2 = conexion.split(' - ')
            heuristics[nodo1] = heuristica_valor
            heuristics[nodo2] = heuristica_valor

    # Leer distancias desde el archivo de kilometraje
    distancias = {}
    with open(archivo_kilometraje, 'r') as file:
        for line in file:
            datos = line.strip().split(':')
            conexion = datos[0].strip()
            distancia = float(datos[1].strip())
            nodo1, nodo2 = conexion.split(' - ')
            distancias[(nodo1, nodo2)] = distancia
            distancias[(nodo2, nodo1)] = distancia

    nodo_inicio = Nodo(inicio)  # Nodo inicial
    nodo_meta = Nodo(meta)  # Nodo meta

    heapq.heappush(lista_abierta, nodo_inicio)  # Agregar nodo inicial a la lista de abiertos

    while lista_abierta:
        nodo_actual = heapq.heappop(lista_abierta)  # Obtener nodo con menor f de la lista de abiertos
        lista_cerrada.add(nodo_actual.nombre)  # Agregar el nombre del nodo actual a los cerrados

        if nodo_actual.nombre == nodo_meta.nombre:
            # Reconstruir el camino si se alcanza el nodo meta
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual.nombre)
                nodo_actual = nodo_actual.padre
            camino.reverse()  # Devolver el camino invertido (inicio a meta)
            return camino

        vecinos = grafo.get(nodo_actual.nombre, [])  # Obtener vecinos del nodo actual desde el grafo
        for vecino_nombre, _ in vecinos:
            if vecino_nombre in lista_cerrada:
                continue  # Saltar a la siguiente iteración si el vecino está en los nodos cerrados

            # Crear nodo vecino
            nodo_vecino = Nodo(vecino_nombre)
            g_tentativa = nodo_actual.g + distancias.get((nodo_actual.nombre, vecino_nombre), float('inf'))  # Calcular el nuevo g tentativo para el vecino

            # Obtener heurística desde el diccionario
            heuristica_valor = heuristics.get(vecino_nombre, 0)  # Si no hay heurística, usar 0

            # Actualizar datos del nodo vecino
            nodo_vecino.g = g_tentativa
            nodo_vecino.h = heuristica_valor
            nodo_vecino.f = nodo_vecino.g + nodo_vecino.h
            nodo_vecino.padre = nodo_actual

            # Agregar nodo vecino a la lista de abiertos si no está ya en la lista con menor f
            if all(nodo_vecino.nombre != nodo.nombre or nodo_vecino.f < nodo.f for nodo in lista_abierta):
                heapq.heappush(lista_abierta, nodo_vecino)

    return None  # Devolver None si no se encuentra un camino

# Función para dibujar el grafo
def dibujar_grafo(grafo, camino=None):
    G = nx.Graph()

    # Agregar nodos al grafo
    for nodo, vecinos in grafo.items():
        G.add_node(nodo)
        for vecino, peso in vecinos:
            G.add_edge(nodo, vecino, weight=peso)

    # Definir posiciones de los nodos para un mejor dibujo
    pos = nx.spring_layout(G)

    # Dibujar nodos y aristas
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.0, alpha=0.5, edge_color='gray')

    # Etiquetas de los nodos
    labels = {nodo: nodo for nodo in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=8)

    # Destacar el camino más corto si se proporciona
    if camino:
        path_edges = [(camino[i], camino[i+1]) for i in range(len(camino)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.0)

    # Mostrar el grafo
    plt.title("Grafo del camino más corto")
    plt.axis('off')
    plt.show()

# Ejemplo de uso
archivo_heuristicas = 'heuristics.txt'
archivo_kilometraje = 'kilometraje.txt'
inicio = 'Centro Santa Catarina Apatlahco'
meta = 'Mercado municipal Emilio Sanchez Piedras'

# Leer grafo desde archivo con conexiones adicionales
grafo = leer_grafo(archivo_heuristicas, archivo_kilometraje)

# Ejecutar algoritmo A* con grafo y heurísticas desde archivos
camino = a_estrella(inicio, meta, grafo, archivo_heuristicas, archivo_kilometraje)
print("Ruta más corta:", camino)

# Dibujar el grafo
if camino:
    dibujar_grafo(grafo, camino)
else:
    print("No se encontró un camino.")
