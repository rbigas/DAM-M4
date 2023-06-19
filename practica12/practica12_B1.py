import json
#Aquest document crea un arxiu .json amb una key "book" i 4 objectes que corresponen a la informació de 4 llibres.
def arxiuJson():
    dades = {
        "book": [
            {
                "title": "The Hitchhiker's Guide to the Galaxy",
                "cover": "dura",
                "year": 1979,
                "pages": 224
            },
            {
                "title": "Las aventuras de Mari",
                "cover": "blanda",
                "year": 1968,
                "pages": 523
            },
            {
                "title": "Timmy and Tommy",
                "cover": "dura",
                "year": 2003,
                "pages": 52
            },
            {
                "title": "El Brujo Celestial",
                "cover": "blanda",
                "year": 1986,
                "pages": 324
            }
        ]
    }
    with open("practica12.json", 'w') as file:
        json.dump(dades, file, indent=2)