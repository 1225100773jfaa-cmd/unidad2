import requests

BASE = "https://jsonplaceholder.typicode.com"

nuevo = {"title": "Prueba de red", "body": "Contenido de ejemplo", "userId": 1}

# POST: crea un recurso. json=nuevo convierte el diccionario a JSON y pone el Content-Type
r = requests.post(f"{BASE}/posts", json=nuevo, timeout=10)
print("POST:", r.status_code, r.json())

# PUT: reemplaza el recurso completo (por eso se envía también el id)
r = requests.put(f"{BASE}/posts/1", json={**nuevo, "id": 1}, timeout=10)
print("PUT:", r.status_code, r.json())

# DELETE: elimina el recurso
r = requests.delete(f"{BASE}/posts/1", timeout=10)
print("DELETE:", r.status_code)
print("fernando alfaro")