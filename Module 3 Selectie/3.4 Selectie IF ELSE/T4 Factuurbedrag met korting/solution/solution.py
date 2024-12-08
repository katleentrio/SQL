# Vraag de gebruiker om het factuurbedrag
factuurbedrag = float(input("Wat is het factuurbedrag? "))

# Controleer het factuurbedrag en bereken de korting
if factuurbedrag > 100:
    korting = factuurbedrag * 0.05
else:
    korting = factuurbedrag * 0.03

# Bereken het bedrag na korting
bedrag_na_korting = factuurbedrag - korting

# Print de korting
print("Je hebt recht op",round(korting,2), "euro korting.")

# Print het bedrag na korting
print("Het bedrag inclusief korting bedraagt",round(bedrag_na_korting,2),"euro.")



print("Einde programma")