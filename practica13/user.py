"""Este codigo define una clase que representa a usaurios, permite ver
   y modificar sus atribitus mediante getters y setters y muestra la informacion de sus atributos.
"""


class user:
    def __init__(self, nUsuario, aUsuario, edad, correo, genero, pais):
        self.nUsuario = nUsuario
        self.aUsuario = aUsuario
        self.edad = edad
        self.correo = correo
        self.genero = genero
        self.pais = pais

    def getnUsuario(self):
        return self.nUsuario

    def setnUsuario(self, nUsuario):
        self.nUsuario = nUsuario

    def getaUsuario(self):
        return self.aUsuario

    def setaUsuario(self, aUsuario):
        self.aUsuario = aUsuario

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getCorreo(self):
        return self.correo

    def setCorreo(self, correo):
        self.correo = correo

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getPais(self):
        return self.pais

    def setPais(self, pais):
        self.pais = pais

    def salutacio(self):
        print("Nombre de usuario: " + self.nUsuario)
        print("Apellido usuario: " + self.aUsuario)
        print("Edad: " + self.edad)
        print("Correo electronico: " + self.correo)
        print("Genero: " + self.genero)
        print("Pais de residencia: " + self.pais + "\n")
