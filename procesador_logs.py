# procesador_logs.py

# Decodificador de Reporte
reporte_string = "ID_SENSOR:T-21,LOC:Planta_Norte,TEMP:45.8,STATUS:OK"

# 1. Dividir por coma para obtener las partes (ej: "ID_SENSOR:T-21")
partes = reporte_string.split(',')

# 2. Para cada parte, dividir por dos puntos y extraer el valor
id_sensor = partes[0].split(':')[1]         # 'T-21'
localizacion = partes[1].split(':')[1]      # 'Planta_Norte'
temperatura_str = partes[2].split(':')[1]   # '45.8'
status = partes[3].split(':')[1]            # 'OK'

# 3. Convertir la temperatura a float
temperatura_float = float(temperatura_str)

# Imprimir el reporte formateado
print("--- Decodificador de Reporte ---")
print("*** REPORTE DE SENSOR ***")
print(f"ID: {id_sensor}")
print(f"Ubicación: {localizacion}")
print(f"Temperatura: {temperatura_float} °C")
print(f"Estado: {status}")
print("-" * 30)

# Validador de Lote
codigo_lote_valido = "LOT-45A-X-B-24"   # (Válido)
codigo_lote_invalido = "LOT-44B-Z-C-23" # (Inválido)

def validar_codigo(codigo_lote):
    # 1. Debe tener exactamente 14 caracteres. (len())
    regla_1 = len(codigo_lote) == 14
    
    # 2. Debe empezar con "LOT-". (startswith())
    regla_2 = codigo_lote.startswith("LOT-")
    
    # 3. Debe terminar con "-24". (endswith())
    regla_3 = codigo_lote.endswith("-24")
    
    # 4. El 8vo carácter (índice 9) debe ser "X" o "Y".
    regla_4 = codigo_lote[8] == "X" or codigo_lote[8] == "Y"
    
    # El código es válido si TODAS las reglas son True
    es_valido = regla_1 and regla_2 and regla_3 and regla_4
    
    return es_valido

print("--- Validador de Lote ---")
# Prueba con lote Válido
if validar_codigo(codigo_lote_valido):
    print(f"Código '{codigo_lote_valido}': Válido")
else:
    print(f"Código '{codigo_lote_valido}': Inválido")

# Prueba con lote Inválido
if validar_codigo(codigo_lote_invalido):
    print(f"Código '{codigo_lote_invalido}': Válido")
else:
    print(f"Código '{codigo_lote_invalido}': Inválido")
print("-" * 33)