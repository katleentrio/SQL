# 1 je start met deze code

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

# 2 je vervolgt met deze code

(Je voegt sep="" aan je 3 regels output toe)
#De omtrek en oppervlakte van een cirkel berekenen

#gegevens
straal = float(input("Geef de straal van de cirkel "))
PI = 3.1415926

#berekeningen
omtrek = 2*PI*straal
oppervlakte = PI*straal**2

#output
print("Voor een cirkel met een straal ",straal,"cm",sep="")
print("is de omtrek ",round(omtrek,5),"cm",sep="")
print("en de oppervlakte ",round(oppervlakte,5),"cm²",sep="")

# 3 vervolgens met deze code

(Je voegt end=" " aan eerste 2 regels output toe)
#De omtrek en oppervlakte van een cirkel berekenen

#gegevens
straal = float(input("Geef de straal van de cirkel "))
PI = 3.1415926

#berekeningen
omtrek = 2*PI*straal
oppervlakte = PI*straal**2

#output
print("Voor een cirkel met een straal ",straal,"cm",sep="",end=" ")
print("is de omtrek ",round(omtrek,5),"cm",sep="",end=" ")
print("en de oppervlakte ",round(oppervlakte,5),"cm²",sep="")

# 4 Je eindigt met deze code

(Je voegt end="\nEinde programma" aan de laatste regel output toe)
#De omtrek en oppervlakte van een cirkel berekenen

#gegevens
straal = float(input("Geef de straal van de cirkel "))
PI = 3.1415926

#berekeningen
omtrek = 2*PI*straal
oppervlakte = PI*straal**2

#output
print("Voor een cirkel met een straal ",straal,"cm",sep="",end=" ")
print("is de omtrek ",round(omtrek,5),"cm",sep="",end=" ")
print("en de oppervlakte ",round(oppervlakte,5),"cm²",sep="",end="\nEinde programma")