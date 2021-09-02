#Opgave 4
"""
    Zet onderstaande code in het Python bestand en voer de code uit.
    De code geeft een foutmelding. Pas de code aan zodat de foutmelding is opgelost. 
    Wat was het achterliggende probleem van deze foutmelding?
    
    nummer = input( "Geef een getal: " )
    print( "Je getal in het kwadraat is", nummer * nummer )
"""

nummer = float(input( "Geef een getal: " ))
print( "Je getal in het kwadraat is", nummer * nummer)

#Achterliggende probleem is dat input een string type returnt (type(nummer) returnt string), je kan 2 strings niet met elkaar vermenigvuldigen.
#Daarom moet het type van "nummer" veranderd in een nummer (float / int), omdat een flaot werkt bij zowel int getallen en float nummers
# is het handiger om het getal in een float array te krijgen