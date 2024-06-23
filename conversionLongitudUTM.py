#Este archivo nos ayuda a corroborar que las coordenadas UTM sean las correctas
'''pyproj es una biblioteca de Python que se utiliza para realizar transformaciones de
coordenadas entre diferentes sistemas de referencia geoespacial. La función Transformer
de pyproj es una herramienta clave dentro de esta biblioteca que permite la conversión de
coordenadas de un sistema de referencia a otro.from pyproj import Transformer'''

# Lista de coordenadas (latitud, longitud)
coordinates = [
    (19.3130, -98.2417),
    (19.3181, -98.2367),
    (19.3351, -98.2301),
    (19.3366, -98.2208),
    (19.3458, -98.2526),
    (19.3118, -98.2569),
    (19.3455, -98.2604),
    (19.3132, -98.1989),
    (19.3382, -98.2230),
    (19.3496, -98.2608),
    (19.3428, -98.2573),
    (19.3365, -98.2647),
    (19.3543, -98.2439)
]

# Crear un objeto Transformer para la transformación de coordenadas
transformer = Transformer.from_crs("epsg:4326", "epsg:32614")  # WGS84 a UTM Zona 14N

# Convertir coordenadas usando la nueva API de Transformer
utm_coordinates = [transformer.transform(lat, lon) for lat, lon in coordinates]

# Imprimir resultados
for coord, utm in zip(coordinates, utm_coordinates):
    lat, lon = coord
    utm_e, utm_n = utm
    print(f"Latitud: {lat}, Longitud: {lon} -> UTM Este: {utm_e:.2f}, UTM Norte: {utm_n:.2f}")
