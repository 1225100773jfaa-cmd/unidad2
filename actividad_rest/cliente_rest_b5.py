import requests

def obtener_clima(latitud, longitud):
    """Consulta Open-Meteo y regresa un diccionario con temperatura y viento."""
    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,wind_speed_10m",
    }
    r = requests.get(url, params=parametros, timeout=10)
    r.raise_for_status()
    return r.json()["current"]

# Tres ciudades de prueba: (nombre, latitud, longitud)
ciudades = [
    ("Querétaro", 20.59, -100.39),
    ("Ciudad de México", 19.43, -99.13),
    ("Guadalajara", 20.67, -103.35),
]

# Tabla impresa en consola
print(f"{'Ciudad':<20}{'Temp (°C)':>12}{'Viento (km/h)':>16}")
print("-" * 48)
for nombre, lat, lon in ciudades:
    try:
        clima = obtener_clima(lat, lon)
        print(f"{nombre:<20}{clima['temperature_2m']:>12}{clima['wind_speed_10m']:>16}")
    except requests.exceptions.RequestException as e:
        print(f"{nombre:<20} Error: {e}")