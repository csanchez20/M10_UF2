numero = int(input("Introduce un número del 1 al 10: "))

print(f"Taula de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(resultado, end=" ")
