Fundamentos de Inteligencia Artificial 4IV1


Juárez Franco Ximena Yahel
Sánchez Juárez Monserrat 
Torrez Oropeza Samuel Alejandro
Ugalde Díaz Mariano

Este proyecto tiene cómo proposito analizar las rutas de transporte público de  la zona centro sur del estado de Tlaxcala, para analizar si las rutas planteadas son las más eficientes o si existe alguna ruta planteada que sea más corta. 

Para lograr lo anterior se está utilizando un algoritmo A*

Para poder ejecutar el programa se debe tener en cuenta que los archivos:

-heuristics.txt 
-kilometraje.txt
-CoordenadasUTM.xlsx 

deben estar en la misma carpeta de ejecución. En caso de no tenerlas, se debe corregir las rutas en heuristicas.py y AlgoritmoA.py con la ruta de ambos archivos.

heuristicas.py obtendrá las heuristicas utilizando la distancia euclidiana, también dibujará el grafo completo.
AlgoritmoA.py usa las heuristicas obtenidas y remarca las aristas de la ruta más corta. 
kilometraje.txt es el archivo en el cual se determina la distancia real (los kilometros ) entre un nodo y otro además nos permite validar que aristas deben existir en la construcción del grafo. 
Puesto que en el grafo completo construido con heuristicas todos los nodos están conectados.
El grafo que construye AlgoritmoA con la validación de entre heuristics y kilometraje nos permite saber que aristas son válidas. Si es que existe alguna carretera o camino que conecte un nodo (lugar) con otro, en caso de que no esté una distancia en kilometraje, esa arista no séra contemplada en el grafo que se usará en A*

El archivo conversitonLongitudUTM nos permite verificar que se transformen la longitud y la latitud y den las coordenadas UTM.
