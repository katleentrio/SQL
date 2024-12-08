# Vraag de gebruiker om het factuurbedrag
factuurbedrag = float(input("Voer het factuurbedrag in: "))

# Controleer het factuurbedrag en bereken de korting
if factuurbedrag > 100:
    korting = "5%"
else:
    korting = "3%"

# Print de korting
print("Je hebt recht op", korting ,"korting")
print("Einde programma")

