#Opgave Telefoonlijst

"""
Schrijf een functie die de lijst met waarden uit het telefoon_lijst.txt bestand inleest en het resultaat naar het scherm schrijft.
Roep de functie aan.
"""

def krijgTelefoonlijstWaardes():
    telefoonLijst =  open("Python Programming/telefoon_lijst.txt", mode="r").read().split("\n")
    for i in telefoonLijst:
        print(i)

krijgTelefoonlijstWaardes()
