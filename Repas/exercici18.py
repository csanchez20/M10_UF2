palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

tupla = (palabra1, palabra2)

frecuencia = {}

for palabra in tupla:
    for letra in palabra:
        if letra.isalpha():
            frecuencia[letra] = frecuencia.get(letra, 0) + 1

print("Frecuencia de las letras:")
for letra, frec in frecuencia.items():
    print(f"{letra}: {frec} veces")
