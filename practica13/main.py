#Imports de classes per part del Roc(A)
from animal import animal
from vehicle import vehicle
from school import school

#Imports de classes per part del Jhamel(B)
from book import book
from user import user
from university import university

#Instàncies i crides per part del Roc(A)
marmota = animal("Marmota", 4.5, "Sciuridae", "Marmota marmota", 15, "Baix", "Estable")
marmota.salutacio()
marmota.setLongevitat(23)
marmota.salutacio()

ornitorinc = animal("Ornitorinc", 1.5, "Ornithorhynchidae", "Ornithorhynchus anatinus", 17, "Amenaçat", "Desconeguda")
ornitorinc.salutacio()
ornitorinc.setPes(2.1)
ornitorinc.salutacio()

cotxe = vehicle("Alumini", 4, 4, "4 cilindres", "Automàtica", "Doble sortida", 5)
cotxe.parts()
cotxe.setMotor("8 cilindres")
cotxe.parts()

moto = vehicle("Ferro", 2, 2, "2 cilindres", "Manual", "Sortida simple", 0)
moto.parts()
moto.setEscape("Sortida doble")
moto.parts()

jaumeBalmes = school(15000, 100, 50000, "Sí", 'Barcelona', ['Enginyeria', 'Dret', 'Medicina'])
jaumeBalmes.info()
jaumeBalmes.setnAules(45)
jaumeBalmes.info()

joanCoromines = school(8000, 50, 25000, "No", 'Madrid', ['Economia', 'Biologia', 'Periodisme'])
joanCoromines.info()
joanCoromines.setnAules(45)
joanCoromines.info()

#Instàncies Jhamel(B)
l1 = book("El Juego de Ender", "Orson Scott Card", "Ediciones B", "1985", "Español", "10.99€")
l2 = book("The Great Gatsby", "F.Scott Fitzgerald", "Scribner", "1925", "Ingles", "9.99€")
book.info(l1)
l1.setPrecio("11.99€")
book.info(l1)
book.info(l2)
l2.setPrecio("10.99€")
book.info(l2)
user1 = user("Sara", "Jones", "27", "sarah.jones@gmail.com", "Femenino", "Estados Unidos")
user2 = user("Juan", "Perez", "32", "juan.perez@gmail.com", "Masculino", "Mexico")
user.salutacio(user1)
user1.setCorreo("sarah.jones@hotmail.com")
user.salutacio(user1)
user.salutacio(user2)
user2.setEdad("30")
user.salutacio(user2)
uni1 = university("Universidad Nacional de Ciencias Aplicadas", "Av. Universitaria 1801, Lima, Perú", "+51 1 748-0888", "informes@unca.edu", "https://www.unca.edu.pe/", "15/5/1950")
uni2 = university("Universidad de las Américas", "Av. de los Cerezos s/n, San Andrés Cholula, Puebla, México", "+52 222 229 2000", "info@udla.mx", "https://www.udla.mx/", "1/9/1960")
university.info(uni1)
uni1.setNumTelef("+51 1 700-0909")
university.info(uni1)
university.info(uni2)
uni2.setCorreo("informacion@udla.mx")
university.info(uni2)