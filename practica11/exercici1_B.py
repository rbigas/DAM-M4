#Esta funcion pide al usuario que inserte 2 numeros y el programa te dira el mas grande.
def numMayorB():
    a = input("Escribe el primer numero: ")
    b = input("Escribe el segundo numero: ")
    if(a > b):
        return("El numero {a} es mayor que el numero {b}.".format(a=a,b=b))
    elif(b > a):
        return("El numero {b} es mayor que el numero {a}.".format(a=a,b=b))