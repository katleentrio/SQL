# Vraag het factuurbedrag op
bedrag = float(input("Voer het bedrag in: "))

# Vraag het delingsgetal op
delingsgetal = float(input("Voer het delingsgetal in: "))

# Voer de deling uit en rond af op 2 decimalen
resultaat = round(bedrag / delingsgetal, 3)

print("Het resultaat is", resultaat)
print("Einde programma")

