import numpy as np

# Datos iniciales
demanda_pasajeros = np.array([50, 60, 30, 60, 35])  # demanda por hora de 6 a 10
rutas = ['Tlaxcala-Xochimilco','Tlaxcala Apatlahco']
tiempos_viaje = np.array([47,45])  # viaje en minutos
capacidad_vehiculo = 12  # capacidad de una combi común

# determinar cada cuanto debe salir una combi para cubrir la demanda 
frecuencias = np.ceil(demanda_pasajeros / capacidad_vehiculo).astype(int)

# horarios 
horarios = []
for i, freq in enumerate(frecuencias):
    num_intervalos = len(demanda_pasajeros) // freq
    horario = np.arange(0, 60 * num_intervalos, 60 / freq)
    horarios.append(horario)

# Asignación de Vehículos
asignaciones = []
for ruta in rutas:
    asignacion = []
    for horario in horarios:
        asignacion.append({'ruta': ruta, 'horarios': horario})
    asignaciones.append(asignacion)

# Sincronización de Horarios (exclusion >59)
for i, asignacion in enumerate(asignaciones):
    for j, asignacion_j in enumerate(asignacion):
        # Ajustar los horarios para la sincronización
        sincronizacion = np.round(asignacion_j['horarios'] / 5) * 5
        # Excluir horarios mayores a 59 minutos
        sincronizacion = sincronizacion[sincronizacion <= 59]
        asignaciones[i][j]['horarios'] = sincronizacion

# Filtrar asignaciones vacías 
asignaciones = [asignacion for asignacion in asignaciones if any(len(horario) > 0 for horario in asignacion)]

# Resultados
for asignacion in asignaciones:
    for ruta in asignacion:
        print(f"Ruta: {ruta['ruta']}, Horarios: {ruta['horarios']}")
