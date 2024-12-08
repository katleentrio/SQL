# 1 Eerst deze code

#De omtrek en oppervlakte van een cirkel berekenen

#gegevens
straal = float(input("Geef de straal van de cirkel "))
PI = 3.1415926

#berekeningen
omtrek = 2*PI*straal
oppervlakte = PI*straal**2

#output
print("Voor een cirkel met een straal",straal,"cm")
print("is de omtrek",omtrek,"cm")
print("en de oppervlakte",oppervlakte,"cm²")



# 2 Dan met uitbreiding van round() deze code
Je voegt de round(variabale,aantal cijfers na de komma) toe

#De omtrek en oppervlakte van een cirkel berekenen

#gegevens
straal = float(input("Geef de straal van de cirkel "))
PI = 3.1415926

#berekeningen
omtrek = 2*PI*straal
oppervlakte = PI*straal**2

#output
print("Voor een cirkel met een straal",straal,"cm")
print("is de omtrek",round(omtrek,5),"cm")
print("en de oppervlakte",round(oppervlakte,5),"cm²")



This activity is an example of a content page, this is NOT an exercise. Note the `"type": "content"` in the `dirconfig.json`.
