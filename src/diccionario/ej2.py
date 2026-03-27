vuelo = {"aerolinea": 'Avianca', 'vuelo': 'AV123', 'origen': 'BOG', 'destino': 'MDE'}

vuelo["destino"] = "CLO"
ciudad_Llegada = vuelo['destino']
vuelo['estado'] = "en el aire"
P = vuelo.get("piloto", "Piloto no asignado")
del vuelo["vuelo"]


print(ciudad_Llegada), print(vuelo), print(P)