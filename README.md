Fundamentos de Inteligencia Artificial 4IV1


Juárez Franco Ximena Yahel
Sánchez Juárez Monserrat 
Torrez Oropeza Samuel Alejandro
Ugalde Díaz Mariano

Este proyecto tiene cómo proposito analizar las rutas de transporte público de  la zona centro sur del estado de Tlaxcala, para analizar si las rutas planteadas son las más eficientes o si existe alguna ruta planteada que sea más corta. 

Para lograr lo anterior se está utilizando un algoritmo mejorado de A* propuesto por Cao Wen en 2009.

Para poder ejecutar el programa se debe tener en cuenta que los archivos:

-heuristics.txt 
-CoordenadasUTM.xlsx 

deben estar en la misma carpeta de ejecución. En caso de no tenerlas, se debe corregir las rutas en heuristicas.py y AlgoritmoA.py con la ruta de ambos archivos.

heuristicas.py obtendrá las heuristicas utilizando la distancia euclidiana, también dibujará el grafo completo.
AlgoritmoA.py usa las heuristicas obtenidas y remarca las aristas de la ruta más corta.


