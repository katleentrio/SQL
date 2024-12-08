naam = input("Voer jouw naam in: ")
geboortejaar = int(input("Voer jouw geboortejaar in: "))
huidig_jaar = int(input("Geef het huidig jaar in: "))

leeftijd = huidig_jaar-geboortejaar
                   
if leeftijd >=18:
    categorie = "volwassen persoon"
else:
    categorie = "kind"
    
print("Hallo",naam+ ", jij bent",leeftijd,"en jij bent een",categorie+".")
print("Einde programma")
