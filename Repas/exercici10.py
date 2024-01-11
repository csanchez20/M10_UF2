import random

numeroSecreto = random.randint(1, 100)
intentos = 0

while True:
    intentoUsuario = int(input("Introduce un número entre 1 y 100: "))
    intentos += 1

    if intentoUsuario < numeroSecreto:
        print("Més gran.")
    elif intentoUsuario > numeroSecreto:
        print("Més petit.")
    else:
        print(f"Encertado! Has adivinado el número en {intentos} intentos.")
        break
