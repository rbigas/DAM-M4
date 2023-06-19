import json
#Aquest document llegeix un arxiu .json i el mostra identat correctament
def llegirJson():
    with open("practica12.json", 'r') as file:
        resultat = json.load(file)
    print(json.dumps(resultat, indent = 2))