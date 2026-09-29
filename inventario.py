inventario= [
	{"hostname": "Core-SW01", "ip": "10.0.0.1", "status": "up"},
	{"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"},
	{"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"},
	{"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"}
]

#imprimir todos los hostnames
for h in inventario:
	print(h["hostname"])
#imprimir todas las IPS
for i in inventario:
	print(i["ip"])
#imprimir todos los que esten en down
for e in inventario:
    if e["status"] == "down":
        print(e)