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


def voegNieuweTelefoonWaardes(studentNummer, naam, telefoonNummer):
    open("Python Programming/telefoon_lijst.txt", mode="a").write("\n" + studentNummer + "\n" + naam  + "\n" + telefoonNummer)
    

def vraagVoorWaardes():
    volledigeNaam = input("Wat is je naam: ")
    studentNummer = input("Wat is je studentennummer: ")
    telefoonNummer = input("Wat is je telefoonnummer: ")
    voegNieuweTelefoonWaardes(studentNummer, volledigeNaam, telefoonNummer)

vraagVoorWaardes()