# Definir la llista
areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34,
             "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

# Imprimir el segon element
print("Segon element:", areas_pis[1])

# Imprimir l'ultim element
print("Ultim element:", areas_pis[-1])

# Imprimir l'area de la terrassa
terrassa = areas_pis.index("Terrassa")
print("Area de la terrassa:", areas_pis[terrassa + 1])

# Imprimir del primer element al tercer element
print("Del primer al tercer element:", areas_pis[:3])

# Imprimir del tercer element a l'ultim
print("Del tercer a l'ultim element:", areas_pis[2:])

# Imprimir el total de l'area de les dues habitacions
habitacio1 = areas_pis.index("Habitació1")
habitacio2 = areas_pis.index("Habitació2")
area_habitacions = areas_pis[habitacio1 + 1] + areas_pis[habitacio2 + 1]
print("Total area habitacions:", area_habitacions)

# Modificar l'area del lavabo i imprimir la nova llista
lavabo = areas_pis.index("Lavabo")
areas_pis[lavabo + 1] = 8.5
print("Nova llista d'arees (amb area de Lavabo modificada):", areas_pis)

# Afegir l'area de "pati interior" i 2.78 a les ultimes posicions. Imprimir la nova llista
areas_pis.extend(["Pati interior", 2.78])
print("Nova llista d'àrees (amb 'Pati interior' i 2.78 afegits):", areas_pis)

# Imprimir el total de l'area del pis
total_area_pis = sum([area for area in areas_pis[1:] if isinstance(area, (int, float))])
print("Total area del pis:", total_area_pis)

