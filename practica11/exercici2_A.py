# Aquest codi llegeix una string per consola. Si aquesta correspon a un dels noms de la llista,
# retorna un missatge personalitzat per a cada nom. Si el nom no està a la llista, ho especifica
# per pantalla.

def llistaNoms():
    nomInput = input("Introdueix un dels següents noms: \nRoc, Roger, Jhamel, Joan, Jovani\n")
    if nomInput == "Roc":
        return("Hola {nomInput}, bon dia!!".format(nomInput=nomInput))
    elif nomInput == "Roger":
        return("Hola {nomInput}, encantat de veure't!!".format(nomInput=nomInput))
    elif nomInput == "Jhamel":
        return("Hola {nomInput}, no em caus bé >:(".format(nomInput=nomInput))
    elif nomInput == "Joan":
        return("Bones {nomInput}, m'agrada el teu nom.".format(nomInput=nomInput))
    elif nomInput == "Jovani":
        return("Encantat {nomInput}, espero que estiguis bé.".format(nomInput=nomInput))
    else:
        return("El nom que has introduït no està a la llista.")