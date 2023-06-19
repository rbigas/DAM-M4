class school:

    # Constructor de la classe
    def __init__(self, nAlumnes, nAules, superficie, gimnas, municipi, graus):
        self.nAlumnes = nAlumnes
        self.nAules = nAules
        self.superficie = superficie
        self.gimnas = gimnas
        self.municipi = municipi
        self.graus = graus

    # Mètode que ens retorna els atributs d'una instància en format de diccionari
    def to_dict(self):
        return {
            "nAlumnes": self.title,
            "nAules": self.pes,
            "superficie": self.color,
            "gimnas": self.sexo,
            "municipi": self.sexo,
            "graus": self.sexo
        }

    # Mètode que mostra per pantalla les dades de la classe
    def info(self):
        print("Dades de l'escola:")
        print(f"Nombre d'alumnes: {self.nAlumnes}")
        print(f"Nombre d'aules: {self.nAules}")
        print(f"Superfície: {self.superficie}m2")
        print(f"Té gimnàs: {self.gimnas}")
        print(f"Municipi: {self.municipi}")
        print(f"Graus: {self.graus}\n")

    # Getters per als atributs de la classe
    def getnAlumnes(self):
        return self.nAlumnes

    def getnAules(self):
        return self.nAules

    def getSuperficie(self):
        return self.superficie

    def getGimnas(self):
        return self.gimnas

    def getMunicipi(self):
        return self.municipi

    def getGraus(self):
        return self.graus

    # Setters per als atributs de la classe
    def setnAlumnes(self, nAlumnes):
        self.nAlumnes = nAlumnes

    def setnAules(self, nAules):
        self.nAules = nAules

    def setSuperficie(self, superficie):
        self.superficie = superficie

    def setGimnas(self, gimnas):
        self.gimnas = gimnas

    def setMunicipi(self, municipi):
        self.municipi = municipi

    def setGraus(self, graus):
        self.graus = graus
