#Definim la llista d'àreas
areas = ["cuina", 7.8, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]

#Imprimim el segon element de la llista
print(areas[1])

#Imprimim l’últim element de la llista
print(areas[-1])

#Imprimim l’àrea de la terrassa
print(areas[5])

#Imprimim des del primer element fins al tercer element
print(areas[0:3])

#Imprimim des del tercer element fins a l’últim
print(areas[2:])

#Imprimim la suma de l'àrea de les dues habitacions
print(areas[9]+areas[11])

#Modifiquem l’àrea del lavabo i imprimim la llista modificada
areas[7] = 14.34
print(areas)

#Afegim l'element “pati interior” i el valor 2.78 a les últimes posicions. Imprimim la llista modificada.
areas.append("pati interior")
areas.append(2.78)
print(areas)