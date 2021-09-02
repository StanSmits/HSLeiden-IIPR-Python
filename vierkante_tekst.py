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

def vierkanteText(text):
    for i in text:
        print(text)

vierkanteText(input("Welke text wil je in een vierkantje? \n"))