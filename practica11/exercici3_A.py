import random

# Aquest codi genera un número aleatori i demana a l'usuari que l'endevini,
# mostrant el rang en el que es troba el número cada cop que l'usuari fa un
# intent. S'adapta a les respostes de l'usuari per a determinar el rang.

def adivinaNumAmbRang():
    numResult = random.randrange(0,100)
    numInput = int(input("Introdueix un número del 0 al 100: "))
    min= 0
    max= 100
    if numInput == numResult:
        return("Molt bé! Has endevinat el número!")
    else:
        while numInput != numResult:
            if numInput > numResult:
                print("El número és més petit")
                max = numInput
                numInput = int(input("Introdueix un número del {min} al {max}: ".format(max=max, min=min)))
            else:
                min = numInput
                print("El número és més gran")
                numInput = int(input("Introdueix un número del {min} al {max}: ".format(max=max, min=min)))
        return("Molt bé! Has endevinat el número!")
