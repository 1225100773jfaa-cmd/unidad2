import requests 
 
BASE = "https://jsonplaceholder.typicode.com" 

respuesta = requests.get(f"{BASE}/posts", params={"userId": 3}, timeout=10)
publicaciones = respuesta.json() # lista de diccionarios
print("Total:", len(publicaciones))
for p in publicaciones:
 print(f"{p['id']:>3} | {p['title']}")
print("fernando alfaro")
