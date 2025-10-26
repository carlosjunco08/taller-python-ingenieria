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