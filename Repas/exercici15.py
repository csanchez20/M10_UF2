numeros = []

while True:
    num = input("Introdueix un número (o 0 per acabar): ")

    if num == "0":
        break 

    try:
        numeros.append(int(num))
    except ValueError:
        print("Si us plau, introdueix només números.")

seleccion = input("¿Vols ordenar de forma (ascendent) o (descendent)? ").lower()

if seleccion == "ascendent":
    numeros_ordenados = tuple(sorted(numeros))
elif seleccion == "descendent":
    numeros_ordenados = tuple(sorted(numeros, reverse=True))
else:
    print("Selecció no vàlida. S'ordenarà de forma predeterminada (ascendent).")
    numeros_ordenados = tuple(sorted(numeros))

print("Tupla ordenada:", numeros_ordenados)
