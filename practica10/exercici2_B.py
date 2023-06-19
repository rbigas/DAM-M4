#Aquest codi defineix una tupla y mostra per consola diferents paràmetres de la mateixa
valors = (23, 423, 59, 423, 1, 0)
print("La longitut de la tupla \"valors\" és de:",len(valors))
print("El número 79 es troba a la tupla." if 79 in valors else "El número 79 NO es troba a la tupla.")
print("El valor 423 apareix",valors.count(423),"vegades a la tupla \"valors\".")