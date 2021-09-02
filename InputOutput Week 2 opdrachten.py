#Opgave 6 Telefoonlijst

"""
Inventariseer samen met je klasgenoten (aan je tafel) de studentnummers, namen en telefoonnummers (laat een A4-tje rondgaan). 
Als je alleen werkt, mag je ook een aantal studenten verzinnen. 
Maak een telefoon_lijst.txt bestand van deze lijst met klasgenotenen plaats deze in dezelfde map als je Python module. 
In het tekstbestand komt iedere student op een nieuwe regel, met een komma ( , ) tussen de waarden:
    <studentnummer>,<naam>,<telefoon>
Schrijf een functie die de lijst met waarden uit het telefoon_lijst.txt bestand inleest en het resultaat naar het scherm schrijft.
Roep de functie aan.
"""

telefoonLijst = open("Python Programming/telefoonLijst.txt", "r").read()
telefoonLijstSplitted = telefoonLijst.split(",")

def callTelefoonLijst():
    print(telefoonLijstSplitted)

callTelefoonLijst()