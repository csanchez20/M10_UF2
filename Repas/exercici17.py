frase = input("Introduce una frase: ")

no_espacios = frase.replace(" ", "")

caracteres = list(set(no_espacios))

no_duplicados = ''.join(caracteres)

palabras = tuple(frase.split()), no_duplicados

print("Contenido de la frase:", palabras)
print("Frase sin caracteres duplicados:", palabras[1])
