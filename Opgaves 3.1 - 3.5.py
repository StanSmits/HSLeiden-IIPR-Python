#Opgaves 3.1 - 3.5
#Opgave 3.1"

standardBookValue = 24.95
bookshopBookValue = standardBookValue * 0.6
"""
Boeken winkel koopt 60 boeken, de prijs van de boeken is bookshopBookValue, de verzendkosten zijn:
                                                                            1e boek - 3 euro
                                                                   elk boek volgend - 0.75 euro
"""

boekenKostenBerekening = float((bookshopBookValue * 60) + (59 * 0.75) + 3)

print("De totale kosten van 60 boeken is: ", format(boekenKostenBerekening , ".2f")) # https://www.codegrepper.com/code-examples/python/python+tofixed%282%29


#Opgave 3.2
#Los de volgende code op"
""" 
    print( "Een boodschap" ).
    print( "Een boodschap')
    print('Een boodschapf"')
"""

print("Een boodschap")
print("Een boodschap")
print('Een boodschapf"')


#Opgave 3.3
# Maak een programma wat een "ZeroDivisionError" output

import random as random

#print(random.randint(0, 10000) / 0)

#Opgave 3.4
#Fix de  volgende code:
"""" 
    print( ((2*3)/4 + (5-6/7)*8 )
    print( ((12*13)/14 + (15-16)/17)*18 )
"""

print(((2*3)/4 + (5-6/7)*8))
print(((12*13)/14 + (15-16)/17)*18)


#Opgave 3.5
# Het is momenteel 14.00 uur, je zet een alarm wat over 535 uur gaat
# Hoe laat gaat dit alarm af?

print(format(14.00 + (535 % 24), ".2f"), "uur")
