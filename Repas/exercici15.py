numeros = []

while True:
    num = input("Introduce un número (o 0 para acabar): ")

    if num == "0":
        break 

    try:
        numeros.append(int(num))
    except ValueError:
        print("Por favor, introduce solo numeros")

seleccion = input("¿Ordenarlo de forma (ascendente) o (descendiente)? ").lower()

if seleccion == "ascendente":
    numeros_ordenados = tuple(sorted(numeros))
elif seleccion == "descendiente":
    numeros_ordenados = tuple(sorted(numeros, reverse=True))

print("Tupla ordenada:", numeros_ordenados)
