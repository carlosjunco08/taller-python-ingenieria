# Módulo 5: Funciones y Funciones Lambda

from gestion_inventario import inventario

# Función de Análisis de Componente (def)

print("Función de Análisis de Componente (def)")

def analizar_componente(componente_dict):
    # Calcula el promedio, máximo y mínimo de las lecturas de un componente.#
    # 1. Obtener la lista de lecturas
    lecturas = componente_dict.get("lecturas", [])
    
    if not lecturas:
        return {"promedio": 0.0, "max": 0.0, "min": 0.0}
    
    # 2. Calcular promedio, maximo y minimo
    promedio = sum(lecturas) / len(lecturas)
    maximo = max(lecturas)
    minimo = min(lecturas)
    
    # 3. Retornar un nuevo diccionario con los resultados
    return {"promedio": round(promedio, 2), "max": maximo, "min": minimo}

# Prueba de la función con el componente
componente_prueba = inventario[1]
resultados_analisis = analizar_componente(componente_prueba)

print(f"Análisis para ID {componente_prueba['id']} ({componente_prueba['tipo']}):")
print(f"  Resultados: {resultados_analisis}")
print("-" * 40)

print("Filtrado y Mapeo Avanzado (lambda)")

# 1. Filtrado: Usar filter() y lambda para crear una lista sensores_criticos
# Criterio: "tipo" sea "Sensor" Y "ubicacion" sea "Planta_Norte"
sensores_criticos_obj = filter(
    lambda comp: comp["tipo"] == "Sensor" and comp["ubicacion"] == "Planta_Norte", 
    inventario
)
# Convertir a lista
sensores_criticos = list(sensores_criticos_obj)


# 2. Mapeo: Usar map() y lambda para obtener solo el 'id' de esos sensores
ids_sensores_obj = map(
    lambda comp: comp["id"],
    sensores_criticos
)
# Convertir a lista
ids_sensores = list(ids_sensores_obj)

# 3. Imprimir ids_sensores
print(f"Componentes filtrados (Sensores en Planta_Norte): {ids_sensores}")
print("-" * 40)