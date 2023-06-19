"""Este codigo define una clase que representa a una universidad, permite ver
   y modificar sus atribitus mediante getters y setters y mediante un metodo muestra la informacion de sus atributos.
"""
class university:
    def __init__(self, nombre, direccion, numTelef, correo, sitioWeb, fechaFundacion):
        self.nombre = nombre
        self.direccion = direccion
        self.numTelef = numTelef
        self.correo = correo
        self.sitioWeb = sitioWeb
        self.fechaFundacion = fechaFundacion

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getDireccion(self):
        return self.direccion
    def setDireccion(self, direccion):
        self.direccion = direccion
    def getNumTelef(self):
        return self.numTelef
    def setNumTelef(self, numTelef):
        self.numTelef = numTelef
    def getCorreo(self):
        return self.correo
    def setCorreo(self, correo):
        self.correo = correo
    def getSitioWeb(self):
        return self.sitioWeb
    def setSitioWeb(self, sitioWeb):
        self.sitioWeb = sitioWeb
    def getFechaFundacion(self):
        return self.fechaFundacion
    def setFechaFundacion(self, fechaFundacion):
        self.fechaFundacion = fechaFundacion

    def info(self):
        print("Nombre Universidad: " + self.nombre)
        print("Direccion: " + self.direccion)
        print("Numero Telefono: " + self.numTelef)
        print("Correo electronico: " + self.correo)
        print("Sitio Web: " + self.sitioWeb)
        print("Fecha Fundacion: " + self.fechaFundacion +"\n")
