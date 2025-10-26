# gestion_inventario.py

# 1. Crear la lista inventario con diccionarios de componentes
# Cada diccionario debe tener las claves: "id", "tipo", "ubicacion", "lecturas" (lista de 3 floats)
inventario = [
    {
        "id": "S-101",
        "tipo": "Sensor",
        "ubicacion": "Planta_Norte",
        "lecturas": [45.5, 46.1, 45.9]
    },
    {
        "id": "M-205",
        "tipo": "Motor",
        "ubicacion": "Planta_Sur",
        "lecturas": [120.2, 121.5, 120.9]
    },
    {
        "id": "V-303",
        "tipo": "Válvula",
        "ubicacion": "Planta_Norte",
        "lecturas": [9.1, 8.9, 9.0]
    }
]

"""" # 2. Calcular el promedio de lecturas para un id específico (ej. "S-101")
id_objetivo = "S-101"
promedio_lecturas = 0

for componente in inventario:
    if componente["id"] == id_objetivo:
        lecturas = componente["lecturas"]
        # Calcular el promedio: suma de lecturas / número de lecturas
        promedio_lecturas = sum(lecturas) / len(lecturas)
        break # Detener el bucle una vez que se encuentra el componente

print("--- Base de Datos de Componentes ---")
print(f"Inventario inicial (3 componentes): {len(inventario)}")
print(f"Promedio de lecturas para ID {id_objetivo}: {promedio_lecturas:.2f}")
print("-" * 42)

# Análisis de Experimentos (Sets y Tuplas)

# IDs de experimentos exitosos (tuplas de (id, fecha))
equipo_A = {("EXP-001", "2023-10-01"), ("EXP-002", "2023-10-02"), ("EXP-003", "2023-10-03")}
equipo_B = {("EXP-002", "2023-10-02"), ("EXP-004", "2023-10-04"), ("EXP-001", "2023-10-01")}

# 1. Intersección: Experimentos que ambos equipos reportaron como exitosos
ambos_exitosos = equipo_A.intersection(equipo_B)

# 2. Unión: Total de experimentos exitosos únicos
total_unicos = equipo_A.union(equipo_B)

# 3. Diferencia: Experimentos que A realizó pero B no
solo_equipo_A = equipo_A.difference(equipo_B)

print("--- Análisis de Experimentos ---")
# Imprimir todos los resultados
print(f"Experimentos exitosos en AMBOS equipos (Intersección): {ambos_exitosos}")
print(f"TOTAL de experimentos exitosos únicos (Unión): {total_unicos}")
print(f"Experimentos solo en Equipo A (Diferencia): {solo_equipo_A}")
print("-" * 30) """

# Clasificador de Inventario (Bucle for y if)
# Usamos el 'inventario' definido en el Módulo 3.

# 1. Crear las listas vacías
sensores = []
motores = []
valvulas = []

# 2. Iterar sobre la lista inventario
for componente in inventario:
    # 3. Revisar la clave "tipo" y añadir el ID a la lista que le corresponde
    tipo = componente["tipo"]
    id_componente = componente["id"]
    
    if tipo == "Sensor":
        sensores.append(id_componente)
    elif tipo == "Motor":
        motores.append(id_componente)
    elif tipo == "Válvula":
        valvulas.append(id_componente)

print("--- Clasificador de Inventario ---")
# Imprimir las tres listas
print(f"IDs de Sensores: {sensores}")
print(f"IDs de Motores: {motores}")
print(f"IDs de Válvulas: {valvulas}")
print("-" * 30)