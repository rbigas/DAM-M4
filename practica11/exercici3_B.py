#Esta funcion te dice si has de declarar la renta.
def hacienda():
    edad = int(input("Escribe tu edad: "))
    ingresos = int(input("Escribe tus ingresos mensuales: "))

    if(edad >= 18 and ingresos >= 1200):
        return("Es necesario que hagas la declaracion de la renta.")
    else:
        return("Aun no puedes hacer la declaracion.")