palabras = input("Introduce 3 palabras: ").split()

for palabra in palabras:
    print(f"Palabra: {palabra}")
    print(f"Numero de carácteres: {len(palabra)}")
    print(f"Primer carácter: {palabra[0]}")
    print(f"Ultimo carácter: {palabra[-1]}")
