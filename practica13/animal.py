class animal:

    # Constructor de la classe
    def __init__(self, nom, pes, familia, especie, longevitat, perillExtincio, poblacio):
        self.nom = nom
        self.pes = pes
        self.familia = familia
        self.especie = especie
        self.longevitat = longevitat
        self.perillExtincio = perillExtincio
        self.poblacio = poblacio

    # Mètode que mostra per pantalla les dades de la classe
    def salutacio(self):
        print("Dades de l'animal:")
        print(f"Nom: {self.nom}")
        print(f"Pes: {self.pes}kg")
        print(f"Família: {self.familia}")
        print(f"Especie: {self.especie}")
        print(f"Longevitat: {self.longevitat} anys")
        print(f"Perill d'extinció: {self.perillExtincio}")
        print(f"Població: {self.poblacio}\n")

    # Getters per als atributs de la classe animal
    def getPes(self):
        return self.pes
    
    def getFamilia(self):
        return self.familia
    
    def getEspecie(self):
        return self.especie
    
    def getLongevitat(self):
        return self.longevitat
    
    def getPerillExtincio(self):
        return self.perillExtincio
    
    def getPoblacio(self):
        return self.poblacio
    
    # Setters per als atributs de la classe animal
    def setPes(self, pes):
        self.pes = pes
    
    def setFamilia(self, familia):
        self.familia = familia
    
    def setEspecie(self, especie):
        self.especie = especie
    
    def setLongevitat(self, longevitat):
        self.longevitat = longevitat
    
    def setPerillExtincio(self, perillExtincio):
        self.perillExtincio = perillExtincio
    
    def setPoblacio(self, poblacio):
        self.poblacio = poblacio
