import requests

BASE = "https://jsonplaceholder.typicode.com"

try:
    r = requests.get(f"{BASE}/posts/9999", timeout=10)
    r.raise_for_status()  # lanza excepción si el código es 4xx o 5xx
    print(r.json())
except requests.exceptions.HTTPError as e:
    print("Error HTTP:", e)           # el servidor respondió con error (404)
except requests.exceptions.RequestException as e:
    print("Error de conexión:", e)    # sin internet, timeout, DNS, etc.
print("fernando alfaro")