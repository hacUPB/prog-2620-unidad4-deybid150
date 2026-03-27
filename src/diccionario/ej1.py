# Diccionario vacío
aeronave = {}

# Diccionario con elementos
aeronave = {
    "modelo": "Boeing 787-9",
    "envergadura": 60.17,  # metros
    "longitud": 62.81,     # metros
    "mtow": 254000,        # kg
    "velocidad_max": 954   # km/h
}

del aeronave["velocidad_max"]

if "vuelo" in aeronave:
    print(f"el alcance es {aeronave["alcance"]} km")
else:
    print("la clave no existe")

velocidad  = aeronave.get("velocidad_max", "No disponible")

print(velocidad)
# Diccionario con diferentes tipos de datos como valores
vuelo = {
    "numero": "AA123",
    "origen": "KLAX",
    "destino": "KJFK",
    "distancia": 3983,
    "a_tiempo": True,
    "tripulacion": ["Capitán Smith", "F/O Johnson", "F/E Williams"]
}

vuelo["distancia"]=4000
print(vuelo["tripulacion"][0]), print(vuelo["distancia"])
# Creación con dict()
motor = dict(fabricante="GE", modelo="GE9X", empuje=470, bypass_ratio=10)


asignaturas = { 1 : "matematicas", 2 : "ciencias", 3 : "lengua"}


asignaturas[9]= "programacion"
print(asignaturas[9])


