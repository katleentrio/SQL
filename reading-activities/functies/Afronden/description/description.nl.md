# Resultaten afronden

De resultaten van de berekeningen worden in de huidige versie van het programma nog niet afgerond.

Om afrondingen in te bouwen, kan je de functie round() toevoegen.

Je voegt round(parameter,aantal cijfers na de komma) toe.


In het resultaat van ons voorbeeld komt nu een afronding van de uitkomsten op 5 cijfers na de komma.

## Voorbeeld

![image](image.png)

# De omtrek en oppervlakte van een cirkel berekenen

# gegevens
straal = float(input("Geef de straal van de cirkel "))
PI = 3.1415926

# berekeningen
omtrek = 2 * PI * straal
oppervlakte = PI * straal**2

# output
print("Voor een cirkel met een straal",straal,"cm")
print("is de omtrek",omtrek,"cm")
print("en de oppervlakte",oppervlakte,"cm²")