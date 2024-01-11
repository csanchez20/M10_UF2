palabra1, palabra2 = input("Introduce dos palabras: ").split()

fusion1 = palabra2[:2] + palabra1[2:]
fusion2 = palabra1[:2] + palabra2[2:]

print(f"Palabra 1: {fusion1}")
print(f"Palabra 2: {fusion2}")
