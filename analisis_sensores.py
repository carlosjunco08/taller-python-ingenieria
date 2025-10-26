# analisis_sensores.py

# Conversor de Unidades
temperatura_celsius = 35.5

# Cálculo a Fahrenheit: F = C * (9/5) + 32
temperatura_fahrenheit = temperatura_celsius * (9/5) + 32  # float

# Cálculo a Kelvin: K = C + 273.15
temperatura_kelvin = temperatura_celsius + 273.15      # float

print("--- Conversor de Unidades ---")
print(f"Temperatura en Celsius: {temperatura_celsius}°C")
print(f"Equivalente en Fahrenheit: {temperatura_fahrenheit}°F")
print(f"Equivalente en Kelvin: {temperatura_kelvin}K")
print("-" * 30)

# Monitor de Seguridad de Caldera
temp_caldera = 95.2        # float
presion_caldera = 101.5    # float
operador_presente = True   # bool

# Alarma debe ser True si:
# (temp_caldera > 100.0 Y presion_caldera > 103.0) O
# (temp_caldera > 105.0 Y operador_presente es False)
alarma_critica = (
    (temp_caldera > 100.0 and presion_caldera > 103.0) or
    (temp_caldera > 105.0 and operador_presente == False)
)

print("--- Monitor de Seguridad de Caldera ---")
print(f"Temperatura: {temp_caldera}°C, Presión: {presion_caldera} kPa, Operador Presente: {operador_presente}")
print(f"Estado de alarma_critica: {alarma_critica}")  # Imprime True o False
print("-" * 30)