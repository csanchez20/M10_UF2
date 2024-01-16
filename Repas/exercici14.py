string = input("Introduce 10 números:  ")
numeros = tuple(map(int, string.split()))

seleccion = input("¿Quieres ordenar de forma (ascendente) o (descendente)? ").lower()

if seleccion == "ascendente":
    numeros_ordenados = tuple(sorted(numeros))
elif seleccion == "descendente":
    numeros_ordenados = tuple(sorted(numeros, reverse=True))

print("Tupla ordenada:", numeros_ordenados)
