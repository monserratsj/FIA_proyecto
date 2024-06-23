import math

# Función para calcular la distancia euclidiana entre dos puntos
def distancia_euclidiana(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Heurística del vecino más cercano
def vecino_mas_cercano(puntos, inicio):
    punto_actual = inicio
    ruta = [punto_actual]
    puntos_restantes = set(puntos)
    puntos_restantes.remove(punto_actual)
    
    while puntos_restantes:
        punto_siguiente = min(puntos_restantes, key=lambda punto: distancia_euclidiana(punto_actual, punto))
        ruta.append(punto_siguiente)
        puntos_restantes.remove(punto_siguiente)
        punto_actual = punto_siguiente
    
    return ruta

# Heurística de mínimo costo (Greedy)
def minimo_costo(puntos, inicio):
    punto_actual = inicio
    ruta = [punto_actual]
    puntos_restantes = set(puntos)
    puntos_restantes.remove(punto_actual)
    
    while puntos_restantes:
        punto_siguiente = min(puntos_restantes, key=lambda punto: distancia_euclidiana(punto_actual, punto))
        ruta.append(punto_siguiente)
        puntos_restantes.remove(punto_siguiente)
        punto_actual = punto_siguiente
    
    # Volver al punto inicial al final de la ruta
    ruta.append(inicio)
    
    return ruta

# Ejemplo de uso
puntos = [(1, 2), (3, 5), (6, 8), (9, 4), (5, 1)]
inicio = puntos[0]

# Usando la heurística del vecino más cercano
ruta_vecino_mas_cercano = vecino_mas_cercano(puntos, inicio)
print("Ruta usando heurística del vecino más cercano:", ruta_vecino_mas_cercano)

# Usando la heurística de mínimo costo (Greedy)
ruta_minimo_costo = minimo_costo(puntos, inicio)
print("Ruta usando heurística de mínimo costo (Greedy):", ruta_minimo_costo)
