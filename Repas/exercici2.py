valor = float(input("Introduce un valor en €: "))

porcentanje_iva = float(input("Introduce un porcentaje (4%, 10% o 21%): "))

if porcentanje_iva not in [4, 10, 21]:
    print("Error: Introduce un valor valido")
else:
    iva = valor * (porcentanje_iva / 100)

    valor_final = valor + iva

    print(f"Valor usuario: {valor} €")
    print(f"IVA aplicado: {porcentanje_iva}%")
    print(f"Valor final: {valor_final} €")