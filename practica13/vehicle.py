class vehicle:

    # Constructor de la classe
    def __init__(self, chasis, rodes, llums, motor, transmissio, escape, portes):
        self.chasis = chasis
        self.rodes = rodes
        self.llums = llums
        self.motor = motor
        self.transmissio = transmissio
        self.escape = escape
        self.portes = portes

    # Mètode que mostra per pantalla les dades de la classe
    def parts(self):
        print("Parts del vehicle:")
        print(f"Chasis: {self.chasis}")
        print(f"Rodes: {self.rodes}")
        print(f"Llums: {self.llums}")
        print(f"Motor: {self.motor}")
        print(f"Transmissió: {self.transmissio}")
        print(f"Escape: {self.escape}")
        print(f"Portes: {self.portes}\n")

    # Getters per als atributs de la classe vehicle
    def getChasis(self):
        return self.chasis

    def getRodes(self):
        return self.rodes

    def getLlums(self):
        return self.llums

    def getMotor(self):
        return self.motor

    def getTransmissio(self):
        return self.transmissio

    def getEscape(self):
        return self.escape

    def getPortes(self):
        return self.portes

    # Setters per als atributs de la classe vehicle
    def setChasis(self, chasis):
        self.chasis = chasis

    def setRodes(self, rodes):
        self.rodes = rodes

    def setLlums(self, llums):
        self.llums = llums

    def setMotor(self, motor):
        self.motor = motor

    def setTransmissio(self, transmissio):
        self.transmissio = transmissio

    def setEscape(self, escape):
        self.escape = escape

    def setPortes(self, portes):
        self.portes = portes