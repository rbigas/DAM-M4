#Aquest codi llegeix dos números per consola i defineix quin és major o si els dos són iguals.

def numMajorA():
    num1 = input("Indtroduiex un número: ")
    num2 = input("Introdueix un altre número: ")
    if (num1 > num2):
        return("El número {num1} és més gran que el número {num2}.".format(num1=num1, num2=num2))
    elif (num1 < num2):
        return("El número {num2} és més gran que el número {num1}.".format(num1=num1, num2=num2))
    else:
        return("El número {num1} és igual que el número {num2}.".format(num1=num1, num2=num2))