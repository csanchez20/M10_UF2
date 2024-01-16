frase = input("Introduce una frase: ")

no_espacios = frase.replace(" ", "")

palabras = tuple(no_espacios.split())

print("Contenido de la frase:", palabras)
