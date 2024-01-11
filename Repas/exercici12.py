meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    mes = int(input("Introduce un número entre 1 y 12 (o 0 para finalizar): "))

    if mes == 0:
        print("Programa finalizado.")
        break

    if 1 <= mes <= 12:
        mesSeleccionado = meses[mes - 1]
        print(f"El mes correspondiente al número {mes} es {mesSeleccionado}.")
    else:
        print("Número no válido. Por favor, introduce un número entre 1 y 12.")
