#Opgave 1:
"""
Maak een variabele xen geef die de waarde 10: x=10
Tel nu de waarde van x bij zichzelf op: x= x +x
Trek vervolgens 5 van de waarde van x af: x = x –5
Print dan de waarde van xop de Python console.
"""
x = 10
x = x + x
x = x - 5

print(x)


#Opgave 2
"""
Maak een variabele ymet de waarde 17.
Deel de waarde van y door 2 en print de uitkomst op de Python console
Wat voor type waarde is die uitkomst?
"""

y = 17
y = y / 2
print(type(y)) # variable y is een "float"


#Opgave 3
"""
Maak een variabele die aangeeft of het mooi weer is. Denk hierbij aan de naam van de variabele en wat voor type waarde je daarvoor gebruikt. 
Ga er van uit dat het weer op dit moment mooi is.
Maak een variabele die aangeeft of het slecht weer is. 
Gebruik voor het toewijzen van de waarde van deze ‘slechtweer' variabele de waarde van 'mooi weer' variabele.
Let op: het kan niet tegelijk slecht weer èn goed weer zijn!
Laat het dan mooi weer zijn en print de waarden van de ‘mooi weer’ variabele en de ‘slecht weer’ variabele op console.
"""

mooiWeer = True
slechtWeer = not mooiWeer

print("Is het mooi weer? ", mooiWeer, "\nIs het slecht weer?", slechtWeer)


#Opgave 4
"""
    Zet onderstaande code in het Python bestand en voer de code uit.
    De code geeft een foutmelding. Pas de code aan zodat de foutmelding is opgelost. 
    Wat was het achterliggende probleem van deze foutmelding?
    
    nummer = input( "Geef een getal: " )
    print( "Je getal in het kwadraat is", nummer * nummer )
"""

#nummer = float(input( "Geef een getal: " ))
#print( "Je getal in het kwadraat is", nummer * nummer)

#Achterliggende probleem is dat input een string type returnt (type(nummer) returnt string), je kan 2 strings niet met elkaar vermenigvuldigen.
#Daarom moet het type van "nummer" veranderd in een nummer (float / int), omdat een flaot werkt bij zowel int getallen en float nummers
# is het handiger om het getal in een float array te krijgen


#Opgave 5

"""
Maak een functie die als input je voornaam en achternaam vraagt en vervolgens je volledige naam teruggeeft.
Print de return waarde van de functie op console.
"""

def volledigeNaam(voornaam, achternaam): 
    print("Je volledige naam is", voornaam, achternaam)

volledigeNaam("Stan", "Smits")

#Opgave 6
"""
Schrijf een functie dat het aantal hoofden, schouders, knieën, en tenen op een feestje telt. 
De functie krijgt als parameter het aantal mensen op het feestje mee. 
Jouw functie moet vier variabelen definiëren genaamd aantal_hoofden , aantal_schouders , aantal_knieenen  aantal_tenen  waarin 
    de berekende waardes worden opgeslagen. 
Print vervolgens, in de functie, deze waardes naar hetscherm.
"""

def ledematenTellen(personen):
    aantalHoofden = personen * 1
    aantalSchouders = personen * 2
    aantalKnieen = personen * 2
    aantalTenen = (personen * 10)
    print("Er zijn in totaal:\n", aantalHoofden, "Hoofden\n", aantalSchouders, "Schouders\n", aantalKnieen, "Knieen\n", aantalTenen, "Tenen")

#ledematenTellen(int(input("Hoeveel mensen zijn er op het feestje?\n")))

#Opgave 7

"""
Schrijf een functie dieeen string aan de gebruiker vraagt en deze string parameter net zo vaak herhaalt als dat de gegeven string lang was. 
Deze nieuwe string wordt daarna teruggegeven. 
Iedere kopie van de originele string moet op een eigen regel. 
Voorbeeld input en resultaat:
“xxx”
wordt: 
"xxx\nxxx\nxxx\n"
Dus op console zie je:
xxx
xxx
xxx
"""
import time

def vierkanteText(text):
    for i in text:
        print(text)

vierkanteText("xxxx")

