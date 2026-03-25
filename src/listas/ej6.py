from random import randint
meses = ["Enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
lista = []
for i in range(13):
    ventas = randint(0,100)
    lista.append(ventas)
print(lista)
M = max(lista)
veces = lista.count(M)
mes = lista.index(M)
print(f" {M} se encontró un total de {veces} \n Se vendieron mas autos en {meses[mes]}\n Se vendieron {M} autos")

if veces > 1:
    lista_meses = []
    for i in range(len(lista)):
        if lista[i] == M:
            lista_meses.append(i)
    print("ventas mayores en: ")
    for mes in lista_meses:
        print(f"{meses[mes]}")
else:
    pass